def minion_game(string):
    string = string.strip()
    stringLength = len(string)
    player1, player2 = 0,0
    for i in range(stringLength):
        if string[i] in "AEIOU":
            player1 += stringLength - i
        else:
            player2 += stringLength - i        
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart", player2)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)