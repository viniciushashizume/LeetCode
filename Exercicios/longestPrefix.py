class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        tamanhoLista = len(strs)
        maiorPrefixo = strs[0]
        for i in range (1,tamanhoLista): #começa da posicao 1 da lists
            while not strs[i].startswith(maiorPrefixo):
                maiorPrefixo = maiorPrefixo[:-1] #vai "cortando" ate começar com o prefixo
        return maiorPrefixo
            
