"""
Given a non-negative number n, print True if n is within 2 of a multiple of 10,  else print false.  For example 22 is within 2 of a multiple of 10 (the multiple here is 20) and 23 is not within 2 of a multiple of 10 (it is within 3 of multiple 20).

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a number n.

Output Format:
For each testcase, in a new line, print True if conditions are met; else print False.

Your Task:
This is a function problem. Do not take any input. Just complete the function isNeighbor

Constraints:
1 <= T <= 100
3 <= n <= 1018

Example:
Input:
4
3
9
13
22
Output:
False
True
False
True
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def isNeighbor(num):
    ##Your code here
    return num%10<3 or num%10>7

#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        n=int(input())
        print(isNeighbor(n))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends