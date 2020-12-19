Score_A=int(input('Enter the score of Team A'))
Score_B=int(input('Enter the socre of Team B'))
if Score_A > Score_B:
    print("Team A is the winner")
elif Score_B == Score_A:
    Super_Score_A=int(input('Enter The super over Score of Team A'))
    Super_Score_B=int(input('Enter the super over Score of Teamb'))
    if Super_Score_A > Super_Score_B:
        print("Team A is the winner Team")
    else:
        print("Team B is the winner Team")
else:
    print("Team B is the Winner")