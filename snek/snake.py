import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
HIGH = 0
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1), # south
    'l' : (-1,0), # west
    'r' : (1,0) # east
}

class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # TODO: See section 3, "Turning the snake".
        self.direction = dir
        pass

    def collision(self, x, y):
        # checks for collision with border
        if x < 0 or x > 23 or y < 0 or y > 23:
            self.dead = True
        
        # checks for collision with self
        for i in range(len(self.body)-1):
            if (x,y) == self.body[i+1]:
                self.dead = True

        pass
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        newBody = []
        # moving the head
        newBody.append((self.body[0][0] + DIR[self.direction][0], self.body[0][1] + DIR[self.direction][1]))
        
        # moving the rest of the body
        for i in range(len(self.body) - 1):
            newBody.append(self.body[i])

        # detecting if the snake ate the apple
        if self.l + 1 != len(self.body):
            newBody.append(self.body[len(self.body) - 1])

        # detecting if a collision with border or self occurred in this move
        self.collision(newBody[0][0], newBody[0][1])

        self.body = newBody
        pass

    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    
    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        pass


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        while self.position in snake:
            self.position = (rand_int(23), rand_int(23))
        pass

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def draw_grid_dead(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (139,0,0) if (x+y) % 2 == 0 else (83,0,0)
            pygame.draw.rect(surface, color, r)
            pygame.display.update()

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0
    show_score = 0

    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    while True:
        # TODO: see section 10, "incremental difficulty".
        clock.tick(10 * (1 + snake.l/8))
        snake.check_events()
        draw_grid(surface)        
        snake.move()

        snake.draw(surface)
        
        if snake.get_head() == apple.position:
            print("the snake ate an apple!")
            apple.place(snake.body)
            snake.l += 1
            score += 1
            show_score = 10
            score_cyan = myfont.render('SCORE: %d' % score, False, (0, 255, 255))
            score_magenta = myfont.render('SCORE: %d' % score, False, (255, 102, 153))

        apple.draw(surface)

        screen.blit(surface, (0,0))

        if score == 0:
            textsurface = myfont.render('SCORE: 0', False, (0, 0, 0))
            screen.blit(textsurface,(0,0))

        if show_score in range(1,11,4) or show_score in range(2,11,4):
            screen.blit(score_cyan,(0,0))
            show_score += -1
        
        if show_score in range(3,11,4) or show_score in range(4,11,4):
            screen.blit(score_magenta,(0,0))
            show_score += -1
        global HIGH
        if score > HIGH:
            print(HIGH)
            HIGH = score
        highscore_text = textsurface = myfont.render('HIGH: %d' % HIGH, False, (128,128,128))
        screen.blit(highscore_text,(350,0))

        # TODO: see section 8, "Display the Score"

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            main()

if __name__ == "__main__":
    main()