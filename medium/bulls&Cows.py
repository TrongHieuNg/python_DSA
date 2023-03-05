"""
You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
"""
from collections import defaultdict

def getHint(self, secret: str, guess: str) -> str:
    def letterCount(s):
        dct = defaultdict(list)
        for i in range(len(s)):
            dct[s[i]].append(i)
        return dct

    bulls = cows = 0
    dctSecret, dctGuess = letterCount(secret), letterCount(guess)
    for key in dctSecret.keys():
        if dctGuess.get(key):
            x = set(dctGuess[key]) & set(dctSecret[key])
            bulls += len(x)
            cows += min(len(dctGuess[key]), len(dctSecret[key])) - len(x)
    return f'{bulls}A{cows}B'
