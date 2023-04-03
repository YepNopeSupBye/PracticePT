# This program calculates the average score of a student's 3 exams.

def get_scores():
    # Get input from the user for three exam scores
    exam_scores = []
    print("Scores range from 1 - 100")
    while True:
        try:
            User_Input = int(input("How Many Exams Have You Had? "))
            break
        except ValueError:
            print("Enter int")
    for i in range(User_Input):
        while True:
            try:
                score = float(input("Enter score for exam " + str(i+1) + ": "))
                break
            except ValueError:
                print("Enter float")
        exam_scores.append(score)
    return exam_scores

def calculate_average(scores_list):
    # Calculate the average score
    sum = 0
    for j in scores_list:
        sum += j
    average = sum / len(scores_list)
    return float(round(average, 2))

# Call the get_scores function to get the exam scores
scores_list = get_scores()
print("Your Average score is " + str(calculate_average(scores_list)))


