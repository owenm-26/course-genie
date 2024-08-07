from datetime import datetime

from sqlalchemy import null
from app import db, app  
from models import HubCredits, Course
from helpers.scrape import fetch_and_write_response

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

def write_courses(courses):
    course_instances = []
    hub_credit_instances = {}

    with app.app_context():
        # start fresh
        db.drop_all()
        db.create_all()
        
        for course in courses:
            course_name = course['descr']
            catalog_number = course['catalog_nbr']
            class_section = course['class_section']
            start_dt = datetime.strptime(course['start_dt'], "%m/%d/%Y")
            lab_parent_id = None
            discussion_parent_id = None
            schedule_id = None

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

            print(f'Creating course with hub_credits_id: {hub_credit_instance.id}')

            # Create Course instance with the valid hub_credits_id
            course_instance = Course(
                course_name=course_name,
                catalog_number=catalog_number,
                class_section=class_section,
                time=start_dt,
                lab_parent_id=lab_parent_id,
                discussion_parent_id=discussion_parent_id,
                schedule_id=schedule_id,
                hub_credits_id=hub_credit_instance.id
            )
            if course_instance.hub_credits_id != null:
                course_instances.append(course_instance)

        try:
            db.session.add_all(course_instances)
            db.session.commit()
            return f'{len(course_instances)} Courses written to the database successfully!'
        except Exception as e:
            db.session.rollback()
            return f'Failed to write courses to the database: {str(e)}'



def main():
    response = fetch_and_write_response()
    if response["status"] == 200:
        result = write_courses(response["body"])
        print('result', result)
    else:
        print('ERROR:', response["status"], response["body"])

if __name__ == '__main__':
    with app.app_context():
        main()
