#https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        dezenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        milhares = ["", "M", "MM", "MMM"]

        milhar = milhares[num // 1000]
        resto = num%1000
        centena = centenas[resto// 100]
        resto = num%100
        dezena = dezenas[resto// 10]
        unidade = unidades[resto % 10]

        resultado = milhar + centena + dezena + unidade
        
        return resultado