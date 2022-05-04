# import the pygame module, so you can use it
import pygame
import os

current_dir = os.path.dirname(__file__) 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(os.path.join(current_dir, "../../resources/graphic/baba_raze.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
    # screen_width = screen.get_width()
    # screen_height = screen.get_height()
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    logo1 = pygame.image.load(os.path.join(current_dir, "../../resources/graphic/baba_raze.png"))
    logo1_width = logo1.get_width()
    logo1_height = logo1.get_height()

    
    
    while running:
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        screen.blit(logo1,[(screen_width-logo1_width)/2,(screen_height-logo1_height)/2])
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print('o kia choi tiep di ban oi')
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                print(event.button)
                print(event.touch)
                print('chuot xuong r')
                
            elif event.type == pygame.MOUSEBUTTONUP:
                print('chuot len r')

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print('sang trai nao')
                if event.key == pygame.K_d:
                    print('nao sang phai')
                if event.key == pygame.K_w:
                    print('len tren nao')
                if event.key == pygame.K_s:
                    print('gio xuong duoi')

        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()