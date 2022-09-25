#Replacing upper/lower case letters with lower/upper case letters in a string:-

'''
Sample Input :
HackerRank.com presents "Pythonist 2".

Sample Output :
hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''
#Code:-

def swap_case(s):
    list1=[]                        #initializing empty list for storing converted characters
    for i in s:                     #looping to check each characters in a string 
        if i.isupper()==True:       #checking whether the letter is Uppercase letter or not
            temp1=i.lower()         #changing it to LowerCase
            list1.append(temp1)
        elif i.islower()==True:     #checking whether the letter is Lowercase letter or not
            temp2=i.upper()         #changing it to uppercase
            list1.append(temp2)
        else:                       #if it is other than letters...
            i1=i                    #keep it as it is 
            list1.append(i1)
    s=''.join(list1)                #joining all characters into a single string
    return s                        #returning that string
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
