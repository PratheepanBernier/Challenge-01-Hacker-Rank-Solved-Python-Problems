#nested list program:- SIZE...NAME..MARK.. STUDENTS WITH SECOND LOWEST MARK IN ALPHABETICAL ORDER

'''
Sample Input :
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output :
Berry
Harry

'''
#code:-

if __name__ == '__main__':
    scores=[]
    names=[]
    for j in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name,score])
    
    score_1 =sorted(set([i[1] for i in scores]))
    score_2 =score_1[1]
    names=sorted([i[0] for i in scores if i[1]==score_2])
    for name in names:
        print(name)
    