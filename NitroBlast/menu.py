import pygame
import pygame_menu

import game
from dificult import Dificult

COLOR_BACKGROUND= (153,153,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
FPS=(60.0)
MENU_BACKGROUND_COLOR = (102,102,153)
MENU_TITTLE_COLOR = (51,51,255)
WINDOW_SCALE = 0.75


pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
WINDOW_SIZE = (13* TILE_SIZE, 13 * TILE_SIZE)

clock = None
show_path = True
surface = pygame.display.set_mode(WINDOW_SIZE)
player_d = Dificult.PLAYER
enemy_easy = Dificult.HARD


def change_path(value, c):
    global show_path 
    show_path = c
def change_player(value, c):
    global player_d
    player_d = c
def chose_dificulty(value, c):
    global enemy_easy
    enemy_easy = c
    
def run_game():
    game.game_init(surface, show_path,player_d, enemy_easy, TILE_SIZE)
    
def main_background():
    global surface
    surface.fill(COLOR_BACKGROUND)

def menu_loop():
    pygame.init()

    pygame.display.set_caption('NitroBlast')
    clock = pygame.time.Clock()
    
    menu_theme = pygame_menu.Theme(
        selection_color= WHITE,
        widget_font = pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color= BLACK,
        title_font= pygame_menu.font.FONT_BEBAS,
        widget_font_color= MENU_BACKGROUND_COLOR,
        widget_font_size= int(TILE_SIZE*0.7),
        background_color=MENU_TITTLE_COLOR
    )
    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        title='Play menu'
    )

    play_options = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        title='Options'
    )
    play_options.add.button('Back', pygame_menu.events.BACK)
    play_menu.add.button('Start',
                         run_game)

    play_menu.add.button('Options', play_options)
    play_menu.add.button('Return  to  main  menu', pygame_menu.events.BACK)
    about_menu_theme = pygame_menu.themes.Theme(
        selection_color=WHITE,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=TILE_SIZE,
        title_font_color=BLACK,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=BLACK,
        widget_font_size=int(TILE_SIZE*0.5),
        background_color=MENU_BACKGROUND_COLOR,
        title_background_color=MENU_TITTLE_COLOR
    )

    about_menu = pygame_menu.Menu(
        theme=about_menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        overflow=False,
        title='About'
    )
    about_menu.add.label("Player controls: ")
    about_menu.add.label("Movement: Arrows")
    about_menu.add.label("Plant bomb: Space")
    about_menu.add.label("Autores:")
    about_menu.add.label("Andres Suarez, Brandon Romero, Cesar Acero", wordwrap=True)
    about_menu.add.label("Sprite: ")
    about_menu.add.label("https://opengameart.org/ content/bomb-party-the-complete-set", wordwrap=True)
    about_menu.add.vertical_margin(25)
    about_menu.add.button('Return  to  main  menu', pygame_menu.events.BACK)

    main_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(WINDOW_SIZE[1] * WINDOW_SCALE),
        width=int(WINDOW_SIZE[0] * WINDOW_SCALE),
        onclose=pygame_menu.events.EXIT,
        title='Main menu'
    )

    main_menu.add.button('Play', play_menu)
    main_menu.add.button('About', about_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    running = True
    while running:

        clock.tick(FPS)

        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background)

        pygame.display.flip()

    exit()


if __name__ == "__main__":
    menu_loop()

    
