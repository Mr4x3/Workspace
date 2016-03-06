#!/usr/bin/python3

import sys

"""def process(i,j,arr):
    l=0
    if arr[i]==arr[j]:
        print(i,j)
        #p=1
        #r,t=i,j
        for x in range(i,j+1):
            if line[x+1]==line[x+(j-i)+1]:
                l=l+1
            else:
                break
    return l

with open(sys.argv[1], 'r') as input:
    line_list = input.read().strip().splitlines()

for line in line_list:
    print(line)
    l=0
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            l=process(i,j,line)
            print(l)
            if l!=0:
                print('#',l)
                break
            

"""
import sys

def main():
	with open(sys.argv[1]) as f:
		for l in f:
			l = l.strip()
			seen = set() 
			count = 0
			for char in l:
				if char not in seen:
					seen.add(char)
					count = count+1
			print count

if __name__=="__main__":
   main()
