def which_prize(pontos):
    premio = None
    if 0<=pontos<=50:
        premio="wooden rabbit"
    elif 151 <= pontos <= 180:
        premio="wafer-thin mint"
    elif 181 <= pontos <= 200:
        premio="penguin"
    if premio:
        return "Congratulations! You have won a {}!".format(premio)
    else:
        return "Oh dear, no prize this time."
    
#print(which_prize(12))
