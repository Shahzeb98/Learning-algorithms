"""
Given a list of positive integers (numbers may be repeated). The task is to print the numbers in sorted order. Numbers occuring more than once should be printed once.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains list elements.

Output:
For each testcase, print the elements(only once) in sorted order.

Constraints:
1 <= T <= 100
1 <= L[i] <= 106

User Task:
The task is to complete the function sorted_elements() which returns a list with elements in sorted order (each element should present once).

Example:
Input:
2
7 8 1 9 0 1
5 5 4 2 9 1

Output:
0 1 7 8 9
1 2 4 5 9

Example:
Testcase 1: Elements of the list printed in sorted order (each element printed only once).
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3
from collections import Counter

# Function to print elements in sorted order
def sorted_elements(numbers):
    
    # Your code here 
    # return the list which contains 
    # elements in sorted order
    dict_res = Counter(numbers)
    res = []
    for key in dict_res.keys():
        res.append(int(key))
    res.sort()
    return res


#{ 
#Driver Code Starts.
# Driver Code
def main():
    testcase = int(input())
    
    while testcase > 0:
        numbers = input().split()
        l = sorted_elements(numbers)
        
        for x in l:
            print (x, end = ' ')
        
        print ()
        testcase -= 1


if __name__ == '__main__':
    main()
#} Driver Code Ends