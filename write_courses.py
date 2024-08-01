from datetime import datetime
from app import db, Course, app
from helpers.scrape import fetch_and_write_response

def write_courses(courses):
    table_instances = []
    # table_instances = [Course(course_name=obj.field1, catalog_number=obj.field2, time=obj.field2, labs=obj.field2, discussions=obj.field2, schedule_id=obj.field2, hub_credits_id=obj.field2) for obj in courses]
    for course in courses:
        course_name = course['descr']
        catalog_number = (course['catalog_nbr'])
        class_section = course['class_section']
        start_dt = datetime.strptime(course['start_dt'], "%m/%d/%Y")  # Assuming date format is MM/DD/YYYY
        lab_parent_id = None
        discussion_parent_id = None
        schedule_id = None
        hub_credits_id = None

        course_instance=Course(course_name, catalog_number, class_section, start_dt, lab_parent_id, discussion_parent_id, schedule_id, hub_credits_id)
        table_instances.append(course_instance)
        # print('--------Course Added:', course_instance)

    try:
        with app.app_context():
            db.session.add_all(table_instances)
            db.session.commit()
        return 'Courses written to the database successfully!'
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