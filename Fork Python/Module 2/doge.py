"""
You are given a string str of lowercase letters. You need to count the number of times the word doge appears in the string. Also, the g in doge can be replaced by any letter from a-z so dope is also valid.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a string str.

Output Format:
For each testcase, in a new line, print the count.

Your Task:
This is a function problem. Do not take any input. Just complete the function doge_count and return the count.

Constraints:
1 <= T <= 100

Example:
Input:
2
dog
dogedopedose
Output:
0
3
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def doge_count(str):
    count=0
    ##Your code here
    for i in range(len(str)-3):
        l = 0
        for j in range(4):
            if j == 2:
                l+=1
                continue
            
            if str[i+j] == "doge"[j]:
                l+=1
        if l == 4:
            count+=1
    
    return count


#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(doge_count(str))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends