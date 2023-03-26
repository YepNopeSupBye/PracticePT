# This program calculates the average score of a student's 3 exams.

def get_scores():
    # Get input from the user for three exam scores
    exam_scores = []
    print("Scores range from 1 - 100")
    for i in range(3):
        score = float(input("Enter score for exam " + str(i+1) + ": "))
        exam_scores.append(score)
    return exam_scores

def calculate_average(scores):
    # Calculate the average score
    total = sum(scores)
    average = total / len(scores)
    return average

# Call the get_scores function to get the exam scores
scores_list = get_scores()


