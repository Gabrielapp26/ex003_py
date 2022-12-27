#Desafio 02
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
print("Digite um número para saber o seu dobro, triplo e a raiz quadrada")
n = int(input("Digite um número: "))
d = n*2
t = n*3
rq = n**(1/2)
print("{} \nO dobro é {} \nO triplo é {} \nA raiz quadrada é {:.2f}".format(n,d,t,rq)) 
#\n para digitar na linha de baixo 
#{:.nf} é o tanto de números que vc quer que apareça