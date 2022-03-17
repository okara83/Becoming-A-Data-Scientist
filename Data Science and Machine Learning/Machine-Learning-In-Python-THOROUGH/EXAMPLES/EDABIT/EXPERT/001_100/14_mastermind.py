"""
Mastermind
The classic game of Mastermind is played on a tray on which the Mastermind conceals a code and the Guesser has 10 tries to guess it. The code is a sequence of 4 (or 6, sometimes more) pegs of different colors. Each guess is a corresponding sequence of 4 (or more) pegs of different colors. A guess is "correct" when the color of every peg in the guess exactly matches the corresponding peg in the Mastermind's code.

After each guess by the Guesser, the Mastermind will give a score comprising black & white pegs, not arranged in any order:

Black peg == guess peg matches the color of a code peg in the same position.
White peg == guess peg matches the color of a code peg in another position.
Create a function that takes two strings, code and guess as arguments, and returns the score in a dictionary.

The code and guess are strings of numeric digits
The color of the pegs are represented by numeric digits
no "peg" may be double-scored
Examples
guess_score("1423", "5678") ➞ {"black": 0, "white": 0}

guess_score("1423", "2222") ➞ {"black": 1, "white": 0}

guess_score("1423", "1234") ➞ {"black": 1, "white": 3}

guess_score("1423", "2211") ➞ {"black": 0, "white": 2}
Notes
The code and guess sequences will have the same length.
The "pegs" consists of only digits from 0-9.
"""
def guess_score(code, guess):
    a = list(code)
    b = list(guess)
    
    d ={}
    c, e = [], []

    for i in range(len(a)):
        if a[i] == b[i]:
            print("i", "=",b[i])
            c.append(a[i])
        else:
            if a[i] in b:
                e.append(i)        
    
    d = {"black": len(c) ,"white": len(e) } 

    return (d)


#guess_score("1423", "5678") #➞ {"black": 0, "white": 0}
#guess_score("1423", "2222") #➞ {"black": 1, "white": 0}
#guess_score("1423", "1234") #➞ {"black": 1, "white": 3}
guess_score("1423", "2211") #➞ {"black": 0, "white": 2}
#guess_score("2928", "7722") # {"black": 1, "white": 1}
#guess_score("4845", "6446") # {"black": 1, "white": 1}