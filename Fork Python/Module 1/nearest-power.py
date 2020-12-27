"""
You are given two numbers a and b. When a is raised to some power p, we get a number x. Now, you need to find what is the value of x that is closest to b.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains a and second line contains b.

Output Format:
For each testcase, in a new line, print the closest power.

Your Task:
This is a function problem. You do not need to take any input. Complete the function nearestPower and return the answer.

Constraints:
1 <= T <= 100
2 <= a <= 100
a <= b <= 108

Example:
Input:
1
2
4
Output:
4

Explanation:
Testcase1: 22=4 is closest to 4
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3
import math
    
def nearestPower(a,b):
    ##Your code here
    p = int(math.log(b,a))
    num1 = a**p
    num2 = a**(p+1)
    ##return the closest power
    if b-num1<num2-b:
        return num1
    else:
        return num2


#{ 
#Driver Code Starts.


import math

    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        print(nearestPower(a,b))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends
