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

dic_images = {"3286x1080": "back3286x1080.png"}

if screen_xy == (3286, 1080):
    screen = pygame.display.set_mode((3286, 1080), FULLSCREEN, 32)
    image_dimention = dic_images["3286x1080"]
    image_dimention_rend = pygame.image.load(image_dimention).convert_alpha()
    screen.blit(image_dimention_rend, (0, 0))

def capture_img():
    image = cv2.VideoCapture(0)
    check, frame = image.read()
    cv2.imshow("Verification", frame)
    cv2.waitKey(1)
    cv2.imwrite("verify.jpg", frame)
    cv2.destroyAllWindows()
    image.release()

def faces_p(image_path):
    """ The image have a face?"""
    img = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(img)
    img_lst = []
    if face_locations == []:
        return False
    else:
        return True
