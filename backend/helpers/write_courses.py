from datetime import datetime

from sqlalchemy import null, text
from app import db, app  
from models import HubCredits, Course, Schedule
# from helpers.scrape import fetch_and_write_response
from datetime import datetime


# helper to map hub credits
def map_hub_credits(crse_attr_value):
    hub_credits = {
        'historical_context': False, 
        'individual_in_community': False,
        'research_and_information': False,
        'social_inquiry_2': False,
        'global_citizenship': False,
        'writing_intensive': False,
        'ethical_reasoning': False,
        'critical_thinking': False,
        'creativity_and_innovation': False,
        'teamwork_and_collaboration': False,
        'scientific_inquiry_1': False,
        'digital_multimedia': False,
        'oral_and_signed_communication': False,
        'aesthetic_exploration': False,
        'philosophical_inquiry': False,
        'first_year_writing': False
    }
    if 'HUB-HCO' in crse_attr_value:
        hub_credits['historical_context'] = True
    if 'HUB-IIC' in crse_attr_value:
        hub_credits['individual_in_community'] = True
    if 'HUB-RIL' in crse_attr_value:
        hub_credits['research_and_information'] = True
    if 'HUB-SO2' in crse_attr_value:
        hub_credits['social_inquiry_2'] = True
    if 'HUB-GCI' in crse_attr_value:
        hub_credits['global_citizenship'] = True
    if 'HUB-WIN' in crse_attr_value:
        hub_credits['writing_intensive'] = True
    if 'HUB-ETR' in crse_attr_value:
        hub_credits['ethical_reasoning'] = True
    if 'HUB-CRT' in crse_attr_value:
        hub_credits['critical_thinking'] = True
    if 'HUB-CRI' in crse_attr_value:
        hub_credits['creativity_and_innovation'] = True
    if 'HUB-TWC' in crse_attr_value:
        hub_credits['teamwork_and_collaboration'] = True
    if 'HUB-SI1' in crse_attr_value:
        hub_credits['scientific_inquiry_1'] = True
    if 'HUB-DME' in crse_attr_value:
        hub_credits['digital_multimedia'] = True
    if 'HUB-OSC' in crse_attr_value:
        hub_credits['oral_and_signed_communication'] = True
    if 'HUB-AEX' in crse_attr_value:
        hub_credits['aesthetic_exploration'] = True
    if 'HUB-PLM' in crse_attr_value:
        hub_credits['philosophical_inquiry'] = True
    if 'HUB-FYW' in crse_attr_value:
        hub_credits['first_year_writing'] = True

    return hub_credits

def map_schedule(rawSchedule):
    schedule = {
        'monday': False,
        'tuesday': False,
        'wednesday': False,
        'thursday': False,
        'friday': False,
        'saturday': False,
        'sunday': False
    }
    if rawSchedule == 'TBA':
        return schedule
    if 'Mo' in rawSchedule:
        schedule['monday'] = True
    if 'Tu' in rawSchedule:
        schedule['tuesday'] = True
    if 'We' in rawSchedule:
        schedule['wednesday'] = True
    if 'Th' in rawSchedule:
        schedule['thursday'] = True
    if 'Fr' in rawSchedule:
        schedule['friday'] = True
    if 'Sa' in rawSchedule:
        schedule['saturday'] = True
    if 'Su' in rawSchedule:
        schedule['sunday'] = True
    return schedule

def convertToLegibleTime(start_time):

    if len(start_time) == 0:
        return 'Undecided'
    # Define the format of the input time string
    input_format = '%H.%M.%S.%f%z'
    
    # Parse the input time string to a datetime object using the correct method
    dt = datetime.strptime(start_time, input_format)
    
    # Convert the datetime object to the desired output format
    output_format = '%I:%M %p'
    american_time = dt.strftime(output_format)
    
    return american_time

