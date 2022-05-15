import sys
sys.path.append('D:\\PythonProject\\BabaIsYouPython\\src')

from gameplay import Baba, Rock, Wall, Water, Skull, Flag, Word

import pygame
import os

current_dir = os.path.dirname(__file__) 

class BabaGraphic(Baba):
    def render(self, window, x, y):
        baba_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))
        baba_image_resized = pygame.transform.scale(baba_image,(40,40))

        window.blit(baba_image_resized,[x,y])
        

class RockGraphic(Rock):
    def render(self, window, x, y):
        rock_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/rock.png"))
        rock_image_resized = pygame.transform.scale(rock_image,(40,40))

        window.blit(rock_image_resized,[x,y])

class WallGraphic(Wall):
    def render(self, window, x, y):
        wall_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/wall.png"))
        wall_image_resized = pygame.transform.scale(wall_image,(40,40))

        window.blit(wall_image_resized,[x,y])

class WaterGraphic(Water):
    def render(self, window, x, y):
        water_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/water.png"))
        water_image_resized = pygame.transform.scale(water_image,(40,40))

        window.blit(water_image_resized,[x,y])

class SkullGraphic(Skull):
    def render(self, window, x, y):
        skull_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/skull.png"))
        skull_image_resized = pygame.transform.scale(skull_image,(40,40))

        window.blit(skull_image_resized,[x,y])

class FlagGraphic(Flag):
    def render(self, window, x, y):
        flag_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/flag.png"))
        flag_image_resized = pygame.transform.scale(flag_image,(40,40))

        window.blit(flag_image_resized,[x,y])

class WordGraphic(Word):
    def render(self, window, x, y):
        png_file_name = "../../resources/graphics/" + self.value.upper() + "-w.png"
        png_image = pygame.image.load(os.path.join(current_dir, png_file_name))
        png_image_resized = pygame.transform.scale(png_image,(png_image.get_width()/6, png_image.get_height()/6))
        
        window.blit(png_image_resized, [x,y])


        # if self.value == 'is':
        #     is_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))

        #     window.blit(is_image,[x,y])

        # elif self.value == 'you':
        #     you_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))

        #     window.blit(you_image,[x,y])
            
        # elif self.value == 'push':
        #     push_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))

        #     window.blit(push_image,[x,y])

        # elif self.value == 'sink':
        #     sink_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))

        #     window.blit(sink_image,[x,y])
            
        # elif self.value == 'defeat':
        #     defeat_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))

        #     window.blit(defeat_image,[x,y])

        # elif self.value == 'stop':
        #     stop_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))

        #     window.blit(stop_image,[x,y])

        # elif self.value == 'win':
        #     win_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))

        #     window.blit(win_image,[x,y])

if __name__ == '__main__':
    pygame.init()

    logo = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba_raze.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
    running = True

    baba_test = BabaGraphic('you')

    while running:
        baba_test.render(screen, 600, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()