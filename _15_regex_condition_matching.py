#writing pattern for specific condition:-
'''
Write a RegEx that will match a string satisfying the following conditions:

The string's length is >=5.
The first character must be a lowercase English alphabetic character.
The second character must be a positive digit. Note that we consider zero to be neither positive nor negative.
The third character must not be a lowercase English alphabetic character.
The fourth character must not be an uppercase English alphabetic character.
The fifth character must be an uppercase English alphabetic character.
'''
'''
Sample input:
h4CkR

Sample output:
true
'''

#code:-

Regex_Pattern = r'^([a-z]{1}[1-9]{1}[A-Z0-9"!@#$%^&*?,;:-_"]{1}[a-z0-9"!@#$%^&*?,;:-_"]{1}[A-Z]{1})'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())