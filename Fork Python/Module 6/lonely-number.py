"""
Given a list of positive integers and a number K. In the list, every element occurs K times except one. The task is to find the element not present K times. If no such element exists then print -1.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains K and next line contains list elements.

Output:
For each testcase, print the only number which is not present K times in the list.

Constraints:
1 <= T <= 100
1 <= L[i] <= 106

User Task:
The task is to complete the function find_lonely() which should find and return the number not present K times.

Example:
Input:
1
3
1 8 7 2 1 7 1 8 7 8

Output:
2

Explanation:
Testcase 1: Every element in list is present 3 times except 8 which is present only once.
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3
from collections import Counter

# Function to print elements in sorted order
def find_lonely(numbers, k):
    # Your code here
    dict_r = Counter(numbers)
    
    for (key, value) in dict_r.items():
        if value is not k:
            print(key)
            return
    
    print(-1)


#{ 
#Driver Code Starts.
# Driver Code
def main():
    testcase = int(input())
    
    while testcase > 0:
        k = int(input())
        numbers = input().split()
        find_lonely(numbers, k)
        
        testcase -= 1


if __name__ == '__main__':
    main()
#} Driver Code Ends