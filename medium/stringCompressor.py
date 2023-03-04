"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Time complexity: O(n)
Space complexity: O(n)
"""

def compress(self, chars: List[str]) -> int:

    stack, i = [[chars[0], 1]], 1

    while i < len(chars):

        if chars[i] == stack[-1][0]:
            stack[-1][1] += 1

        else:
            stack.append([chars[i], 1])

        i += 1

    string = ''
    for x, y in stack:
        if y == 1:
            string += x

        else:
            string += f'{x}{y}'


    chars[:] = list(string)

    return len(chars)
