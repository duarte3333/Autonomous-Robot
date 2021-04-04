# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:50:39 2020

@author:  Duarte Morais 100163 Joana Caramelo 100198
"""

from graphics import*
from Classe_Ilhas import*
from Classe_Cais import*
from Classe_Impurezas import *
from Classe_Roboat import*
from time import *
from Functions_ficheiros_aleatorios import*



def lista_pontos_det(lista_pontos_ilhas,window):
    
        """Esta função serve para escolher através de um clique de rato, o lugar das impurezas em ambiente gráfico. Caso o utilizador tente colocar uma impureza por cima de uma ilha
        esta função irá ignorar esse clique, de modo que o utlizador terá de tentar novamente colocar a respetiva impureza """
    
        lista_pontos_detritos = []
        
        a=0
        while a < 5:
            ponto_d = window.getMouse()
            n=0
            while n < len(lista_pontos_ilhas) :
                
                #Restrição para que não sejam criadas impurezas por cima de ilhas
                if ((lista_pontos_ilhas[n].getX() - ponto_d.getX())**2 + ((lista_pontos_ilhas[n].getY()) - (ponto_d.getY()))**2) <= 81:
                    break
                
                #Restrição para que não sejam criadas impurezas no cais e na zona de partida do Roboat
                elif 0<ponto_d.getX()<15 and  0<ponto_d.getY()<15:
                    break
                
                #Restrição para que o Roboat não saia da janela gráfica 
                elif not 5<ponto_d.getX()<95 and 5<ponto_d.getY()<95:
                    break
                
                else:
                    n= n+1
                
            else:
                lista_pontos_detritos.append(ponto_d)
                a=a+1
                
        return lista_pontos_detritos
    
def lista_pontos_det_imp1(lista_pontos_ilhas,window):
    
        """Esta função serve para escolher através de um clique de rato, o lugar de uma impureza em ambiente gráfico. Caso o utilizador tente colocar a impureza por cima de uma ilha
        esta função irá ignorar esse clique, de modo que o utlizador terá de tentar novamente colocar a respetiva impureza. Esta função é parecida à "lista_pontos_det" 
        ,no entanto, existe uma pequena diferença pois esta função apenas permite que seja criada uma impureza"""    
    
        lista_pontos_detritos = []
        
        a=0
        while a < 1:
            ponto_d = window.getMouse()
            n=0
            while n < len(lista_pontos_ilhas) :
                
                #Restrição para que não sejam criadas impurezas por cima de ilhas
                if ((lista_pontos_ilhas[n].getX() - ponto_d.getX())**2 + ((lista_pontos_ilhas[n].getY()) - (ponto_d.getY()))**2) <= 81:
                    break
                
                #Restrição para que não sejam criadas impurezas no cais e na zona de partida do Roboat
                elif 0<ponto_d.getX()<15 and  0<ponto_d.getY()<15:
                    break
                
                #Restrição para que o Roboat não saia da janela gráfica 
                elif not 5<ponto_d.getX()<95 and 5<ponto_d.getY()<95:
                    break
                
                else:
                    n= n+1
                
            else:
                lista_pontos_detritos.append(ponto_d)
                a=a+1
                
        return lista_pontos_detritos

    
def lista_pontos_det_imp2(lista_pontos_ilhas,window,nImpurezas):
    
        """Esta função serve para escolher através de um clique de rato, o lugar das impurezas em ambiente gráfico. Caso o utilizador tente
        colocar uma impureza por cima de uma ilha esta função irá ignorar esse clique, de modo que o utlizador terá de tentar novamente 
        colocar a respetiva impureza. Além disso, esta função permite escolher o número de impurezas que serão geradas na plataforma gráfica"""    
    
        lista_pontos_detritos = []
        
        a=0
        while a < nImpurezas:
            ponto_d = window.getMouse()
            n=0
            while n < len(lista_pontos_ilhas):
                
                #Restrição para que não sejam criadas impurezas por cima de ilhas
                if ((lista_pontos_ilhas[n].getX() - ponto_d.getX())**2 + ((lista_pontos_ilhas[n].getY()) - (ponto_d.getY()))**2) <= 81:
                    break
                
                #Restrição para que não sejam criadas impurezas no cais e na zona de partida do Roboat
                elif 0<ponto_d.getX()<15 and  0<ponto_d.getY()<15:
                    break
                
                #Restrição para que o Roboat não saia da janela gráfica 
                elif not 5<ponto_d.getX()<95 and 5<ponto_d.getY()<95:
                    break
                
                else:
                    n= n+1
                
            else:
                lista_pontos_detritos.append(ponto_d)
                a=a+1
                
        return lista_pontos_detritos
    

def lista_temporaria(Roboat1,lista_pontos_detritos):
        
        """Esta função elabora uma lista temporária com pares ordenadados dos centros das impurezas e as suas distâncias em relação à posição inicial do Roboat. Após isso,
        a função ordena essa lista temporária de maneira a que os pontos fiquem ordenados de forma crescente pela distância que têm em relação ao ponto inicial do Roboat"""
        
        lista_pontos_temporaria = []
        for i in lista_pontos_detritos:
                dist =  ((i.getX() - Roboat1.getX())**2 + (i.getY() - Roboat1.getY())**2)**1/2
                lista_pontos_temporaria.append(tuple([i,dist]))
                
                lista_pontos_temporaria.sort(reverse = False, key=lambda x : x[1])
        
        return lista_pontos_temporaria

def lista_final(lista_pontos_temporaria):
    
        """Esta função elimina as distâncias da lista temporária, de modo a que se obtenha uma lista apenas com os centros das impurezas ordenados de forma crescente"""
        lista_final= []
        
        for i in range(len(lista_pontos_temporaria)):
                    
                    x = list(lista_pontos_temporaria[i])
                    lista_final.append(x[0])
                    
        return lista_final
                    

def lista_1(win,lista_pontos1_ilhas, lista_opçao1_ilhas):
        
         """Esta função gera todas as ilhas em ambiente gráfico a partir de uma lista com os centros das ilhas e de outra lista com os seus formatos geométricos"""
         
         lista_ilhas = []
    
         for c in range(len(lista_pontos1_ilhas)):
            
            z = lista_pontos1_ilhas[c]
            escolha = lista_opçao1_ilhas[c]
            i = Ilha(z ,'white','black', win, escolha)
            lista_ilhas.append(i)
            
         
         return lista_ilhas


                    