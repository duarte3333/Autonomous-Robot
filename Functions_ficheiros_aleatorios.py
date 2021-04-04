# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:36:56 2020

@author: Duarte Morais 100163 Joana Caramelo 100198
"""


from graphics import*
from Classe_Ilhas import*
from Classe_Cais import*
from Classe_Impurezas import *
from Classe_Roboat import*
from time import *
from random import randrange

    
def impurezas_aleatorias(lista_pontos_ilhas,window):
    
        """Esta função gera aleatóriamente impurezas"""
    
        lista_pontos_detritos = []
        
        a=0
        while a < 5:
            
            #Ilaboração aleatória da abcissa e da ordenada de cada impureza
          
            pb3 = randrange(5,95)
            pb4= randrange(5, 95)
            
            ponto_d = Point(pb3,pb4)
            n=0
            while n < len(lista_pontos_ilhas) :
                
                #Restrição para que não sejam criadas impurezas por cima de ilhas
                if ((lista_pontos_ilhas[n].getX() - ponto_d.getX())**2 + ((lista_pontos_ilhas[n].getY()) - (ponto_d.getY()))**2) <= 81:
                    break
                
                #Restrição para que não sejam criadas impurezas no cais e na zona de partida do Roboat
                elif 0<ponto_d.getX()<20 and  0<ponto_d.getY()<20:
                    break
                
                else:
                    n= n+1
                
            else:
                lista_pontos_detritos.append(ponto_d)
                a=a+1
    
                
        return lista_pontos_detritos

def ilhas_aleatorias_pontos():
    
        """Esta função permite gerar os centros das ilhas aleatoriamente"""
        
        lista_opçao_ilhas = ["Triangulo","Circulo","Circulo","Quadrado","Cruz"]
        c =[]
        
        #Ilaboração aleatória da abcissa e da ordenada do centro de cada ilha
            
        a=0
        while a < 5:
        
            pb5 = randrange(20,80)
            pb6= randrange(20, 80)
            ponto_d = Point(pb5,pb6)
            n=0

            #Restrição para que não sejam criadas ilhas no cais e na zona de partida do Roboat
            if not (0<ponto_d.getX()<35 and 0<ponto_d.getY()<35):
                    
                b=0
                for i in c:
                      
                    #Restrição para que não sejam criadas ilhas sobrepostas
                    if ((ponto_d.getX() - i.getX())**2 + ((ponto_d.getY()) - i.getY())**2) >= 400:
                        b=b+1

                if b == len(c):                
                    c.append(ponto_d)
                    
                    a=a+1
      
        return c  

def ilhas_aleatorias_pontos_mode4():
    
        """Esta função permite gerar os centros das ilhas aleatoriamente, sabendo que não se podem gerar ilhas
        nos locais das impurezas definidas pelo ficheiro "Documento_leitura_impurezas.txt" """
        
        lista_opçao_ilhas = ["Triangulo","Circulo","Circulo","Quadrado","Cruz"]
        a1 = leitura_impurezas("Documento_leitura_impurezas.txt")   
        c = []
        
        a=0
        while a < 5:
        
            pb5 = randrange(5,95)
            pb6= randrange(5,95)
            ponto_d = Point(pb5,pb6)
            n=0

            #Restrição para que não sejam criadas ilhas no cais e na zona de partida do Roboat
            if not (0<ponto_d.getX()<35 and 0<ponto_d.getY()<35):
                    
                b=0
                d=0
                for i in c:
                    
                    #Restrição para que não sejam criadas ilhas sobrepostas às impurezas
                    
                    if ((ponto_d.getX() - i.getX())**2 + ((ponto_d.getY()) - i.getY())**2) >= 400:
                        b=b+1
                for i in a1:
                    
                    #Restrição para que não sejam criadas ilhas sobrepostas
                    if ((ponto_d.getX() - i.getX())**2 + ((ponto_d.getY()) - i.getY())**2) >= 400:
                        d=d+1
                        
                if b == len(c) and d == len(a1):                
                    c.append(ponto_d)
                    
                    a=a+1
        
        return c 
       
def ilhas_aleatorias_formato():

        """Esta função gera aleatóriamente o formato da ilhas"""    

        a = [Point(25,75),Point(25,25),Point(75,75),Point(75,25),Point(50,50)] 
        lista_opçao_ilhas = ["Triangulo","Circulo","Circulo","Quadrado","Cruz"]
   
        b = [] 
        
        for i in range(5):
            
            possibilidade2 = randrange(0,5)
            z2 = lista_opçao_ilhas[int(possibilidade2)]
        
            b.append(z2)
    
     
        return b
                        
def leitura (Documento_leitura):

    """Esta função faz a leitura do tamanho da janela gráfica através de um ficheiro txt"""
        
    #Leitura do ficheiro
    ficheiro_ilhas = open(Documento_leitura, "r")
    
    dadoslidos = ficheiro_ilhas.read().replace('\n', '.').replace(' ', '.')
    dadosdivididos = dadoslidos.split('.')
   
    aux = 0
    
    #Extração do tamanho da janela escrito no ficheiro 
    
    for elemento in dadosdivididos:
        
        if elemento == 'sugerida:':
            pixx = int(dadosdivididos[aux + 1])
            pixy = int(dadosdivididos[aux + 2])
    
    
        aux=aux+1
        
    
    return pixx, pixy

    
def leitura_opçao_centros(Documento_leitura): 
    
    """Esta função faz a leitura dos centros das ilhas e do seu formato através de um ficheiro txt"""
    
    #Leitura do ficheiro
    ficheiro_ilhas = open(Documento_leitura, "r")
    
    dadoslidos = ficheiro_ilhas.read().replace('\n', '.').replace(' ', '.')
    dadosdivididos = dadoslidos.split('.')

    aux = 0
    
    for elemento in dadosdivididos:
        
            if elemento == 'ilhas:':
                #Opçao 1
                #Extração do centro de uma das cinco ilhas e do seu formato geometrico 
                opt1 = str(dadosdivididos[aux + 2])
                var1 = str(dadosdivididos[aux + 3]).split('t(')[1]
                el1_opt1 = var1.split(',')[0]
                el2_opt1 = var1.split(',')[1]
                el3_opt1 = el2_opt1.split(')')[0]
          
                #Opçao 2
                #Extração do centro de uma ilha e do seu formato geometrico
                opt2 = str(dadosdivididos[aux + 4])
                var2 = str(dadosdivididos[aux + 5]).split('t(')[1]
                el1_opt2 = var2.split(',')[0]
                el2_opt2 = var2.split(',')[1]
                el3_opt2 = el2_opt2.split(')')[0]
          
                #Opçao 3
                #Extração do centro de uma ilha e do seu formato geometrico
                opt3 = str(dadosdivididos[aux + 6])
                var3 = str(dadosdivididos[aux + 7]).split('t(')[1]
                el1_opt3 = var3.split(',')[0]
                el2_opt3 = var3.split(',')[1]
                el3_opt3 = el2_opt3.split(')')[0]
            
                #Opçao 4
                #Extração do centro de uma ilha e do seu formato geometrico
                opt4 = str(dadosdivididos[aux + 8])
                var4 = str(dadosdivididos[aux + 9]).split('t(')[1]
                el1_opt4 = var4.split(',')[0]
                el2_opt4 = var4.split(',')[1]
                el3_opt4 = el2_opt4.split(')')[0]
      
                #Opçao 5
                #Extração do centro de uma ilha e do seu formato geometrico
                opt5 = str(dadosdivididos[aux + 10])
                var5 = str(dadosdivididos[aux + 11]).split('t(')[1]
                el1_opt5 = var5.split(',')[0]
                el2_opt5 = var5.split(',')[1]
                el3_opt5 = el2_opt5.split(')')[0]
            
            aux=aux+1
            
    #Ilaboração de uma lista com os centros de cada ilha 
    lista_pt = []   
    lista_pt = [Point(el1_opt1,el3_opt1),Point(el1_opt2,el3_opt2),Point(el1_opt3,el3_opt3),Point(el1_opt4,el3_opt4),Point(el1_opt5,el3_opt5)]
    
    #Ilaboração de uma lista com os formatos de cada ilha
    lista_formas = []
    lista_formas = [opt1,opt2,opt3,opt4,opt5]
    
    return lista_pt , lista_formas

 
def leitura_cais(Documento_leitura): 
    
    """Esta função faz a leitura dos pontos do cais através de um ficheiro txt"""
    
    #Leitura do ficheiro
    ficheiro_ilhas = open(Documento_leitura, "r")
    
    dadoslidos = ficheiro_ilhas.read().replace('\n', '.').replace(' ', '.')
    dadosdivididos = dadoslidos.split('.')
        
    aux = 0

    for elemento in dadosdivididos:
        
            if elemento == 'Cais1':
                
                #Primeiro ponto do primeiro cais
                cais1_pt1 = str(dadosdivididos[aux + 2]).split('int(')[1]
                a2 = cais1_pt1.split(',')[0]
                a3 = cais1_pt1.split(',')[1]
                a4 = a3.split(')')[0]
                
                #Segundo ponto do primeiro cais
                cais1_pt2 = str(dadosdivididos[aux + 3]).split('int(')[1]
                b2 = cais1_pt2.split(',')[0]
                b3 = cais1_pt2.split(',')[1]
                b4 = b3.split('))')[0]
                 
                #Primeiro ponto do segundo cais
                cais2_pt1 = str(dadosdivididos[aux + 6]).split('int(')[1]
                c2 = cais2_pt1.split(',')[0]
                c3 = cais2_pt1.split(',')[1]
                c4 = c3.split(')')[0]
   
                #Segundo ponto do segundo cais
                cais2_pt2 = str(dadosdivididos[aux + 7]).split('int(')[1]
                d2 = cais2_pt2.split(',')[0]
                d3 = cais2_pt2.split(',')[1]
                d4 = d3.split('))')[0]
 
            aux=aux+1  
              
    lista_cais = []
    lista_cais = [Point(a2,a4),Point(b2,b4),Point(c2,c4),Point(d2,d4)]
    return lista_cais
 
def leitura_impurezas (Documento_leitura):
    
    """Esta função faz a leitura das impurezas através de um ficheiro txt"""

    #Leitura do ficheiro
    ficheiro_ilhas = open(Documento_leitura, "r")
    
    dadoslidos = ficheiro_ilhas.read().replace('\n', ',').replace(' ', ',')
    dadosdivididos = dadoslidos.split(',')
    
    aux = 0
    
    #Extração das coordenadas das impurezas a partir do ficheiro 
    
    for elemento in dadosdivididos:
        
        if elemento == 'impurezas:':
            i1 = float(dadosdivididos[aux + 2])
            i2 = float(dadosdivididos[aux + 3])
            
            i3 = float(dadosdivididos[aux + 4])
            i4 = float(dadosdivididos[aux + 5])
            
            i5 = float(dadosdivididos[aux + 6])
            i6 = float(dadosdivididos[aux + 7])
            
            i7 = float(dadosdivididos[aux + 8])
            i8 = float(dadosdivididos[aux + 9])
            
            i9 = float(dadosdivididos[aux + 10])
            i10 = float(dadosdivididos[aux + 11])
            
        aux=aux+1
    
    imp = []
    imp = [Point(i1,i2),Point(i3,i4),Point(i5,i6),Point(i7,i8),Point(i9,i10)]
    
    return imp
                


  
 