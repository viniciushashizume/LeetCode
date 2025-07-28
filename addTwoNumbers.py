#https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        indice = 0
        noInicial = ListNode(0) #nó "cabeça"
        noAtual = noInicial
        while l1 is not None or l2 is not None or indice!=0:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            soma = val1 + val2 + indice
            elemento = soma%10 
            indice = soma//10 #indice resolve o problema da soma exceder 9
            novoNo = ListNode(elemento)
            noAtual.next = novoNo
            noAtual = noAtual.next #avançando o ponteiro do no saida
            #avançando as listas para evitar laço infinito
            if l1: l1 = l1.next 
            if l2: l2 = l2.next
        return noInicial.next        