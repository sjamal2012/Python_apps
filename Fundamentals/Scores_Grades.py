def scores():
    for i in range(10):
        import random
        score = random.randint(60, 100)
        grade = ""
        if 60 <= score <= 69:
            grade = "D"
        elif 70 <= score <= 79:
            grade = "C"
        elif 80 <= score <= 89:
            grade = "B"
        elif 90 <= score <= 100:
            grade = "A"

        print "Score: " + str(score) + "; Your grade is " + grade
print "Scores and Grades"
scores()
