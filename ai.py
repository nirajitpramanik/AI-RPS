import json
from helper import *
    
def winner(choice):
    """
    Defining the winner based on the choice
    """
    if choice == "r":
        return "p"
    elif choice == "p":
        return "s"
    else:
        return "r"

def model1(choices = None):
    """
    Predicting the output based on the user's last round choice
    """
    if not choices:
        return winner(winner(read_data(1)))
    else:
        return winner(read_data(1))
    
def model2(choices):
    """
    Move based on the last 3 rounds
    """
    try:
        r1, r2, r3 = choices[-3], choices[-2], choices[-1]

        if (r1 == r2) and (r2 == r3):
            return winner(r1)
        elif (r1 == r2):
            return winner(r1)
        elif (r1 == r3):
            return winner(r2)
        elif (r2 == r3):
            return winner(r2)
        else:
            return winner(r1)
    except:
        try:
            r1, r2 = choices[-2], choices[-1]

            if (r1 == r2):
                return winner(r1)
            else:
                return winner(r2)
        except:
            return model1(choices)
        
def model3(choices):
    """
    Most commonly used choice
    """
    rc, sc, pc = choices.count("r"), choices.count("p"), choices.count("s")
    
    if (rc > sc and rc > pc):
        return "p"
    elif (sc > pc and sc > rc):
        return "r"
    else:
        return "s"
    
def model4(choices):
    """
    Least commonly used choice
    """
    rc, sc, pc = choices.count("r"), choices.count("p"), choices.count("s")
    
    if (rc < sc and rc < pc):
        return "p"
    elif (sc < pc and sc < rc):
        return "r"
    else:
        return "s"
    
def calc_score(record):
    """
    Calculates score for the model
    """
    numerator = 0
    denominator = 0
    for i in range(len(record)):
        numerator += (record[i] * (i ** 2))
        denominator += (i ** 2)
    try:
        score = numerator / denominator
    except ZeroDivisionError:
        score = 0
    return score

def choose_model():
    """
    Chooses the model based on the score
    """
    m1, m2, m3, m4 = read_data(2)

    if not m1:
        return model1()
    else:
        scores = [calc_score(m1), calc_score(m2), calc_score(m3), calc_score(m4)]

        max_score = max(scores)
        record = read_data(3)

        if max_score == scores[0]:
            return model1(record)
        elif max_score == scores[1]:
            return model2(record)
        elif max_score == scores[2]:
            return model3(record)
        elif max_score == scores[3]:
            return model4(record)

def rate_all_models(user):
    """
    Rates all the models based on the output it predicted.
    """
    data = read_data(3)
    m1_choice, m2_choice, m3_choice, m4_choice = model1(data), model2(data), model3(data), model4(data)
    wm1, wm2, wm3, wm4 = declare_winner(user, m1_choice), declare_winner(user, m2_choice), declare_winner(user, m3_choice), declare_winner(user, m4_choice)
    data1, data2, data3, data4 = read_data(2)

    if wm1 == "Player":
        data1.append(-1)
    elif wm1 == "Computer":
        data1.append(1)
    elif wm1 == "Draw":
        data1.append(0)

    if wm2 == "Player":
        data2.append(-1)
    elif wm2 == "Computer":
        data2.append(1)
    elif wm2 == "Draw":
        data2.append(0)

    if wm3 == "Player":
        data3.append(-1)
    elif wm3 == "Computer":
        data3.append(1)
    elif wm3 == "Draw":
        data3.append(0)

    if wm4 == "Player":
        data4.append(-1)
    elif wm4 == "Computer":
        data4.append(1)
    elif wm4 == "Draw":
        data4.append(0)

    with open("logs.json", "r") as fp:
        data = json.load(fp)

    if data["Round"] == 1:
        data["1"], data["2"], data["3"], data["4"] = data1, [0], [0], [0]
    else:
        data["1"], data["2"], data["3"], data["4"] = data1, data2, data3, data4

    data["Choices"].append(user)
    data["Last"] = user
    data["Round"] += 1

    with open("logs.json", "w") as f:
        json.dump(data, f, indent = 2)