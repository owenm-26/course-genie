from ortools.sat.python import cp_model

def contains_invalid_characters(s):
    return not set(s).issubset({'0', '1'})

def get_all_courses():
    from app import app, see_table
    with app.app_context():
        return see_table('courses').get_json()

def get_course_schedule(schedule_id):
    from models import Schedule
    from app import app
    with app.app_context():
        if schedule_id:
            schedule = Schedule.query.get(schedule_id)
            return [schedule.monday, schedule.tuesday, schedule.wednesday,
                    schedule.thursday, schedule.friday, schedule.saturday, 
                    schedule.sunday]
        return [False] * 7
    
def get_hub_credits(hub_credits_id):
    from models import HubCredits
    from app import app
    with app.app_context():
        if hub_credits_id:
            hub_credits = HubCredits.query.get(hub_credits_id)
            return [
                int(hub_credits.historical_context), 
                int(hub_credits.individual_in_community), 
                int(hub_credits.research_and_information),
                int(hub_credits.social_inquiry_2), 
                int(hub_credits.global_citizenship), 
                int(hub_credits.writing_intensive), 
                int(hub_credits.ethical_reasoning), 
                int(hub_credits.critical_thinking), 
                int(hub_credits.creativity_and_innovation), 
                int(hub_credits.teamwork_and_collaboration), 
                int(hub_credits.scientific_inquiry_1), 
                int(hub_credits.digital_multimedia), 
                int(hub_credits.oral_and_signed_communication), 
                int(hub_credits.aesthetic_exploration), 
                int(hub_credits.philosophical_inquiry),
                int(hub_credits.first_year_writing)
            ]
        return [0] * 16

def solver(maxCredits, hubString, courses):
    # Verify Inputs
    if maxCredits is None or hubString is None:
        return (f"Inputs are not both defined {maxCredits}, {hubString}") 
    if len(hubString) != 16 or contains_invalid_characters(hubString):
        return (f"Malformed hubString: {hubString}, len: {len(hubString)}")
    if maxCredits > 22:
        return (f"maxCredits not allowed to go that high {maxCredits}")
    
    # Initialize the CP-SAT model
    model = cp_model.CpModel()

    num_hub_credits = len(hubString)

    # Create a binary variable for each course
    course_vars = [model.NewBoolVar(course['course_name']) for course in courses]

    # Identify which courses have 0 credits
    zero_credit_courses = [i for i, course in enumerate(courses) if course['credits'] == 0]

    # Create a binary variable to indicate if any 0-credit course is selected. ONLY ONE ALLOWED
    if zero_credit_courses:
        zero_credit_var = model.NewBoolVar('zero_credit_var')
        model.Add(sum(course_vars[i] for i in zero_credit_courses) <= 1)
        model.Add(sum(course_vars[i] for i in zero_credit_courses) == zero_credit_var)


    # Constraint: No overlapping classes
    for i in range(len(courses)):
        schedule_i = get_course_schedule(courses[i]['schedule_id'])
        for j in range(i + 1, len(courses)):
            schedule_j = get_course_schedule(courses[j]['schedule_id'])
            same_day = any(schedule_i[day] and schedule_j[day] for day in range(7))
            if same_day and not (courses[i]['end_time'] <= courses[j]['start_time'] or courses[i]['start_time'] >= courses[j]['end_time']):
                model.Add(course_vars[i] + course_vars[j] <= 1)

    # Constraint: Total credits should not exceed maxCredits
    total_credits = sum(course_vars[i] * courses[i]['credits'] for i in range(len(courses)))
    model.Add(total_credits <= maxCredits)


    # Objective: Maximize HUB credits
    hub_credits = []
    for j in range(num_hub_credits):
        hub_credits_j = sum(course_vars[i] * get_hub_credits(courses[i]['hub_credits_id'])[j] for i in range(len(courses)))
        if hubString[j] == '1':
            hub_credits.append(hub_credits_j)
    
    model.Maximize(sum(hub_credits))

    # Solve the model
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 60
    status = solver.Solve(model)

    selectedCourses = []
    selectedCourseIds = []
    netHubCredits = 0
    creditsUsed = 0
    gainedHubCredits = [0] * num_hub_credits

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        print('Feasible solution found.')
        for i, course in enumerate(courses):
            if solver.BooleanValue(course_vars[i]):
                creditsUsed += course["credits"]
                selectedCourses.append(course)
                selectedCourseIds.append(course['id'])

                 # Track which HUB credits were gained
                hubs_i = get_hub_credits(course['hub_credits_id'])
                for j in range(num_hub_credits):
                    if hubString[j] == '1' and hubs_i[j] == 1:
                        gainedHubCredits[j] = 1
        netHubCredits = sum(gainedHubCredits)
    else:
        print('No feasible solution found.')
    
    gainedHubString = format(int(hubString, 2) & int(''.join(str(value) for value in gainedHubCredits), 2), f'0{num_hub_credits}b')

    return {
        # 'Selected Courses': selectedCourses, 
        'Selected Course Ids': selectedCourseIds,
        'Credits Used': creditsUsed,
        'Net Hub Credits': netHubCredits,
       'Gained (Needed) Hub String': gainedHubString,
        'Total Hubs String': format(int(gainedHubString,2) | int(hubString, 2), f'0{num_hub_credits}b')
    }

if __name__ == "__main__":
    maxCredits = 16
    hubString = '0000111100001111' # 16 char string, each digit represents a yes or no for if user needs that hub unit
    solution = solver(maxCredits, hubString, courses=get_all_courses())
    print(solution)
