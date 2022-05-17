import sys
from numpy import blackman

from pyparsing import White
sys.path.append('D:\\PythonProject\\BabaIsYouPython\\src')

from graphics import GameplayGraphic
import pygame
import os
current_dir = os.path.dirname(__file__) 


class MainWindow:
    def __init__(self) -> None:
        pass

    def open_main_menu(self):
        self.scene = 'menu'
        pass

    def pop_up_win(self): 
        win_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/you_win.png"))
        # win_banner_resized = pygame.transform.scale(win_banner,(40,40))
        win_width = win_banner.get_width()
        win_height = win_banner.get_height()

        self.screen.blit(win_banner,[(self.window_width-win_width)/2,(self.window_height-win_height)/2])

        reset_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/reset_game.png"))
        reset_width = reset_banner.get_width()
        reset_height = reset_banner.get_height()
        self.screen.blit(reset_banner,[(self.window_width-reset_width)/2,(self.window_height-reset_height)])

    def pop_up_lose(self):
        lose_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/you_lose.png"))
        # win_banner_resized = pygame.transform.scale(win_banner,(40,40))
        lose_width = lose_banner.get_width()
        lose_height = lose_banner.get_height()

        self.screen.blit(lose_banner,[(self.window_width-lose_width)/2,(self.window_height-lose_height)/2])

        reset_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/reset_game.png"))
        reset_width = reset_banner.get_width()
        reset_height = reset_banner.get_height()
        self.screen.blit(reset_banner,[(self.window_width-reset_width)/2,(self.window_height-reset_height)])



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

        self.map_graphic.get_rules()
        self.map_graphic.apply_rules()

        self.window_width = self.map_graphic.columns*40
        self.window_height = self.map_graphic.rows*40

        self.screen = pygame.display.set_mode((self.window_width,self.window_height))
        

        self.running = True

        self.map_graphic.render(self.screen)
        pygame.display.update()


    def run_game(self):
        while self.running:
            
            for event in pygame.event.get():
                self.process_event(event)
            pygame.display.update()


    def process_event(self, event: pygame.event):
        if event.type == pygame.QUIT:
            print('bye bye my love')
            self.running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.map_graphic.move_left()            
            elif event.key == pygame.K_d:
                self.map_graphic.move_right()
            elif event.key == pygame.K_w:
                self.map_graphic.move_up()
            elif event.key == pygame.K_s:
                self.map_graphic.move_down()
            self.screen.fill(('black'))
            self.map_graphic.get_rules()
            self.map_graphic.apply_rules()

            
            self.map_graphic.render(self.screen)

            # rules, win lose condition, interaction, display
            if self.map_graphic.check_lose():
                self.pop_up_lose()
                self.scene = 'endgame'
                print('you lose')   #print to screen later
                # self.running = False
            elif self.map_graphic.check_win():
                self.pop_up_win()
                self.scene = 'endgame'
                print('winner winner chicken dinner')
                # self.running = False
            
if __name__ == '__main__':
    main_window = MainWindow()
    main_window.start_game(2)
    main_window.run_game()

        

        