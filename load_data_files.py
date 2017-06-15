# -*- coding: utf-8 -*-
"""

@author: Sathvik
"""

#Import text files from the europarl text data
# Simple procedure: Replace 'pl' with all the language names (21) and there you go all the text files
#into another folder NLP_TEXT_SMALL picking it randomly.
import glob as g
import codecs
import random
data_test=[]
get_dir=g.glob('C:/Users/Sathvik/Desktop/DS/europarl/txt/pl/*')
b=list(get_dir)
random.shuffle(b)
a=2200
for k in range(0,a):
    with codecs.open(get_dir[k],encoding="iso-8859-1") as f:
        data_test.append(f.read())
        

with codecs.open("C:/Users/Sathvik/Desktop/DS/NLP_TEXT_SMALL/pl.txt", "w",encoding=" iso-8859-1") as output:
    output.write( ','.join(data_test) )
    
#TO IMPORT ALL THE FILES, LARGER SET
    
import glob as g
import codecs
data=[]
get_dir=g.glob('C:/Users/Sathvik/Desktop/DS/europarl/txt/*')

a=len(get_dir)
for k in range(0,a):
    with codecs.open(get_dir[k],encoding=" iso-8859-1") as f:
        data.append(f.read())
        
with codecs.open("C:/Users/Sathvik/Desktop/DS/NLP_TEXT/pl.txt", "w",encoding=" iso-8859-1") as output:
    output.write( ','.join(data) )