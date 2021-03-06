"""
You are given a mean m and an integer d. The mean m is the mean of 3 numbers a,b, and c. Find the mean of a, b, c and d.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains d and second line contains m.

Output Format:
For each testcase, in a new line, print the mean of a,b,c, and d.

Your Task:
This is a function problem. You do not need to take any input. Complete the function mean and return the new mean.

Constraints:
1 <= T <= 100
1 <= d, m <= 108

Example:
Input:
1
5
1
Output:
2

Explanation:
Testcase1: Mean of 3 numbers is 1. If we include 5 and find the new mean, it will be 2.
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def mean(d,m):
    ##Your code here
    return int((3*m + d)/4)


#{ 
#Driver Code Starts.


    

    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        d=int(input()) ##taking d as input
        m=int(input()) ## taking mean of 3 numbers
        print(mean(d,m))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends
