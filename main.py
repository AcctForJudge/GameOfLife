import pygame
from game_of_life import GameOfLife
from input_rect import InputRect
# pygame setup
pygame.init()

n = 65
c = 0.5

BACKGROUND = (100,100,150)

size = w, h = 192 * 7, 108 * 7
centre = (w / 2, h / 2)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

game = GameOfLife(n, c)
total_w, total_h = 650, 650
gap_h, gap_v = 1,1

o_colour = (255,255,255)
x_colour = (0,0,0)


def initialise_shit(n):
    boxes = [[None for i in range(n)] for j in range(n)]
    box_positions = [[None for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            box = pygame.Surface((total_w / n, total_h / n))
            box.fill(o_colour) if game.grid[i][j] == 'o' else box.fill(x_colour)
            boxes[i][j] = box
        
    return boxes, box_positions

boxes, box_positions = initialise_shit(n)

start_pos = (0,0)
def draw_boxes(s: pygame.Surface, g: GameOfLife, b: list[list[pygame.Surface]], box_positions, initialise_positions = False):
    global start_pos
    start_pos = centre[0] - (g.n * (total_w / g.n + gap_h) - gap_h) / 2.0, centre[1] - (g.n * (total_h / g.n + gap_v) - gap_v) / 2.0
    for y in range(g.n):
        for x in range(g.n):
            box = b[x][y]
            box.fill(o_colour) if game.grid[x][y] == 'o' else box.fill(x_colour)
            pos = (x * (total_w / g.n + gap_h) + start_pos[0],y * (total_h / g.n + gap_v) + start_pos[1])
            s.blit(box, pos)
            if initialise_positions:
                box_positions[x][y] = pos
    

play = False
update = False

game_speed = 100 # ms

pygame.time.set_timer(pygame.USEREVENT, game_speed)

text = pygame.font.Font(None, 30)
step_surface = text.render("Step: ", True, "Black")
info = ['Key Binds:', 'Space - Play/Pause','R - Reset','LMB - Change Cell Colour']

c_input_rect = InputRect(180, 20, 75, 30, str(c))
c_text_surface = text.render("Proportion Alive:", True, "Black")

n_input_rect = InputRect(180, 60, 75, 30, str(n))
n_text_surface = text.render("Grid Size:", True, "Black")

step = 0
first_frame = True


while running:
    mouse_pos = pygame.mouse.get_pos()
    step_counter_surface = text.render(str(step), True, "Black")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = not play
            if event.key == pygame.K_r:
                play = False
                step = 0
                game = GameOfLife(n_input_rect.get_text(True), c_input_rect.get_text())
                boxes, box_positions = initialise_shit(n_input_rect.get_text(True))
        if event.type == pygame.USEREVENT:
            update = True
            pygame.time.set_timer(pygame.USEREVENT, game_speed)
        c_input_rect.handle_event(event)
        n_input_rect.handle_event(event, True)
        if event.type == pygame.MOUSEBUTTONDOWN and not first_frame and not play:
            x = int((mouse_pos[0] - start_pos[0]) // (total_w / game.n + gap_h))
            y = int((mouse_pos[1] - start_pos[1]) // (total_h / game.n + gap_v))
            if 0 <= x < game.n and 0 <= y < game.n:
                if game.grid[x][y] == "o":
                    game.grid[x][y] = "x"
                else:
                    game.grid[x][y] = "o"

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BACKGROUND)

    # RENDER YOUR GAME HERE
    if first_frame:
        draw_boxes(screen, game, boxes, box_positions, True)
        first_frame = False
    else:
        draw_boxes(screen, game, boxes, box_positions)
    screen.blit(step_surface, (w - 280, 25))
    screen.blit(step_counter_surface, (w - 210, 25))
    c_input_rect.draw(screen)
    screen.blit(c_text_surface, (10, 25))
    n_input_rect.draw(screen)
    screen.blit(n_text_surface, (10, 65))
    
    for i, txt in enumerate(info):
        i_surf = text.render(txt, True, "Black")
        screen.blit(i_surf, (w - 280, 75 + i * 50))
    # screen.blit(info_surface, (100, 250))
    if play and update:
        game.play()
        step += 1
        update = False
    
            
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