def write_courses(courses):
    course_instances = []
    hub_credit_instances = {}
    schedule_instances = {}

    with app.app_context():
        # start fresh
        db.session.execute(text('DROP TABLE IF EXISTS course CASCADE'))
        # db.session.execute(text('DROP TABLE IF EXISTS course CASCADE'))
        # db.session.execute(text('DROP TABLE IF EXISTS hub_credits CASCADE'))
        # db.session.execute(text('DROP TABLE IF EXISTS schedule CASCADE'))
        # db.session.execute(text('DROP TABLE IF EXISTS schedule CASCADE'))
        # db.session.execute(text('DROP TABLE IF EXISTS schedule CASCADE'))
        # db.session.execute(text('DROP TABLE IF EXISTS schedule CASCADE'))
        
        db.create_all()

        skipped_courses = 0
        
        for course in courses:
            if len(course["meetings"]) == 0 or len(course['crse_attr']) == 0 or len(course['meetings'][0]) == 0:
                skipped_courses +=1
                continue
          
            course_name = course['descr']
            catalog_number = course['catalog_nbr']
            class_section = course['class_section']
            start_time = convertToLegibleTime(course['meetings'][0]['start_time'])
            end_time = convertToLegibleTime(course['meetings'][0]['end_time'])
            instructor = course['meetings'][0]['instructor']
            credits = course['units']

            lab_parent_id = None
            discussion_parent_id = None

            if start_time == "Undecided" or end_time == "Undecided":
                skipped_courses +=1
                continue
            
            if 'bldg_cd' in course['meetings'][0]:
                class_room = course['meetings'][0]['bldg_cd'] + ' ' + course['meetings'][0]['room']
            else:
                class_room = 'Undecided'

            # CREATE HUB CREDITS RELATION
            hub_credits_dict = map_hub_credits(course["crse_attr_value"])

            # Create a unique key for each HubCredits instance
            hub_credits_key = tuple(hub_credits_dict.items())

            if hub_credits_key not in hub_credit_instances:
                hub_credit_instance = HubCredits(**hub_credits_dict)
                db.session.add(hub_credit_instance)
                db.session.commit()

                # Retrieve the committed instance to ensure we have the ID
                hub_credit_instance = HubCredits.query.filter_by(**hub_credits_dict).first()
                if hub_credit_instance:
                    hub_credit_instances[hub_credits_key] = hub_credit_instance
                else:
                    print(f'Error: HubCredits instance not found after commit for key: {hub_credits_key}')
                    continue
            else:
                hub_credit_instance = hub_credit_instances[hub_credits_key]

            # print(f'Creating course with hub_credits_id: {hub_credit_instance.id}')

            # CREATE SCHEDULE RELATION

            schedule_dict = map_schedule(course["meetings"][0]['days'])

            # Create a unique key for each HubCredits instance
            schedule_key = tuple(schedule_dict.items())

            if schedule_key not in schedule_instances:
                schedule_instance = Schedule(**schedule_dict)
                db.session.add(schedule_instance)
                db.session.commit()

                # Retrieve the committed instance to ensure we have the ID
                schedule_instance = Schedule.query.filter_by(**schedule_dict).first()
                if schedule_instance:
                    schedule_instances[schedule_key] = schedule_instance
                else:
                    print(f'Error: HubCredits instance not found after commit for key: {schedule_key}')
                    continue
            else:
                schedule_instance = schedule_instances[schedule_key]

            # print(f'Creating course with hub_credits_id: {schedule_instance.id}')

            # Create Course instance with the valid hub_credits_id
            course_instance = Course(
                course_name=course_name,
                catalog_number=catalog_number,
                class_section=class_section,
                start_time= start_time,
                end_time = end_time,
                instructor = instructor,
                class_room = class_room,
                lab_parent_id=lab_parent_id,
                discussion_parent_id=discussion_parent_id,
                schedule_id=schedule_instance.id,
                hub_credits_id=hub_credit_instance.id,
                credits=credits
            )
            if course_instance.hub_credits_id is not None:
                course_instances.append(course_instance)

        try:
            db.session.add_all(course_instances)
            db.session.commit()
            return f'{len(course_instances)} Courses written to the database successfully! {skipped_courses} Courses skipped!'
        except Exception as e:
            db.session.rollback()
            return f'Failed to write courses to the database: {str(e)}'



def main():
    # from newScrape import scraper
    # response = scraper()
    # if response["status"] == 200:
    #     result = write_courses(response["body"])
    #     print('result', result)
    # else:
    #     print('ERROR:', response["status"], response["body"])
    pass

if __name__ == '__main__':
    with app.app_context():
        main()
