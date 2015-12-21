import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    age=int(test)
    if age in range(0,3):
        print("Still in Mama's arms")
    elif age in range(3,5):
        print("Preschool Maniac")
    elif age in range(5,12):
        print("Elementary school")
    elif age in range(12,15):
        print("Middle school")
    elif age in range(15,19):
        print("High school")
    elif age in range(19,23):
        print("College")
    elif age in range(23,66):
        print("Working for the man")
    elif age in range(66,101):
        print("The Golden Years")
    else:
        print("This program is for humans")
    
