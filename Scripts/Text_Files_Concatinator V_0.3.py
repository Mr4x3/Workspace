""" Often We Have Many File Of text and we want them all in to one file,
This is the Thing You Were Looking For"""
#Program Released Under BSD Licence
#Created By Mr.4x3 And May Be Distributed Any Further But With Some Credit
#If Any Bug Found Please Mail At: Mr4x3@crushus.com
#So To Use It Just Put This File File In The Directry Where You Want To
#Concatinate
#It Means Source Of The Files

ver = .3

import os

Texo=1
Texography='This is Generated By Text File Concatinator V{} By Mr.4x3 \n \
Get Latest Version of this Script at http://doyl.in/scripts For Free.'.format(ver)

def ReadWrite(input_file, output_file='{}_Mr.4x3.TxT'.format(os.getcwd().split(os.sep)[-1])):
    """Write Given Input File To To A Give File"""
    global Texo
    if Texo==1:
        with open(input_file,'w') as inf:
            ix=inf.write(Texography)
        Texo=0
    with open(input_file) as inf:
        ix = inf.read()
        with open(output_file, 'a') as opf:
            line = '------->>'+input_file+'<<-------'
            opf.write('\n'+line.center(80, '-')+'\n')
            opf.write(ix)


def FileThrow(directry):
    """List All Files In The Given Directry, And Directry After That"""
    lis = os.listdir(directry)
    for i in lis:
        if os.path.isdir(i):
            FileThrow('./'+i+'/')
        else:
            arr.append(directry+i)
    return arr

di = input('Tell The Directry From Where you Want to Start, \n Or \
Should I Start \n \
From Here '+os.getcwd()+' "Y" for Current Working Directry:> ').lower()
if di == 'y':
    di = './'
arr = []
FT = FileThrow(di)
for i in FT:
    try:
        ReadWrite(i)
    except:
        pass
print("I Think Its Beautifully Done Check Em' Out")
