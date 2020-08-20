import pygame
from pygame.locals import *
from sys import exit
import cv2
import time
import face_recognition
from PIL import Image

pygame.init()

capture = False

#screen information
data_screen = pygame.display.Info()
screen_xy = (data_screen.current_w, data_screen.current_h)
screen = pygame.display.set_mode(screen_xy, FULLSCREEN, 32)
screen.fill((0,0,0))
