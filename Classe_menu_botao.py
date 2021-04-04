8# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:22:18 2020

@author: Duarte Morais 100163 Joana Caramelo 100198
"""

from graphics import *


class Botao:
    """#A classe Botao permite desenhar botões na janela gráfica.
    Estes são ativados ou desativados com os métodos activate() e deactivate()
    e permitem ao utilizador fazer diversas escolhas ao longo do programa."""
    
    
    def __init__(self, win, center, width, height, label, cor):      
        """Este método cria botões rectangulares."""
        self.cor = cor
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(str(self.cor))
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    
    def clicked(self,p):    
        """Este método reconhece quando se clica num botão"""
        return(self.active and 
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)
     
    
    def activate(self): 
        """Este método ativa o botão"""
        self.label.setFill('Black')
        self.rect.setWidth(2)
        self.rect.setFill(str(self.cor))
        self.active = True
        
          
    def deactivate(self):
        """Este método desativa o botão """
        self.label.setFill('black')
        self.rect.setWidth(1)
        self.rect.setFill('grey')
        self.active = False
     
    
    def grablabel(self):
        """Este método permite legendar o botão"""
        return self.label.getText()



class Menu1: 
    """O Menu1 permite ao utilizador escolher qual das três implementações pretende visualizar"""  
    
    def __init__(self, setSize):
        """Este método permite desenhar graficamente o menu 1"""
        self.win = win = GraphWin( "MENU", 800, 800)
        self.win.setCoords(0, 0, 100, 100)
        self.win.setBackground('antiquewhite')     
        self.setSize = setSize
        
        img = Image(Point(85,12.5), "Imagem1.png").draw(win)
               
        title = Text(Point(35,15), "Computação e programação 2020/2021")
        title.draw(self.win)
        title.setSize(self.setSize)
        
        name = Text(Point(30,10), "Duarte Morais e Joana Caramelo")
        name.draw(self.win)
        name.setSize(self.setSize)
        
        label = Text(Point(50,90),"MENU ROBOAT")
        label.draw(self.win)
        label.setSize(self.setSize)
        
        self.Botao_1 = Botao(self.win,Point(20,75),20,15,"Implementação 1", "salmon")
        self.Botao_1.activate()
            
        self.Botao_2 = Botao(self.win,Point(50,75),20,15,"Implementação 2", "salmon")
        self.Botao_2.activate()
            
        self.Botao_3 = Botao(self.win,Point(80,75),20,15,"Implementação 3", "salmon")
        self.Botao_3.activate()
            
        self.Botao_4 = Botao(self.win,Point(20,35),20,8,"Configurações", "dark turquoise")
        self.Botao_4.activate()
            
        self.Botao_5 = Botao(self.win,Point(80,35),20,8,"Quit", "dark turquoise")
        self.Botao_5.activate()
        
    
    
    def use(self):
        """Método que deteta que botão é clicado, retornando "Implementacao 1", ou "Implementacao 2"
        "Menu 3", "Configurações" ou "Quit"""
        a = True
        while a == True:
            point = self.win.getMouse()
            if self.Botao_1.clicked(point):
                a = False
                return "Implementacao 1"
            if self.Botao_2.clicked(point):
                a = False
                return "Implementacao 2"
            if self.Botao_3.clicked(point):
                a = False
                return "Menu 3"
            if self.Botao_4.clicked(point):
                a = False
                return "Configurações"
            if self.Botao_5.clicked(point):
                self.close()
                a = False
                return "Quit"
    
               
    def close(self):
        """Fechar janela """
        self.win.close()
          
        
        
class Menu2:
    """ Menu2 permite ao utilizador escolher o número de impurezas que deseja colocar no
    ambiente gráfico para que o Roboat as possa limpar"""    
    
    def __init__ (self, nImpurezas):
        """Método que desenha o Menu2 graficamente"""
               
        self.win = win = GraphWin("Impurezas", 200, 200)
        self.win.setCoords(0,0,100,100)
        self.win.setBackground('salmon')
        
        Text(Point(50,80), "Inserir número de impurezas").draw(win)
        Text(Point(50,70),"que pretende limpar").draw(win)
        self.nImpurezas = Entry(Point(50,50), 5).draw(win)
        self.nImpurezas.setText(str(nImpurezas))
        
        self.seguinte = Botao(self.win, Point(20,20), 35,10 , "Seguinte", "white")
        self.seguinte.activate()
        
        self.quit = Botao(self.win, Point(80,20), 20, 10, "Quit", "white")
        self.quit.activate()
        
      
    def get_nImpurezas(self):
        """Método que retorna o número de impurezas """
        self.nImpurezas = int(self.nImpurezas.getText())
        return self.nImpurezas
    
    
    def use(self): 
        """Método que deteta que botão é clicado, retornando "Seguinte" ou "Quit"""
        a = True
        while a == True:
            point = self.win.getMouse()
            if self.quit.clicked(point):
                self.close()
                a = False
                return "Quit"
            if self.seguinte.clicked(point):
              a = False
              return "Seguinte"

    
    def close(self):    
        """Fechar janela"""
        self.win.close()
    
            
    
