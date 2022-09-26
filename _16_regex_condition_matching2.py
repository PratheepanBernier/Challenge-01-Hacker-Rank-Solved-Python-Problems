#Matching specific pattern:
'''
You have a test string S.
Your task is to write a regex that will match  with following conditions:

S must be of length: 6
First character: 1, 2 or 3
Second character: 1, 2 or 0
Third character: x, s or 0
Fourth character: 3, 0 , A or a
Fifth character: x, s or u
Sixth character: . or ,
'''
'''
Sample input:
1203x.
sample output:
true
'''
#code:-

Regex_Pattern = r'^[1,2,3]{1}[1,2,0]{1}[x,s,0]{1}[3,0,A,a]{1}[x,s,u]{1}[\.,]{1}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())