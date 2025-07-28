class Solution:
    def isPalindrome(self, x: int) -> bool:
        numero = str(x) #transforma em string
        numeroReverso = numero[::-1] #inverte a string
        if (numero == numeroReverso): 
            return True 
        else: 
            return False