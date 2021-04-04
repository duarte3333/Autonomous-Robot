# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 01:58:48 2021

@author: Duarte Morais
"""
from graphics import*
from math import*

class Roboat:
    
     """Esta classe cria as propriedades do Roboat"""
    
     def __init__(self,tempo):
        
        """Este método inicializa a classe Roboat"""
    
        self.inicio = Point(10,10)
        self.xpos = self.inicio.getX()
        self.ypos = self.inicio.getY()
        self.xvel = 0
        self.yvel = 0
        self.angulo = pi/3
        self.tempo = tempo
             
     def getInicio(self):
         
         """Este método retorna a posição inicial e o angulo inicial do roboat"""
         
         return self.inicio, self.direct
     
     def velocidade(self,destino):
                 
                 if self.ypos >= 100:
                     self.yvel= -40
                     self.xvel = 0
                
                 elif self.xpos >= 100:
                     self.xvel = -40
                     self.yvel = 0
                
                 elif self.ypos <= 0:
                     self.yvel= 40
                     self.xvel= 0
                
                 elif self.xpos >= 100:
                     self.xvel = 40
                     self.yvel= 0
                     
                 else:
                     self.mover(destino)    

     def mover(self,destino):
             
                 """Este método calcula a velocidade do Roboat em linha reta para o destino"""
         
                 self.dx = destino.getX() - self.xpos 
                 self.dy = destino.getY() - self.ypos
                 
                 vel = 40
                 self.xvel=vel*cos(self.angulo)
                 self.yvel= vel*sin(self.angulo)  
                 
                 
                 
     def update(self, time):
         
        "Este método atualiza a posição e o vetor velocidade do Roboat a cada instante"
         
        self.xpos = self.xpos + time * self.xvel
        self.ypos = self.ypos + time * self.yvel 
        
     def getY(self):
         
        """Este método retorna o valor da ordenada do centro do roboat"""
         
        return self.ypos
    
     def getX(self):
         
        """Este método retorna o valor da abcissa do centro do Roboat""" 
        
        return self.xpos
      

        
class Roboat_graph:
    
    """Esta classe é responsável por criar gráficamente o Roboat"""
    
    def __init__(self,raio1,centro1,cor_roboat,tempo,win):
        
        self.cor_roboat = cor_roboat
        self.centro1 = centro1
        self.raio1 = raio1
        self.win = win
        self.tempo = tempo
        self.c = Roboat(self.tempo)
        self.desenhar()
    

    def desenhar(self):
        
       """Este método desenha o Roboat e a proa do Roboat em ambiente gráfico"""
        
       self.bola_graph()


    def mover_roboat(self,pos):
        
        """Este método irá atualizar a posição do Roboat ao longo do tempo"""

        x=pos.getX()
        y=pos.getY()    
        if x > self.c.getX():
                       while x != self.c.getX():
                               self.velocidade_graph(pos)
                               self.update(1/200)
                               update(200)  
                               
        elif x < self.c.getX():
                       while x != self.c.getX(): 
                               self.velocidade_graph(pos)
                               self.update(1/200)
                               update(200)   
    
    def bola_graph(self):
        
        """Este método desenha o Roboat em ambiente gráfico"""
       
        self.bola = Circle(Point(self.c.getX(), self.c.getY()),self.raio1)
        self.bola.setFill(str(self.cor_roboat))
        self.bola.draw(self.win)
    
    def velocidade_graph(self,pos):
        
        """Este método chama o método velocidade da Class Roboat para que o Roboat tenha velocidade em ambiente gráfico"""
        
        self.c.velocidade(pos)
    
    def mover_fim_graph(self):
        
        """Este método desloca o Roboat de volta para o cais após a limpeza das impurezas"""
        
        pos , angulo = self.c.getInicio()
        self.mover_roboat(pos)
        self.c.setAngulo(angulo)
        
        self.undraw()
        self.desenhar()
           
    def update(self, dt):
        
        """Este método atualiza constantemente o local do Roboat em ambiente gráfico"""
        
        self.undraw()
        self.c.update(dt)
        self.desenhar()
     
    def getX(self):
        
        """Este método retorna a abcissa do centro do Roboat em ambiente gráfico"""
        
        return self.c.getX()
    
    def getY(self):
        
        """Este método retorna a ordenada do centro do Roboat em ambiente gráfico"""
         
        return self.c.getY()
    
    def undraw(self):
        
        """Este método apaga em ambiente gráfico a proa e o Roboat"""
        
        self.bola.undraw()  
        
def main():
    
     window =  GraphWin("Animação",800,800,autoflush=False)
     window.setCoords(0,0,100,100)
     window.setBackground("salmon") 
     window.getMouse()
     
     Bola = Roboat_graph(3,Point(50,50),"white",0.01,window)
     while True:
         p1 = window.getMouse() 
         Bola.mover_roboat(p1)
     
main()
    