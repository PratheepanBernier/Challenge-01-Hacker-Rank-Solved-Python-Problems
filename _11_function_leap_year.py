#return true if leap year . else false:-
'''
Sample Input :
1990

Sample Output :
False
'''

def is_leap(year):
    leap = False
    d=0
    
    #logic :-
    
    if (year % 400 == 0) and (year % 100 == 0):
        d=1
        return True
    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        d=1
        return True
    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return leap

year = int(input())
print(is_leap(year))