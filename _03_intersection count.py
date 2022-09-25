#Getting sizes and inputs for it. And printing the count of intersections:- 
'''
Sample input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample output:
5
'''

#code:-

size1=int(input())
values1 = [int(num) for num in input().split(" ", size1-1)]
size2=int(input())
values2 = [int(num) for num in input().split(" ", size2-1)]
set1=set(values1)
set2=set(values2)
intersect_count=set1.intersection(set2)
print(len(intersect_count))
