#Mia
while True:
    TestCase = input()
    if TestCase == "0 0 0 0":
        break
    else:
        s0, s1, r0, r1 = map(int, TestCase.split(" "))
        Player1 = [s0, s1]
        Player1.sort(reverse = True)
        Player2 = [r0, r1]
        Player2.sort(reverse = True)
        if Player1 == Player2:
            print("Tie.")
        else:
            if Player1 == [2, 1]:
                print("Player 1 wins.")
            elif Player2 == [2, 1]:
                print("Player 2 wins.")
            elif r0 == r1 and s0 != s1:
                print("Player 2 wins.")
            elif s0 == s1 and r0 != r1:
                print("Player 1 wins.")
            elif (Player1[0] * 10) + (Player1[1]) > (Player2[0] * 10) + (Player2[1]):
                print("Player 1 wins.")
            elif (Player1[0] * 10) + (Player1[1]) < (Player2[0] * 10) + (Player2[1]):
                print("Player 2 wins.")
#SOLVED