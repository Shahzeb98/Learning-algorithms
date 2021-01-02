"""
Given a python list of integers, you need to print True if 4 contains another 4 next to it in the list. If such thing doesn't occur then print False.

Input Format:
The first line of input contains T denothing the number of testcases. T testcases follow. Each testcase contains one line of input containing the contents of the list separated by spaces.

Output Format:
Fo each testcase, in a new line, print True or False.

Your Task:
This is a function problem, you don't need to take any input. Complete the function has44 and return True if conditions are met; else return False.

Constraints:
1 <= T <= 100

Examples:
Input:
2
5 4 3 2 1
1 2 3 4 4
Output:
False
True
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3


def has44(mylist):
    ##Your code here
    for i in range(len(mylist)-1):
        if mylist[i]==4 and mylist[i+1]==4:
            return True
    return False

#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        
        mylist= [int(x) for x in input().split()]
        print(has44(mylist))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends