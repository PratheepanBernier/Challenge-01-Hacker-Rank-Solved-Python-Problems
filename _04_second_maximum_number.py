#Printing the second largest number in the input
'''
Sample Input :-
5
2 3 6 6 5

Sample Output :-
5
'''

#Code:-

size1=int(input())
values1 = set([int(num) for num in input().split(" ", size1-1)])
max1=max(values1)
values1.remove(max1)
max2=max(values1)
print(max2)