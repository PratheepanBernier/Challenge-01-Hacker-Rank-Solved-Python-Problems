#Get a string and split it and join it with '-':

'''
Sample Input:
this is a string  

Sample Output:
this-is-a-string
'''
#code:-

def split_and_join(line):
    a=line.split(" ")
    b="-".join(a)
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)