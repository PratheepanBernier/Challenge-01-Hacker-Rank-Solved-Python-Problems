#Inputing size and names and scores and inputing name of the person whose average mark you wish to display:

'''
Sample Input :
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output :
56.00
'''
#Code:-

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split(" ")
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=student_marks[query_name]
    temp=0
    for i in marks:
        temp=temp+i
    average=temp/3.00
    res = "{:.2f}".format(average)
    print(res)   
