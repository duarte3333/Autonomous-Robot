# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 02:41:28 2020

@author: Duarte Morais 100163 Joana Caramelo 100198
"""
from graphics import*
from math import* 
              
class Impureza:
    
    """Este classe irá gerar os detritos em ambiente gráfico"""
  
    def __init__(self,centro2,fill,outline,win):
    
        """Este método inicializa a classe Impureza"""

        self.centro2 = centro2
        self.fill= fill
        self.outline = outline
        self.win =win
        self.desenhar_impurezas()
          
    def desenhar_impurezas(self):
        
        """Este método permite desenhar em ambiente gráfico as impurezas"""
           
        self.impr = Circle(self.centro2,2)
        self.impr.setFill(str(self.fill))
        self.impr.setOutline(str(self.outline))
        self.impr.draw(self.win)  
    
    def getCentro(self):
        
        """Este método retorna o centro da impureza"""
        
        return self.centro2
    
    def undraw_imp(self):
        
        """Este método apaga a impureza gráficamente"""
        
        self.impr.undraw()