class Menu3:
    """O menu 2 permite escolher se os obstáculos da terceira implementação
    são lidos de um ficheiro ou gerados aleatoriamente"""
    
    def __init__(self, opcao_obstaculos, opcao_Imp):   
        """Método que desenha o menu 3 graficamente"""
        self.opcao_Imp = opcao_Imp
        self.opcao_obstaculos = opcao_obstaculos
        
        self.win = win= GraphWin("Implementação 3", 300, 300)
        self.win.setCoords(0, 0, 100, 100)
        self.win.setBackground('antiquewhite')
            
        Text(Point(50,90),"IMPLEMENTAÇÃO 3").draw(self.win)
        
        Text(Point(50,70),"Criar obstáculos").draw(self.win)     
        self.Botao_A = Botao(self.win,Point(20,60),30,10,"Ler ficheiro", "salmon")
        self.Botao_B = Botao(self.win,Point(80,60),30,10,"Aleatórios", "salmon")
        
        if self.opcao_obstaculos == "Ler Ficheiro":
            self.Botao_B.activate()
            self.Botao_A.deactivate()
            
        elif self.opcao_obstaculos == "Aleatórios":
            self.Botao_B.deactivate()
            self.Botao_A.activate()
        
        Text(Point(50,40),"Impurezas").draw(self.win) 
        self.Botao_C = Botao(self.win,Point(20,30),28,10,"Ler ficheiro", "salmon")
        self.Botao_D = Botao(self.win,Point(50,30),28,10,"Clique Rato", "salmon")
        self.Botao_F = Botao(self.win,Point(80,30),28,10,"Aleatórias","salmon")
        
        if self.opcao_Imp == "Ler Ficheiro":
            self.Botao_D.activate()
            self.Botao_C.deactivate()
            self.Botao_F.activate()
        
        elif self.opcao_Imp == "Clique Rato":
            self.Botao_D.deactivate()
            self.Botao_C.activate()
            self.Botao_F.activate()
            
        elif self.opcao_Imp == "Aleatórias":
            self.Botao_D.activate()
            self.Botao_C.activate()
            self.Botao_F.deactivate()
            
            
        self.Botao_E = Botao(self.win,Point(80,10),20,10,"Quit", "dark turquoise")
        self.Botao_E.activate() 
        
        self.seguinte = Botao(win, Point(20,10), 22, 10, "Seguinte", "salmon")
        self.seguinte.activate()
    
        
    
    def get_opcao_Imp(self):       
        """Método que retorna a opção escolhida pelo utilizador para as impurezas"""
        return str(self.opcao_Imp)
   
    
    def get_opcao_obstaculos(self):
        """Método que retorna a opção escolhida pelo utilizador para os obstáculos"""
        return str(self.opcao_obstaculos)
    
    
    def use(self): 
        """Método que deteta que botão é clicado, retornando "Seguinte" ou "Quit" e
        ativando/desativando botões para retornar as opções escolhidas."""
        a = True
        while True:
                pt = self.win.getMouse()
                
                if self.seguinte.clicked(pt):
                    self.close()
                    return "Seguinte"
                
                elif self.Botao_A.clicked(pt):
                    self.opcao_obstaculos = "Ficheiro"
                    self.Botao_A.deactivate()
                    self.Botao_B.activate()
                    
                elif self.Botao_B.clicked(pt):
                    self.opcao_obstaculos = "Aleatórios"
                    self.Botao_B.deactivate()
                    self.Botao_A.activate()
                    
                elif self.Botao_C.clicked(pt):
                    self.opcao_Imp = "Ficheiro"
                    self.Botao_D.activate()
                    self.Botao_C.deactivate()
                    self.Botao_F.activate()
                    
                elif self.Botao_D.clicked(pt):
                    self.opcao_Imp = "Clique Rato"
                    self.Botao_D.deactivate()
                    self.Botao_C.activate()
                    self.Botao_F.activate()
                    
                elif self.Botao_F.clicked(pt):
                    self.opcao_Imp = "Aleatórias"
                    self.Botao_D.activate()
                    self.Botao_C.activate()
                    self.Botao_F.deactivate()
                    
                    
                    
                elif self.Botao_E.clicked(pt):
                    self.close()
                    a = False
                    return "Quit"
                
                                            
    def close(self):
        """Fechar janela"""
        self.win.close()
        
        

        
      
