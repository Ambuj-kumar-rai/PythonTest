Total_class=int(input('Enter the total number of classes'))
Attend_class=int(input('Enter the number of classes you attend'))
Medical=input("had you faced some medical issue\t press Y for yes and N for no")
Medical_issue=Medical.upper()
attendance=(Attend_class/Total_class)*100

if Medical_issue == "Y":
    criteria=60
elif Medical_issue == "N":
    criteria=75
if Medical_issue == "Y":
    if attendance > criteria:
        print(True)
    else:
        print(False)
elif Medical_issue == "N":
    if attendance > criteria:
        print(True)
    else:
        print(False)
