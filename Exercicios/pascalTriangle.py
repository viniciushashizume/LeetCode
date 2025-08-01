class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]] #lista de listas
        for i in range (1,numRows):
            linhaAnterior = pascal[-1] # [1]
            novaLinha = [1]  #[[1][1]]
            for j in range(len(linhaAnterior)-1): #penultimo termo
                #soma termo 1 com o proximo
                soma = linhaAnterior[j] + linhaAnterior[j+1] 
                novaLinha.append(soma)
            novaLinha.append(1)
            pascal.append(novaLinha) 
        return pascal
        