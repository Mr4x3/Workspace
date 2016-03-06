import re
import os
di='/home/vivek/Dropbox/M.Tech Sem IV Research/SentiWord On Lyrics (Indore)/Code/left songs'
files=[f for f in os.listdir(di) if os.path.isfile(di+f)]
print(files)
pattern=re.compile(r'\b([a-zA-Z].+?)\b')
for f in files:
    with open(di+f) as file:
        for k in range(8):
            file.readline()
        for i in file:
            k=re.findall(pattern,i)
            arr=[]
            for _ in k:
                if len(_)>2:
                    arr.append(_)
            z=' '.join(arr)
            with open('Extracted/'+f,'a') as newfile:
                newfile.write(z)
                newfile.write('\n')
