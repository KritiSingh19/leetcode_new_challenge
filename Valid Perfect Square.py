Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a=num**(0.5)
        b=a*10
        c=b%10
        if(c==0):
            return True
        else:
            return False
