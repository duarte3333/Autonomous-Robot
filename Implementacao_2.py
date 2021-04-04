# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 03:05:19 2020

@author: Duarte Morais 100163 Joana Caramelo 100198
"""

from graphics import*
from Classe_Ilhas import*
from Classe_Cais import*
from Classe_Impurezas import *
from Classe_Roboat import*
from time import *
from Aux_Functions import*

#Função que irá correr a segunda implementação
     
def RunBotao_second(tempo_limpeza, cor_proa, cor_roboat,nImpurezas):
        
        """Esta função irá correr a segunda implementação"""         
        
        #Ilaboração da plataforma gráfica
        
        window =  GraphWin("Piscina do Dudu e da Juju",800,800,autoflush=False)
        window.setCoords(0,0,100,100)
        window.setBackground("Darkturquoise") 
        
        #Com um clique as ilhas irão aparecer na plataforma gráfica
        #Ilaboração da lista com os centros das ilhas e da lista com os formatos das ilhas
        #A partir dessas duas listas a função lista_1 irá gerar as ilhas em ambiente gráfico

        window.getMouse()
 
        lista_pontos_ilhas = [Point(25,75),Point(25,25),Point(75,75),Point(75,25),Point(50,50)] 
        lista_opçao_ilhas = ["Triangulo","Circulo","Circulo","Quadrado","Cruz"] 
        
        islands_list = lista_1(window, lista_pontos_ilhas, lista_opçao_ilhas)
        
        #Com um clique o cais irá aparecer na plataforma gráfica
        #Irá criar a partir da Classe Cais as diferentes partes do cais
       
        window.getMouse()

        Cais1 = Cais(Point(0,0),Point(15,5) ,'black','white', window)  
        Cais2 = Cais(Point(0,5),Point(5,15) ,'black','white', window) 
      
        #Criação do Roboat em ambiente gráfico a partir da classe Roboat     
        
        Roboat1 = Roboat_graph(3,Point(40,50),cor_roboat,cor_proa,"black",5,window,islands_list)  
        
        #No ficheiro "Aux_Functions" é possível ver a descrição detalhada destas funçoes
        #Criação das Impurezas e da Ilhas em ambiente gráfico
        a = lista_pontos_det_imp2(lista_pontos_ilhas,window,nImpurezas)
        b = lista_temporaria(Roboat1,a)
        c = lista_final(b)
        
        #A partir da lista com os centros das impurezas ordenados, irá ser criada uma lista com Impurezas, feitas a partir da classe Impureza 
        
        lista_detritos = []
        
        for d in c:
                 
                pos1 = Point(d.getX(), d.getY())
                i1 = Impureza(pos1,'white','black', window)
                lista_detritos.append(i1) 
                  
        #O Roboat irá mover-se até ao centro de cada impureza e demorar um segundo a limpar cada impureza
        for x in lista_detritos:
            
                Roboat1.mover_roboat(x.getCentro())
                sleep(tempo_limpeza)
                
                x.undraw_imp()
           
        #o Roboat após limpar todas as impurezas irá regressar ao cais    
        Roboat1.mover_fim_graph()
        window.getMouse()
        window.close()
        
  

                    

                           
