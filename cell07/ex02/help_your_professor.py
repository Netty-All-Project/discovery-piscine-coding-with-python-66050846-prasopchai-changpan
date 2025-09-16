def average(class_scores):
    """
    Takes a dictionary as a parameter, associating the students' first
    names with their scores on an assignment, and calculate the class average for that assignment.
    """
    total_score = sum(class_scores.values())
    num_students = len(class_scores)
    if num_students == 0:
        return 0  # Avoid division by zero
    return total_score / num_students

# Example usage:
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}")
print(f"Average for class 3C: {average(class_3C)}")