class Configuracoes: 
    """A classe configurações obtém valores, tais como a cor do roboat, a cor da proa, o número de
#impurezas existentes e o tempo que o roboat demora a limpar as impurezas. """

   
    def __init__(self, corRoboat, corProa, tempolimpeza):
        """Método que desenha o menu das configurações graficamente"""
        self.cor_proa = corProa
        self.cor_roboat= corRoboat
        
        self.win = win = GraphWin("Configurações", 400, 400)
        self.win.setCoords(0,0,100,100)
        self.win.setBackground('antiquewhite')
        
        Text(Point(50,90), "CONFIGURAÇÕES").draw(self.win)
        
        Text(Point(20,70), "Cor Roboat").draw(self.win)
        self.Botao_cr1 = Botao(self.win,Point(55,70),20,15,"Salmão", "salmon")
        self.Botao_cr2 = Botao(self.win,Point(80,70),20,15,"Branco", "white")
        
        if str(self.cor_roboat) == 'salmon':
            self.Botao_cr1.deactivate()
            self.Botao_cr2.activate()
            
        elif str(self.cor_roboat) == 'white':
            self.Botao_cr1.activate()
            self.Botao_cr2.deactivate()
        
        Text(Point(20,50), "Cor Proa").draw(self.win)
        self.Botao_cp1 = Botao(self.win,Point(55,50),20,15,"Violeta", "cornflowerblue")
        self.Botao_cp2 = Botao(self.win,Point(80,50),20,15,"Azul", "dark turquoise")
        if str(self.cor_proa) =='cornflowerblue':
            self.Botao_cp2.activate()
            self.Botao_cp1.deactivate()
        
        elif str(self.cor_proa) =='dark turquoise':
            self.Botao_cp2.deactivate()
            self.Botao_cp1.activate()
            
        Text(Point(20,35), "Tempo limpeza").draw(win)
        self.tempolimpeza = Entry(Point(80,35), 5).draw(win)
        self.tempolimpeza.setText(str(tempolimpeza))

        self.seguinte = Botao(win, Point(50,15), 20, 10, "Seguinte", "salmon")
        self.seguinte.activate()
        
      
              
    def get_tempo(self):
        """Método que retorna o tempo de limpeza """
        self.tempo = int(self.tempolimpeza.getText())
        return self.tempo
     
    
    def get_cor_proa(self):
        """Método que retorna a cor da proa"""
        return self.cor_proa
    
    
    def get_cor_roboat(self):
        """Método que retorna a cor do roboat"""
        return self.cor_roboat
    
    
    def use(self):
        """Método que deteta que botão é clicado, retornando "Seguinte" ou "Quit" e
        ativando/desativando botões para retornar as cores escolhidas"""
        while True:
            pt = self.win.getMouse()
           
            if self.seguinte.clicked(pt):
                self.close()
                return "Seguinte"
            
            elif self.Botao_cr1.clicked(pt):
                    self.cor_roboat = "salmon" 
                    self.Botao_cr1.deactivate()
                    self.Botao_cr2.activate()
                    
            elif self.Botao_cr2.clicked(pt):
                    self.cor_roboat = "white"
                    self.Botao_cr2.deactivate()
                    self.Botao_cr1.activate()
                    
            elif self.Botao_cp1.clicked(pt):
                    self.cor_proa = "cornflowerblue"
                    self.Botao_cp2.activate()
                    self.Botao_cp1.deactivate()
                    
            elif self.Botao_cp2.clicked(pt):
                    self.cor_proa = "dark turquoise"      
                    self.Botao_cp2.deactivate()
                    self.Botao_cp1.activate()

    
    def close(self):   
        """Fechar a janela"""
        self.win.close()
    
    
