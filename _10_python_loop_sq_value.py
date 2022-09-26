#size...non negative sq values of 0 to size-1 ...

'''
Sample Input :
5

Sample Output :
0
1
4
9
16

'''
n = int(input())
j=0
if n>=1 and n<=20 :
    for i in range(0,n,1):
        j=i*i
        print(j)
else:
    print("enter number between 1 to 20")
        
    
