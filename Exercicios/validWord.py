class Solution:
    def isValid(self, word: str) -> bool:
        tamanho = len(word)
        vogais = "aeiouAEIOU"
        consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        digitos = "0123456789"
        charsPermitidos = vogais + consoantes + digitos #eliminar obrigatoriedade de digitos
        #palavraMinuscula = word.lower()
        if (tamanho >= 3 and 
        any (char in vogais for char in word) and 
        any (char in consoantes for char in word) and
        all (char in charsPermitidos for char in word)):
            return True
        else: 
            return False