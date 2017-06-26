def convert_to_numeric(score):
    """
    Uma função que converte a nota em float
    """
    return float(score)

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Soma os três valores médios, entre os cinco informados)
    """
    max_score = max(score1,score2,score3,score4,score5)
    min_score = min(score1,score2,score3,score4,score5)
    return score1 + score2 + score3 + score4 + score5 - max_score - min_score

def score_to_rating_string(score):
    """
    Função que converte a nota média em uma string
    """
    if (0 <= score < 1):
        rating = "Terrible"
    elif (1 <= score < 2):
        rating = "Bad"
    elif (2 <= score < 3):
        rating = "OK"
    elif (3 <= score < 4):
        rating = "Good"
    elif (4 <= score <= 5):
        rating = "Excellent"
    else:
        rating = "Out of range!"
    return rating

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

###MAIN
#print("int: " + str(convert_to_numeric(3)))
#print("str: " + str(convert_to_numeric("3")))
#print("float: " + str(convert_to_numeric(3.0)))
#print(sum_of_middle_three(1,2,3,4,1))
#print("Rating: " + score_to_rating_string(0))
#print("Rating: " + score_to_rating_string(1))
#print("Rating: " + score_to_rating_string(2))
#print("Rating: " + score_to_rating_string(3))
#print("Rating: " + score_to_rating_string(4))
#print("Rating: " + score_to_rating_string(5))
#print("Rating: " + score_to_rating_string(6))
#print("Rating: " + score_to_rating_string(-1))
#print("Rating: " + score_to_rating_string(1000))

#END
print("Final rating: " + scores_to_rating(0.5, 0.6,2,3,4))
