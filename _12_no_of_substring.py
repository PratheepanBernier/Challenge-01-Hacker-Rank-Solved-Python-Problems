#number of substring in a string ...

'''
Sample Input:
ABCDCDC
CDC

Sample Output:
2
'''
#code:-

def count_substring(string, sub_string):
    str_size = len(string)       
    sub_str_size = len(sub_string)     
    count1=0   
    
    for i in range(str_size-sub_str_size+1):
        if string[i:i+sub_str_size]==sub_string:
            count1=count1+1
    return count1
        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
