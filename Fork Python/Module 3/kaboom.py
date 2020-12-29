"""
You are given a string str. You need to print True if the str ends with boom else print False.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a string str.

Output Format:
For each testcase, in a new line, print True or False as directed.

Your Task:
This is a function problem. Do not take any input. Just complete the function boom and return True or False.

Constraints:
1 <= T <= 100

Example:
Input:
1
Kaboom

Output:
True
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def boom(str):
    ##Your code here
    return str.endswith("boom")


#{ 
#Driver Code Starts.





def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(boom(str))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends