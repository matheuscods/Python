"""Desafio 021 proposto pelo Professor Guanabara (Curso Python #08 - Utilizando Módulos)
-> Faça um programa em python que abra e reproduza o áudio de um arquivo MP3"""
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("desafio_006/teste.mp3")
pygame.mixer.music.play()
input("Digite enter para parar a musica")
