# This program calculates the average score of a student's 3 exams.

def get_scores():
    # Get input from the user for three exam scores
    exam_scores = []
    print("Scores range from 1 - 100")
    for i in range(3):
        score = float(input("Enter score for exam " + str(i+1) + ": "))
        exam_scores.append(score)
    return exam_scores

def calculate_average(scores_list):
    # Calculate the average score
    sum = 0
    for j in scores_list:
        sum += j
    average = sum / len(scores_list)
    return float(average)

# Call the get_scores function to get the exam scores
scores_list = get_scores()
print("Your Average score is " + str(calculate_average(scores_list)))


