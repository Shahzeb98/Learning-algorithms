"""
Given 2 integers, a and b, print their sum. However, if the sum is in the range (20-40) both inclusive, then just return 42.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input containing a and b.

Output Format:
For each testcase, in a new line, print output as directed.

Your Task:
This is a function problem. Do not take any input. Just complete the function aweSum

Constraints:
1 <= T <= 100
1 <= a, b <= 107

Example:
Input:
2
2
5
20
1
Output:
7
42
Explanation: There are two test cases. The first test case has output 7 (2 + 5).  Since this sum is not in the given specific range it is printed as it is.
In second case, the sum is 21 (20+1). Since this sum is in given range, 42 is printed.
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def aweSum(a, b):
    ##Your code here
    res = a+b
    if res>=20 and res<=40:
        return 42
    else:
        return res


#{ 
#Driver Code Starts.





def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        print(aweSum(a,b))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends