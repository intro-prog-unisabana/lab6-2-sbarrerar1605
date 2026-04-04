def student_averages(students):
    result = {}
    
    for student, grades in students.items():
        if grades:
            avg = round(sum(grades.values()) / len(grades))
            result[student] = avg
    
    return result


def assignment_averages(students):
    if not students:
        return {}

    result = {}

    assignments = set()
    for grades in students.values():
        assignments.update(grades.keys())

    for assignment in assignments:
        total = 0
        count = 0

        for grades in students.values():
            if assignment in grades:
                total += grades[assignment]
                count += 1

        result[assignment] = round(total / count)

    return result