import sys
sys.path.append('D:\\PythonProject\\BabaIsYouPython\\src')

from graphics import GameplayGraphic
import pygame
import os
current_dir = os.path.dirname(__file__) 


class MainWindow:
    def __init__(self) -> None:
        pass

    def start_game(self, level):
        pygame.init()

        logo = pygame.image.load(os.path.join(current_dir, "../resources/graphics/baba_raze.png"))
        pygame.display.set_icon(logo)
        pygame.display.set_caption("minimal program")

        self.map_graphic = GameplayGraphic(5,5)
        if level == 1:
            self.map_graphic.load_map_level(os.path.join(current_dir,'../resources/maps/level_1.csv'),os.path.join(current_dir,'../resources/maps/level_1.info'))
        elif level == 2:
            self.map_graphic.load_map_level(os.path.join(current_dir,'../resources/maps/level_2.csv'),os.path.join(current_dir,'../resources/maps/level_2.info'))

        self.window_width = self.cols*42
        self.window_height = self.rows*42

        self.screen = pygame.display.set_mode((self.window_width,self.window_height))


    def run_game(self):
        pass

    def process_event(self, event):
        pass
    