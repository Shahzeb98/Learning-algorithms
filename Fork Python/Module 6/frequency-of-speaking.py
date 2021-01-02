"""
Given a statement containing some words (lowercase characters) which may have some repeating words. The task is to count the frequency of each word in the statement.

Input:
First line of input contains number of testcases T. For each testcase, the only line of input contains statement.

Output:
For each testcase, print the word with its frequency, if it is greater than 1. Also, the word appearing more than once should be printed once when it is encountered first in the statement.

Constraints:
1 <= T <= 100

User Task:
The task is to complete the function frequency_word() which should count the frequency an print them as required (also explained in same input).

Example:
Inuput:
2
i am a sports person
code while code

Output:
i
am
a
sports
person
code 2
while

Explanation:
Testcase 2: code word has frequency 2 and while has 1. So words are printed with their frequency (if greater than 1).
"""

#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

# Function to count frequency of words
def frequency_word(statement):
    
    # Your code here
    list_ = []
    for x in statement:
        if x not in list_:
            list_.append(x)
            value = statement.count(x)
            if value>1:
                print(x + " " + str(value))
            else:
                print(x)
 

#{ 
#Driver Code Starts.
# Driver Code
def main():
    # testcase input
    testcase = int(input())
    
    # loop to iterate through testcases
    while testcase > 0:
        statement = input().split()
        frequency_word(statement)
        
        testcase -= 1


if __name__ == '__main__':
    main()
#} Driver Code Ends