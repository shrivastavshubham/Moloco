'''Using one of the languages from {Go, Python, Java, C++},
implement a function/method that is given two strings and returns whether one can be obtained by the other after removing exactly one character.
Specifically, given two strings x and y, return true if and only if (1) x can be obtained by removing one character from y and/or (2) if y can be obtained by removing one character from x.
Assume that both strings only contain English alphabets and that neither is an empty string.
Note that x and y can be quite long (each containing millions of characters).

Implement this function/method and submit a link to your code (answer) below.
You can share via a link to your code using free websites like https://gist.github.com/ or ideone.com.'''

class Solution:
    def equalsWhenOneCharRemoved(self, x, y):
        if abs(len(x)-len(y))>1:return False
        i = j = 0
        dif_count = 0
        while i < len(x) and j < len(y):
            if x[i] != y[j]:
                dif_count += 1
                if dif_count>1:return False
                if len(x) > len(y):i += 1
                elif len(x) < len(y):j += 1
                else:i += 1;j += 1
            else:i += 1 ; j += 1
        if i < len(x) or j < len(y): dif_count += 1
        return True if dif_count == 1 else False