from ortools.sat.python import cp_model



def contains_invalid_characters(s):
    return not set(s).issubset({'0', '1'})

def get_course_schedule(course):
    if course:
        schedule = course.schedule
        return [schedule.monday, schedule.tuesday, schedule.wednesday,
                schedule.thursday, schedule.friday, schedule.saturday, 
                schedule.sunday]
    return [False] * 7


def solver(maxCredits, hubString, courses):
    # Verify Inputs
    if maxCredits == None or hubString == None:
        print(f"Inputs are not both defined {maxCredits}, {hubString}")
        return 
    if len(hubString) != 16 or contains_invalid_characters(hubString):
        print(f"Malformed hubString: {hubString}, len: {len(hubString)}")
        return
    if maxCredits > 22:
        print(f"maxCredits not allowed to go that high {maxCredits}")
        return
    
    # Initialize the CP-SAT model
    model = cp_model.CpModel()

    num_hub_credits = len(hubString)

    # Create a binary variable for each course
    course_vars = []
    for course in courses:
        course_vars.append(model.NewBoolVar(course['course_name']))

    # Constraint: No overlapping classes
    for i in range(len(courses)):
        schedule_i = get_course_schedule(courses[i])
        for j in range(i + 1, len(courses)):
            schedule_j = get_course_schedule(courses[j])
            same_day = any(schedule_i[day] and schedule_j[day] for day in range(7))
            if not same_day or same_day and courses[i]['end_time'] > courses[j]['start_time'] and courses[i]['start_time'] < courses[j]['end_time']:
                model.Add(course_vars[i] + course_vars[j] <= 1)
    
    # Constraint: Total credits should not exceed maxCredits
    total_credits = sum(course_vars[i] * courses[i]['credits'] for i in range(len(courses)))
    model.Add(total_credits <= maxCredits)

    # Objective: Maximize HUB credits
    hub_credits = [0] * num_hub_credits
    for i, course in enumerate(courses):
        for j in range(num_hub_credits):
            if course['hub_credits'][j] == '1' and hubString[j] == '1':
                hub_credits[j] += course_vars[i]

    model.Maximize(sum(hub_credits))

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    selectedCourses = []
    netHubCredits = 0
    creditsUsed = 0

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        
        for i, course in enumerate(courses):
            if solver.BooleanValue(course_vars[i]):
                
                creditsUsed += course["credits"]
                selectedCourses.append(course)
        netHubCredits = solver.ObjectiveValue()
    else:
        print('No feasible solution found.')
    
    return {'Solution':selectedCourses, 
            'Credits Used': creditsUsed,
            'Net Hub Credits': netHubCredits}

if __name__ == "__main__":
    maxCredits = 3
    hubString = '1111111111111111' # 16 char string, each digit represents a yes or no for if user needs that hub unit
    solver(maxCredits, hubString)