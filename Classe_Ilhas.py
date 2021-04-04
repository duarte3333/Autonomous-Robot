# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 02:58:45 2020

@author: Duarte Morais 100163 Joana Caramelo 100198
"""
from graphics import*
from math import* 

class Ilha:
    
    """Esta classe irá gerar as ilhas que o Roboat terá que se desviar para limpar os detritos"""

    def __init__(self,centro,fill,outline,win, opcao):
        
        """Este método que inicializa a classe Ilha"""
        
        self.opcao = opcao
        self.centro = centro
        self.fill= fill
        self.outline = outline
        self.win =win
        self.desenhar_ilha()

    def desenhar_ilha(self):
        
        """Este método permite escolher qual é o formato da ilha que será desenhada na plataforma gráfica"""
        
        if self.opcao == "Triangulo":
            self.triangulo_ilha_graph()
        elif self.opcao == "Circulo":
            self.circulo_ilha_graph()
        elif self.opcao== "Cruz":
            self.cruz_ilha_graph()
        elif self.opcao == 'Quadrado':
            self.quadrado_ilha_graph()
               
    def quadrado_ilha_graph(self):
        
            """Este método elabora ilhas em formato quadrangular"""    
        
            dist = 5
            ax= self.centro.getX() + dist*cos(pi/4)
            ay= self.centro.getY() + dist*sin(pi/4)
                
            bx= self.centro.getX() + dist*cos(5*pi/4)
            by= self.centro.getY() + dist*sin(5*pi/4)  

            self.retangulo = Rectangle(Point(bx,by),Point(ax,ay))
            self.retangulo.setFill(str(self.fill))
            self.retangulo.setOutline(str(self.outline))
            self.retangulo.draw(self.win)  
            
       
    def circulo_ilha_graph(self):
     
            """Este método elabora ilhas em formato circular"""

            dist = 5
            ax= self.centro.getX()
            ay= self.centro.getY() 
        
            self.circulo = Circle(Point(ax,ay),5)
            self.circulo.setFill(str(self.fill))
            self.circulo.setOutline(str(self.outline))
            self.circulo.draw(self.win)
          
    def triangulo_ilha_graph(self):
        
            """Este método elabora ilhas em formato triangular"""
            
            dist = 5
            ax= self.centro.getX() + dist*cos(pi/4)
            ay= self.centro.getY() + dist*sin(pi/4)
                
            bx= self.centro.getX() + dist*cos(3*pi/4)
            by= self.centro.getY() + dist*sin(3*pi/4)  
                                    
            cx= self.centro.getX() + dist*cos(-pi/2)
            cy= self.centro.getY() + dist*sin(-pi/2)  
                                    
                
            self.triangulo = Polygon(Point(bx,by),Point(ax,ay),Point(cx,cy))
            self.triangulo.setFill(str(self.fill))
            self.triangulo.setOutline(str(self.outline))
            self.triangulo.draw(self.win)
            
    def cruz_ilha_graph(self):
        
            """Este método elabora ilhas em formato de cruz"""
        
            dist = 5
            dist_1 = 2.5
            
            ax= self.centro.getX() + dist_1*cos(pi/4)
            ay= self.centro.getY() + dist_1*sin(pi/4)
                
            bx= self.centro.getX() + dist*cos(pi/3)
            by= self.centro.getY() + dist*sin(pi/3)  
                                    
            cx= self.centro.getX() + dist*cos(2*pi/3)
            cy= self.centro.getY() + dist*sin(2*pi/3)  
                
            dx= self.centro.getX() + dist_1*cos(3*pi/4)
            dy= self.centro.getY() + dist_1*sin(3*pi/4)
                
            ex= self.centro.getX() + dist*cos(5*pi/6)
            ey= self.centro.getY() + dist*sin(5*pi/6)  
                                    
            fx= self.centro.getX() + dist*cos(7*pi/6)
            fy= self.centro.getY() + dist*sin(7*pi/6)    

            gx= self.centro.getX() + dist_1*cos(5*pi/4)
            gy= self.centro.getY() + dist_1*sin(5*pi/4)
                
            hx= self.centro.getX() + dist*cos(4*pi/3)
            hy= self.centro.getY() + dist*sin(4*pi/3)  
                                    
            ix= self.centro.getX() + dist*cos(5*pi/3)
            iy= self.centro.getY() + dist*sin(5*pi/3)  
                
            jx= self.centro.getX() + dist_1*cos(7*pi/4)
            jy= self.centro.getY() + dist_1*sin(7*pi/4)
                
            mx= self.centro.getX() + dist*cos(11*pi/6)
            my= self.centro.getY() + dist*sin(11*pi/6)  
                                    
            nx= self.centro.getX() + dist*cos(pi/6)
            ny= self.centro.getY() + dist*sin(pi/6)                      
                
            self.cruz = Polygon(Point(ax,ay),Point(bx,by),Point(cx,cy),
                                     Point(dx,dy),Point(ex,ey),Point(fx,fy),
                                     Point(gx,gy),Point(hx,hy),Point(ix,iy),
                                     Point(jx,jy),Point(mx,my),Point(nx,ny))
            self.cruz.setFill(str(self.fill))
            self.cruz.setOutline(str(self.outline))
            self.cruz.draw(self.win)
     
    def ilhas_X(self):
        
            """Este método retorna o valor da abcissa do centro de uma dada ilha"""
             
            return self.centro.getX()
    
    def ilhas_Y(self):
             
            """Este método retorna o valor da ordenada do centro de uma dada ilha"""
        
            return self.centro.getY()       
