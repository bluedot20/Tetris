import pygame
import random
s_width = 800
s_height = 700

play_width = 300
play_height = 600

block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
pygame.font.init()
I = [[False,True,False], [False,True,False], [False,True,False], [False,True,False]]
l = [[False,False,False], [False,False,True], [True,True,True]]
s = [[False,False,False], [False,True,True], [True,True,False]]
z = [[False,False,False], [True,True,False], [False,True,True]]
j = [[False,True,False], [False,True,False], [True,True,False]]
t = [[False,False,False], [False,True,False], [True,True,True]]
o = [[False,False,False], [False,True,True], [False,True,True]]

shapes = [I, j, s, o, z, t, l]
shape_colors = [(255, 104, 195),
                (0, 255, 239),
                (208, 230, 65),
                (255, 255, 204),
                (53, 23, 152),
                (92, 178, 141),
                (175, 178, 92)]

class Piece(object):
    def __init__(self, shape):
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_positions={}):
    grid = [[0 for column in range(10)] for row in range(20)]
    return grid

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    shape = Piece(random.choice(shapes))



def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label,(top_left_x + play_width/2 - (label.get_width()/2),
                        top_left_y + play_height/2 - label.get_height()/2))




def draw_grid(surface, row, col):
    pass

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 20)
    label = font.render("Next Shape", 1, (255,255,123))

    surface.blit(label, (top_left_x + play_width+100 - (label.get_width() /2), 150))


def draw_window(win, grid):
    win.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render("Tetris", 1, (255,255,123))

    win.blit(label, (top_left_x + play_width/2 - (label.get_width() /2), 30))

    pygame.draw.rect(win, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 5)

def main(win):
    run = True
    print("MAIN GAME BEGINS")
    locked_positions = {}
    grid = create_grid(locked_positions)
    current_shape = get_shape()
    next_shape = get_shape()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

        draw_window(win, grid)
        draw_next_shape(next_shape, win )
        pygame.display.update()

def main_menu(win):
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle("Press any key to start", 60, (255,255,123), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)
    pygame.display.quit()

window = pygame.display.set_mode((s_width, s_height))
main_menu(window)





















