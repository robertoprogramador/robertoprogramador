#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TRADER DE ELITE 2021
#CONTROLANDO MEU DESEMPENHO NO TRADER E CONTAS A PAGAR


# In[2]:


#!/usr/bin/python


# In[4]:


#COLETANDO OS PARAMETROS PARA CONSULTA
print('bem vindo Roberto')
diainformado=input ('digite o dia do mes')
saldoinformado=input ('digite o saldo de hoje')


# In[5]:


dia=int(diainformado)
saldo=float(saldoinformado)


# In[6]:


while saldo>=200:
    print('Voce tem margem pra operar, vamos em frente!')
    break
else:
    print('Voce esta sem margem cuidado no trader agora 1x1 apenas')
    


# In[7]:


if saldo >=400 and saldo<=699 and dia>10:
    print('vamos em frente com 2 CONTRATOS')
elif saldo >=400 and saldo <=600:
    print ('podemos tentar 4 CONTRATOS, você ja pagou agua e luz')
elif saldo >=700:
    print('voce ja pagou o SENAC ACORDO!!!')
    print('bom pagar também a vivo e a claro')
elif dia >20:
    print('PROXIMOS PAGAMENTOS TERRENO_dia26 E MENTORIA_TRADE_dia01')
else:
    print("estamos na margem de operação controlada, boa sorte")


# In[8]:


#controle de desempenho e faixas trader bruto
#digite valor de trade todos os dias para dias nao uteis digite 0
#pra consultar o valor de um dia lembre-se:A INDEXAÇÃO EM PYTHON COMEÇA EM 0!!!


# In[9]:


#registro diario de traders para consulta
tradersaldo2=[106,164,0,166,0,0,6,-261,]
#registgro so de dias uteis para avaliar desempenho
traderuteis=[106,164,166,6]


# In[10]:


sum(tradersaldo2)


# In[11]:


#SALDO DO DIA 1 COMANDO: tradersaldo2[0]
#SALDO DO DIA 2 COMANDO: tradersaldo2[1], etc
tradersaldo2[0]


# In[12]:


x=int(input("digite o dia que quer consultartrade"))
print(x)
tradersaldo2[x-1]


# In[13]:


sum(tradersaldo2)


# In[14]:


if sum(tradersaldo2)>=500:
    print("Bem vindo a FAIXA ROXA Trader Elite")
elif sum(tradersaldo2)>=2000:
    print("Bem vindo a FAIXA MARROM Trader Elite")
else:
    print("Vamos que vamos subir faixa jovem trader")


# In[15]:


#nao estou aqui para ser perfeito, mas para ser lucrativo!!!
mediatrader=sum(traderuteis) / len(traderuteis)
print('a media DIÁRIA deste mês trader é:', mediatrader)
mensal=mediatrader*22


# In[16]:


print("E O SALARIO MES PROJETADO É:", mensal)


# In[17]:


def somatrader (tradersaldo2):
    return sum(tradersaldo2)
print("a soma dos traders deste mes é:", sum(tradersaldo2))


# In[ ]:





# In[ ]:




