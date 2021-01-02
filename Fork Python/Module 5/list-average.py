"""
You are given a list of integers. You need to return the average of the list, except ignore the maximum and the minimum value. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division (or floor to int) to produce the final average. You may assume that the array is length 3 or more.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing the elements of the list separated by spaces.

Output Format:
For each testcase, in a new line, print the average as directed.

Your Task:
This is a function problem. You don't need to take input. Complete the function avg and return the average.

Constraints:
1 <= T <= 100

Examples:
Input:
2
1 2 3 4 100
1 1 5 5 10 7 8
Output:
3
5
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3


def avg(mylist):
    ##Your Code Here
    if len(mylist)>2:
        return (sum(mylist)-max(mylist)-min(mylist))//(len(mylist)-2)
    else:
        return 0


#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        
        mylist= [int(x) for x in input().split()]
        print(avg(mylist))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends