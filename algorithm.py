from ortools.sat.python import cp_model

def contains_invalid_characters(s):
    return not set(s).issubset({'0', '1'})

def solver(maxCredits, hubString):
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

    # Example data
    courses = [
        {'id': 1, 'name': 'Course 1', 'start_time': 9, 'end_time': 10, 'credits': 3, 'hub_credits': '1010100000000000'},
        {'id': 2, 'name': 'Course 2', 'start_time': 10, 'end_time': 11, 'credits': 3, 'hub_credits': '0100000000000000'},
        # Add more courses with start_time, end_time, credits, and hub_credits
    ]

    num_hub_credits = len(hubString)

    # Create a binary variable for each course
    course_vars = []
    for course in courses:
        course_vars.append(model.NewBoolVar(course['name']))

    # Constraint: No overlapping classes
    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            if courses[i]['end_time'] > courses[j]['start_time'] and courses[i]['start_time'] < courses[j]['end_time']:
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

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print('Selected courses:')
        for i, course in enumerate(courses):
            if solver.BooleanValue(course_vars[i]):
                print(course['name'])
        print('Total HUB credits:', solver.ObjectiveValue())
    else:
        print('No feasible solution found.')

if __name__ == "__main__":
    maxCredits = 3
    hubString = '1111111111111111' # 16 char string, each digit represents a yes or no for if user needs that hub unit
    solver(maxCredits, hubString)