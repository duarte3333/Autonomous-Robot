# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:38:42 2020

@author:  Duarte Morais 100163 Joana Caramelo 100198
"""
from graphics import *
from Classe_menu_botao import *
from Implementacao_1 import *
from Implementacao_2 import *
from Implementacao_3_mode1_ff import*
from Implementacao_3_mode2_aa import*
from Implementacao_3_mode3_fa import*
from Implementacao_3_mode4_af import*
from Implementacao_3_mode5_fc import*
from Implementacao_3_mode6_ac import*


def main():
    """Função que gere o funcionamento do menu"""
    
    menu_principal = Menu1(20)
    tipo_menu = menu_principal.use()
    cor_proa = "cornflowerblue"
    cor_roboat="salmon"
    tempo_limpeza = 2
    nImpurezas = 3
    opcao_obstaculos = "Ler Ficheiro"
    opcao_Imp = "Ler Ficheiro"
    
    valor = True

    
    while valor == True:
        
            #Se clicar no botão "Implementação 1" corre a 1ª implementação
            if tipo_menu == "Implementacao 1":
                menu_principal.win.close()
                RunBotao_first(cor_roboat, cor_proa, tempo_limpeza)
                valor=False
            
            #Se clicar no botão "Implementação 2" abre a janela do menu2
            elif tipo_menu == "Implementacao 2":
                menu2 = Menu2(nImpurezas)
                b = menu2.use()
                
                #Se clicar em "Seguinte" (após escolher o número de impurezas) corre
                #a 2ª implementação
                if b == "Seguinte":
                    menu_principal.win.close()
                    menu2.win.close()
                    nImpurezas = menu2.get_nImpurezas()
                    RunBotao_second(tempo_limpeza, cor_proa, cor_roboat, nImpurezas)
                    valor = False
                    
                #Se clicar em "Quit" volta ao menu inicial    
                elif b == "Quit":
                    tipo_menu = menu_principal.use()
                    
            #Se clicar no botão "Implementação 3" abre a janela do menu3         
            elif tipo_menu == "Menu 3":
                menu3 = Menu3(opcao_obstaculos, opcao_Imp)
                a = menu3.use()
                
                #Se clicar em Quit volta ao menu principal
                if a == "Quit":
                    tipo_menu = menu_principal.use()
                     
                #Se clicar em "Seguinte" (após o utilizador escolher as opções que quer ) corre a 3ª implementação  
                if a == "Seguinte":
                    
                    opcao_obstaculos = menu3.get_opcao_obstaculos()
                    opcao_Imp = menu3.get_opcao_Imp()
                    
                    #Se o utilizador escolher a opção "Ler ficheiro" para os obstáculos e "Ler ficheiro" para as impurezas
                    if opcao_obstaculos == "Ler Ficheiro" and opcao_Imp == "Ler Ficheiro":
                        menu_principal.win.close()
                        RunBotao_third_mode1(tempo_limpeza, cor_proa, cor_roboat)
                        valor = False
                    
                    #Se o utilizador escolher a opção "Aleatórios" para os obstáculos e "Aleatórias" para as impurezas
                    if opcao_obstaculos == "Aleatórios" and opcao_Imp == "Aleatórias":
                        menu_principal.win.close()
                        RunBotao_third_mode2(tempo_limpeza, cor_proa, cor_roboat)
                        valor = False
    
                    #Se o utilizador escolher a opção "Ler ficheiro" para os obstáculos e "Aleatórias" para as impurezas
                    if opcao_obstaculos == "Ler Ficheiro" and opcao_Imp == "Aleatórias":
                        menu_principal.win.close()
                        RunBotao_third_mode3(tempo_limpeza, cor_proa, cor_roboat)
                        valor = False
    
                    #Se o utilizador escolher a opção "Aleatórios" para os obstáculos e "Ler ficheiro" para as impurezas
                    if opcao_obstaculos == "Aleatórios" and opcao_Imp == "Ler Ficheiro":
                        menu_principal.win.close()
                        RunBotao_third_mode4(tempo_limpeza, cor_proa, cor_roboat)
                        valor = False
           
                    #Se o utilizador escolher a opção "Ler ficheiro" para os obstáculos e "Clique Rato" para as impurezas
                    if opcao_obstaculos == "Ler Ficheiro" and opcao_Imp == "Clique Rato":
                        menu_principal.win.close()
                        RunBotao_third_mode5(tempo_limpeza, cor_proa, cor_roboat)
                        valor = False
                             
                    #Se o utilizador escolher a opção "Aleatórios" para os obstáculos e "Clique Rato" para as impurezas 
                    if opcao_obstaculos == "Aleatórios" and opcao_Imp == "Clique Rato":
                        menu_principal.win.close()
                        RunBotao_third_mode6(tempo_limpeza, cor_proa, cor_roboat)
                        valor = False
                
                        
            #Se clicar em "Configurações" abre-se o menu configurações onde o utilizador
            #pode escolher a cor do roboat, a cor da sua proa e o tempo de limpeza das impurezas
            elif tipo_menu == "Configurações":
                config = Configuracoes(cor_roboat, cor_proa, tempo_limpeza)
                c = config.use()
                
                #Se clicar em seguinte, guardam-se as alterações feitas para poderem ser usadas em qualquer implementação
                if c == "Seguinte":
                    tempo_limpeza = config.get_tempo()
                    cor_proa = config.get_cor_proa()
                    cor_roboat = config.get_cor_roboat()
                    tipo_menu = menu_principal.use()
                                    
              
main()

