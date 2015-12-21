import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

CHAR = [
	'-**----*--***--***---*---****--**--****--**---**--',
	'*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-',
	'*--*---*---**---**--****-***--***----*---**---***-',
	'*--*---*--*-------*----*----*-*--*--*---*--*----*-',
	'-**---***-****-***-----*-***---**---*----**---**--',
	'--------------------------------------------------']
width=5
height=6


for test in test_cases:
    digits=[]
    for i in test:
        if i.isdigit():
            digits.append(i)
    x=''
    for i in range(height):
        for j in digits:
            index=int(j)*width
            x=x+CHAR[i][index:index+5]
        x=x+'\n'
    print(x,end='')
        
            
            
        
                
