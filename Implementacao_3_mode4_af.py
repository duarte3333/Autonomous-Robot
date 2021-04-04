# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 04:36:30 2020

@author: Duarte Morais 100163 Joana Caramelo 100198
"""

from graphics import*
from Classe_Ilhas import*
from Classe_Cais import*
from Classe_Impurezas import *
from Classe_Roboat import*
from time import *
from Functions_ficheiros_aleatorios import*
from Aux_Functions import *

def RunBotao_third_mode4(tempo_limpeza, cor_proa, cor_roboat):
    
        """Esta função irá correr a terceira implementação, de modo que as ilhas serão geradas aleatóriamente e as impurezas sejam geradas a partir de um ficheiro txt"""
        
        #Ilaboração da janela gráfica
        
        window =  GraphWin("Piscina do Dudu e da Juju",800,800,autoflush=False)
        window.setCoords(0,0,100,100)
        window.setBackground("Darkturquoise") 
 
        #Com um clique as ilhas irão aparecer na plataforma gráfica
        #Ilaboração da lista com os centros das ilhas e da lista com os formatos das ilhas
        #A partir dessas duas listas a função lista_1 irá gerar as ilhas em ambiente gráfico
        
        window.getMouse()
        a1 = ilhas_aleatorias_pontos_mode4()
        b1 = ilhas_aleatorias_formato()
        islands_list = lista_1(window, a1 , b1)
        
        #Com um clique o cais irá aparecer na plataforma gráfica
        #Irá criar a partir da Classe Cais as diferentes partes do cais
       
        window.getMouse()

        Cais1 = Cais(Point(0,0),Point(15,5) ,'black','white', window)  
        Cais2 = Cais(Point(0,5),Point(5,15) ,'black','white', window) 
      
        #Criação do Roboat em ambiente gráfico a partir da classe Roboat     

        Roboat1 = Roboat_graph(3,Point(40,50), cor_roboat, cor_proa ,"black",5,window,islands_list) 
        
        #No ficheiro "Aux_Functions" e "Functions_ficheiros_aleatorios" é possível ver a descrição detalhada destas funçoes
        
        a = leitura_impurezas("Documento_leitura_impurezas.txt")   
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
        

