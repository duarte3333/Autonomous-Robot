# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:57:38 2020

@author: Duarte Morais 100163 Joana Caramelo 100198
"""
from graphics import*
from math import* 



class Roboat:
    
     """Esta classe cria as propriedades do Roboat"""
    
     def __init__(self,tempo,lista_i):
        
        """Este método inicializa a classe Roboat"""
    
        self.inicio = Point(10,10)
        self.direct = pi/4
        self.lista_i = lista_i
        self.angulo = self.direct
        self.xpos = self.inicio.getX()
        self.ypos = self.inicio.getY()
        self.xvel = 0
        self.yvel = 0
        self.tempo = tempo
             
     def getInicio(self):
         
         """Este método retorna a posição inicial e o angulo inicial do roboat"""
         
         return self.inicio, self.direct
     
     def velocidade(self,destino):
             
            """Este método permite definir a velocidade do Roboat para todas as circunstâncias que possam acontecer na plataforma gráfica"""
         
            #Obter os centros génericos de todas as impurezas em simultâneo, onde quer que estejam
            m1 = destino.getX()
            m2 = destino.getY()
            valor = False
            
            #Obter os centros génericos de todas as ilhas em simultâneo, onde quer que estejam
            for il in self.lista_i:
                 
                a = float(il.ilhas_X())
                b = float(il.ilhas_Y())
              
                #Situação para quando o centro do roboat tem maior abcissa do que o centro da ilha(1º e 4º quadrante)
                if  ((a - self.xpos)**(2) + (b - self.ypos)**(2))**1/2 <= 49 and self.xpos > a :
                    
                        
                        x1 = atan((b-self.ypos)/(a-self.xpos))
                        
                        alfa = atan((1/cos(x1)*(sin(x1))))
                        
                        vel = 40
                        self.xvel=vel*cos(alfa)
                        self.yvel= vel*sin(alfa)  
                        valor = True
                        
                #Situação para quando o centro do roboat tem menor abcissa do que o centro da ilha(2º e 3 quadrante)               
                elif  ((a - self.xpos)**(2) + (b - self.ypos)**(2))**1/2 <= 49 and self.xpos < a:
                    
                        
                        x1 = atan((b-self.ypos)/(a-self.xpos))
                        
                        alfa = atan((1/cos(x1+pi)*(sin(x1+pi))))
                        
                        vel = 40
                        self.xvel=-vel*cos(alfa)
                        self.yvel=-vel*sin(alfa)  
                        valor = True
                        
                #Situação para quando o centro do roboat tem a mesma abcissa que o centro da ilha
                elif  ((a - self.xpos)**(2) + (b - self.ypos)**(2))**1/2 <= 49 and self.xpos == a:
                        
                        alfa = 0
                        
                        vel = 40
                        self.xvel=vel*cos(alfa)
                        self.yvel= vel*sin(alfa)  
                        valor = True
       
                        
                #Situação para quando o Roboat não tem de contornar nenhum obstaculo        
                elif valor == False:
                        self.mover(destino)    

     def mover(self,destino):
             
                 """Este método calcula a velocidade do Roboat em linha reta para o destino"""
         
                 self.dx = destino.getX() - self.xpos 
                 self.dy = destino.getY() - self.ypos
                 
                 vel=40
                 
                 self.angulo_2()
                 self.xvel=vel*cos(self.angulo)
                 self.yvel= vel*sin(self.angulo)  
                 
     def angulo_2(self):
        
        """Este método define o angulo do vetor velocidade, considerando o centro do Roboat como referencial"""
         
        if self.dx >0:
            self.angulo = atan(self.dy/self.dx)
            
        elif self.dx <0:
                self.angulo = atan(self.dy/self.dx)+pi
        elif self.dx==0:
            if self.dy>0:
                    self.angulo = pi/2
            elif self.dy<0:
                     self.angulo = -pi/2
    
     def setAngulo(self, angulo3):
         
          """Este método que permite redefinir o angulo"""
         
          self.angulo = angulo3
                 
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
      
     def getAngulo(self):
         
        """Este método retorna o valor do angulo do vetor velocidade"""
         
        return self.angulo
     
        
class Roboat_graph:
    
    """Esta classe é responsável por criar gráficamente o Roboat"""
    
    def __init__(self,raio1,centro1,cor_roboat,cor_proa,outline3,tempo,win,listai):
        
        self.cor_proa = cor_proa
        self.cor_roboat = cor_roboat
        self.listai = listai
        self.centro1 = centro1
        self.raio1 = raio1
        self.outline3 = outline3
        self.win = win      
        self.c = Roboat(tempo,listai)
        self.desenhar()
    

    def desenhar(self):
        
       """Este método desenha o Roboat e a proa do Roboat em ambiente gráfico"""
        
       self.bola_graph()
       self.triangulo_graph()

    def mover_roboat(self,pos):
        
        """Este método irá atualizar a posição do Roboat ao longo do tempo"""
        
        x=pos.getX()
        y=pos.getY()    
        if x > self.c.getX():
                       while x > self.c.getX():
                               self.velocidade_graph(pos)
                               self.update(1/200)
                               update(200)  
                               
        elif x < self.c.getX():
                       while x < self.c.getX(): 
                               self.velocidade_graph(pos)
                               self.update(1/200)
                               update(200)   
    
    def triangulo_graph(self):
            
        """Este método elabora uma proa triangular, de maneira que aponte sempre para a mesma direção do vetor velocidade do Roboat ao longo do tempo. """  
            
        ax= self.c.getX() + self.raio1*cos(self.c.getAngulo())
        ay= self.c.getY() + self.raio1*sin(self.c.getAngulo())
            
        bx= self.c.getX() + self.raio1*cos(self.c.getAngulo()-pi/2)
        by= self.c.getY() + self.raio1*sin(self.c.getAngulo()-pi/2)    
                                
        cx= self.c.getX() + self.raio1*cos(self.c.getAngulo()+pi/2)
        cy= self.c.getY() + self.raio1*sin(self.c.getAngulo()+pi/2)
            
        self.triangulo = Polygon(Point(bx,by),Point(ax,ay),Point(cx,cy))
        self.triangulo.setFill(self.cor_proa)
        self.triangulo.setOutline('black')
        self.triangulo.draw(self.win)
    
    def bola_graph(self):
        
        """Este método desenha o Roboat em ambiente gráfico"""
       
        self.bola = Circle(Point(self.c.getX(), self.c.getY()),self.raio1)
        self.bola.setFill(str(self.cor_roboat))
        self.bola.setOutline(str(self.outline3))
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
        self.triangulo.undraw()