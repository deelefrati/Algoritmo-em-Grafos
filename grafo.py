import sys
import unittest

class Grafh(object):
	dicio = {}
	checado = {}
	distancia ={}
	pred = {} 
	def updateVert(self, key, valor):
		self.dicio.update({key: valor})
		self.checado.update({key:"white"})
		self.distancia.update({key:100000000})
		self.pred.update({key:None})
		for i in valor:
			if i not in self.dicio:
				self.dicio.update({i:[]})
				self.checado.update({key:"white"})
				self.distancia.update({key:100000000})
				self.pred.update({key:None})
	def removeVert(self, key):
		entrou = False
		for i in self.dicio:
			if i == key:
				del self.dicio[i]
				entrou = True	
				break 
		for i in self.dicio:
			if key in self.dicio[i]:		
				self.dicio[i].remove(key)
		if not entrou:
			print("Esse vértice não pertence ao grafo")

	def verificarAresta(self, v1, v2):
		if v2 in self.dicio[v1]:
			print("Existe a ligação")
		else:
			print("Não existe a ligação")

	def verticeAdj(self, v1):
		print(self.dicio[v1])	

	def verticeIncidente(self, v1):
		for i in self.dicio:
			if v1 in self.dicio[i]:
				print(i)		

	def grauVertice(self, v1):
		count = 0	
		for i in self.dicio:
			if v1 in self.dicio[i]:
				count+=1
		return(len(self.dicio[v1]), count)

	def complemento(self):
		comp = {}
		for i in self.dicio:
			vetor = self.dicio.keys()
			vetor = list(vetor)
			vetor.remove(i)
			for elemento in self.dicio[i]:
				if elemento in vetor:
					vetor.remove(elemento)
			comp.update({i:vetor})
		return(comp)			

	def transposto(self):
		trans = {}
		for i in self.dicio:
			vetor = []
			for j in self.dicio:
				if i in self.dicio[j]:
					vetor.append(j)
			trans.update({i:vetor})		
		return (trans)

	def BFS(self,raiz):
		if raiz not in self.dicio:
			print("Esse vertice não faz parte do grafo!")
		else:
			self.checado.update({raiz:"gray"})
			self.distancia.update({raiz:0})
			fila = []
			fila.append(raiz)
			while fila != []:
				u = fila.pop(0)
				for elemento in self.dicio[u]:
					if self.checado[elemento] == "white":
						self.checado.update({elemento:"gray"})
						self.distancia.update({elemento:self.distancia[u] + 1})
						self.pred.update({elemento:u})
						fila.append(elemento)
				self.checado.update({u:"black"})					
		print(self.distancia)

	def printarBFS(self,elemento,lista):
		if self.pred[elemento] == None:
			lista.append(elemento)
		else:
			lista.append(elemento)
			self.printarBFS(self.pred[elemento],lista)
		return (lista)		
		


		
				


def main():
	Grafo = Grafh()
	opcao = -1
	while (opcao != 0):
		print("1- Inserir vertice\n2- Remover vértice\n3- Verificar aresta\n4- Printar vertices adjascentes\n5- Printar vertice incidente\n6- Verificar grau\n7- Complemento\n8- Trasposto\n9- BCD")
		opcao = int(input("Digite a opção: "))
		lista = []
		if opcao == 1:
			key = input("Digite o nome do vertice: ")
			n = int(input("Digte a quatidade de vértices ligados a ele: "))
			valor = [input("Digite o nome do vertice ligado ao vertice: ") for i in range(n)]
			Grafo.updateVert(key, valor)
			print(Grafo.dicio)
		elif opcao == 2:
			key = input("Digite o nome do vertice: ")
			Grafo.removeVert(key)
			print(Grafo.dicio)
		elif opcao == 3:
			v1 = input("Digite o nome do primeiro vertice: ")
			v2 = input("Digite o nome do segundo vertice: ")
			Grafo.verificarAresta(v1, v2)
		elif opcao == 4:
			v1 = input("Digite o nome do vertice:")
			Grafo.verticeAdj(v1)
		elif opcao == 5:
			v1 = input("Digite o nome do vertice:")
			Grafo.verticeIncidente(v1)
		elif opcao == 6:
			v1 = input("Digite o nome do vertice:")
			x = Grafo.grauVertice(v1)
			print("O grau de saida ", v1 ,"é: ", x[0])
			print("O grau de entrada", v1 ,"é: ", x[1])
		elif opcao == 7:
			print("Complemento: ",Grafo.complemento())

		elif opcao == 8:
			print("O grafo transposto é: ",Grafo.transposto())
		elif opcao == 9:
			elemento = input("Digite um vertice: ")
			Grafo.BFS(elemento)
			elemento2 = input("Digite um vertice que deseja consultar: ")
			print("\n")
			print(Grafo.printarBFS(elemento2,lista))	
		print("\n")	


if __name__ == '__main__':
	main()