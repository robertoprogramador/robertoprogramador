#!/bin/python,
#testando python no servidor bem-vindo com script simples
visitante=input("digite seu nome:")
idade=input("Digite sua idade:")
idade=float(idade)

if idade >=18:
    print ("Você está aprovado para dirigir.")
else:
    print ("Você não está aprovado para dirigir.")