# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 03:02:09 2020

@author: Duarte Morais 100163 Joana Caramelo 100198
"""
from graphics import*
from math import* 
    
class Cais:
    
    """Esta classe é responsável por gerar o cais do Roboat através de retângulos"""
    
    def __init__(self,point3,point4,fill2,outline2,win):
        
        """Este método que inicializa a classe Cais"""

        self.point3 = point3
        self.point4 = point4
        self.fill2 = fill2
        self.outline2 = outline2
        self.win = win
        self.b = self.desenhar_cais()

    def desenhar_cais(self):
        
        """Este método desenha graficamente o cais através de retângulos"""
        
        self.b = Rectangle(self.point3,self.point4)
        self.b.setFill(str(self.fill2))
        self.b.setOutline(str(self.outline2))
        self.b.draw(self.win)
    