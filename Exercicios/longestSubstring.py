#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution: #a ideia é usar o conceito da janela deslizante
    def lengthOfLongestSubstring(self, s: str) -> int:
        maiorSubstring = 0
        for i in range(len(s)):
            #substring = s[i]
            substring = ''
            #proximoCaracter = s[i+1]
            for j in range(i,len(s)):
                char = s[j]
                if char in substring:
                    break
                else: 
                    substring += char
                '''if c == proximoCaracter:
                    janela = 0 #reseta a janela
                else:
                    janela += 1 #aumenta o tamanho da janela'''
            if len(substring) > maiorSubstring:
                maiorSubstring = len(substring)
        return maiorSubstring