import sys
import os
current_dir = os.path.dirname(__file__) 
sys.path.append(os.path.join(current_dir,"."))

from graphics import GameplayGraphic
import pygame



class MainWindow:
    def __init__(self) -> None:
        pygame.init()
        # load and set the logo
        logo = pygame.image.load(os.path.join(current_dir, "../resources/graphics/baba.png"))
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Baba Is You Phake")
        self.window_width = 1280
        self.window_height = 720

        self.screen = pygame.display.set_mode((self.window_width,self.window_height))
        # self.background_music = pygame.mixer.music.load(os.path.join(current_dir, '../resources/graphics/Music.mp3'))
        # pygame.mixer.music.play()



    def open_main_menu(self):
        self.scene = 'menu'
        self.screen.fill(('black'))

        menu_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/banner_main_menu.png"))
        menu_width = menu_banner.get_width()
        menu_height = menu_banner.get_height()
        self.screen.blit(menu_banner,[(self.window_width-menu_width)/2,0])

        level_1_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/level_1.png"))
        level_1_banner = pygame.transform.scale(level_1_banner, (160, 80))
        lv1_width = level_1_banner.get_width()
        lv1_height = level_1_banner.get_height()

        self.level_1_banner_rect = level_1_banner.get_rect(topleft=((self.window_width-lv1_width)/2-lv1_width*2,(self.window_height*0.8)))

        self.screen.blit(level_1_banner,self.level_1_banner_rect)
        

        level_2_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/level_2.png"))
        level_2_banner = pygame.transform.scale(level_2_banner, (160, 80))
        lv2_width = level_2_banner.get_width()
        lv2_height = level_2_banner.get_height()

        self.level_2_banner_rect = level_2_banner.get_rect(topleft=((self.window_width-lv2_width)/2+lv2_width*2,(self.window_height*0.8)))

        self.screen.blit(level_2_banner,self.level_2_banner_rect) 

        # get event
        self.running = True
        getting_level = True
        while getting_level and self.running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    print(position)
                    self.level = self.get_level(position)
                    if self.level > 0:
                        getting_level = False
                elif event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    print('bye')
                    self.running = False

            pygame.display.update()
        self.open_gameplay(self.level)


    def get_level(self,position:pygame.mouse):
        if self.level_1_banner_rect.collidepoint(position):
            return 1
        elif self.level_2_banner_rect.collidepoint(position):
            return 2
        else:
            return -1

    def pop_up_win(self): 
        win_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/you_win.png"))
        # win_banner_resized = pygame.transform.scale(win_banner,(40,40))
        win_width = win_banner.get_width()
        win_height = win_banner.get_height()

        self.screen.blit(win_banner,[(self.window_width-win_width)/2,(self.window_height-win_height)/2])

        reset_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/reset_game.png"))
        reset_button = pygame.transform.scale(reset_button, (reset_button.get_width()/2, reset_button.get_height()/2))

        self.reset_button_rect = reset_button.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()*0.75))
        self.screen.blit(reset_button, self.reset_button_rect)
        print(self.reset_button_rect.topleft)

        pygame.display.update()

    def pop_up_lose(self):
        lose_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/you_lose.png"))
        # win_banner_resized = pygame.transform.scale(win_banner,(40,40))
        lose_width = lose_banner.get_width()
        lose_height = lose_banner.get_height()

        self.screen.blit(lose_banner,[(self.window_width-lose_width)/2,(self.window_height-lose_height)/2])

        reset_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/reset_game.png"))
        reset_button = pygame.transform.scale(reset_button, (reset_button.get_width()/2, reset_button.get_height()/2))

        self.reset_button_rect = reset_button.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()*0.75))
        self.screen.blit(reset_button, self.reset_button_rect)
        print(self.reset_button_rect.topleft)
       
        pygame.display.update()


    def open_gameplay(self, level):
        self.screen.fill(('black'))
        self.level = level
        self.scene = 'gameplay'

        self.map_graphic = GameplayGraphic(5,5)

        if level == 1:
            self.map_graphic.load_map_level(os.path.join(current_dir,'../resources/maps/level_1.csv'),os.path.join(current_dir,'../resources/maps/level_1.info'))

        elif level == 2:
            self.map_graphic.load_map_level(os.path.join(current_dir,'../resources/maps/level_2.csv'),os.path.join(current_dir,'../resources/maps/level_2.info'))

        self.running = True
        
        self.map_graphic.get_rules()
        self.map_graphic.apply_rules()
        self.map_graphic.render(self.screen)
        
        pygame.display.update()
        self.run_gameplay()
        if self.scene == 'endgame':
            self.process_endgame_screen()
        



    def run_gameplay(self):
        while self.running and self.scene == 'gameplay':            
            for event in pygame.event.get():
                self.process_event(event)
            pygame.display.update()

    def process_endgame_screen(self):
        self.scene = 'endgame'
        while self.running and self.scene == 'endgame':
            for event in pygame.event.get():
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if self.reset_button_rect.collidepoint(position):
                        print('heeeee')
                        self.scene = 'menu'

                    
                elif event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    print('bye')
                    self.running = False
            pygame.display.update()
        if self.scene == 'menu':     
            self.open_main_menu()

    def process_event(self, event: pygame.event):
        if event.type == pygame.QUIT:
            print('bye bye my love')
            self.running = False

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
    main_window.open_main_menu()
    # main_window.start_game(2)
    # main_window.run_game()

        

        