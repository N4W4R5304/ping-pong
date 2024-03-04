import pygame
import sys
import random

#initiating pygame
pygame.init()

#setting the height and width of the screen
HEIGHT, WIDTH = 600, 600

#making the screen load
screen = pygame.display.set_mode((HEIGHT, WIDTH))

#naming the window 
pygame.display.set_caption("Ping Pong")

#setting the fps setting
time = pygame.time.Clock()
#

#the value of fps
fps = 60

#Ball setting
ball_x, ball_y = WIDTH / 2.5, HEIGHT / 2.5
x_speed, y_speed = 5 * random.choice((1,-1)), 5 * random.choice((1, -1))
ball = pygame.Rect(ball_x, ball_y, 30, 30)

def ball_res():
    global ball_x, ball_y
    ball.center = (WIDTH/2, HEIGHT/2)
    ball_x *= random.choice((1,-1))
    ball_y *= random.choice((1,-1))

speed = 15
class PADDLE:

    #setting the pos and height and widht of the paddle from the main file
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        
    #drawing the paddle
    def draw_pad(self):
        #drawing the paddle
        pygame.draw.rect(screen, pygame.Color("White"),(self.x, self.y, self.width, self.height))

    #moving the right paddle
    def move(self):

        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= speed

        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += speed


    #moving the left paddle
    def move_l(self):

        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_w] and self.y > 0:
            self.y -= speed

        if keys[pygame.K_s] and self.y < HEIGHT - self.height:
            self.y += speed

#paddle setting
pad_w, pad_h = 10, 100
left_paddle = pygame.Rect(HEIGHT /2 - 295, WIDTH/2 , pad_w, pad_h)
right_paddle = pygame.Rect(HEIGHT /2 + 285, WIDTH/2 , pad_w , pad_h)

#def difficulty():
    #pass




#draws objects
def draw():
    #making the background black
    screen.fill(pygame.Color("Black"))

    
    pygame.draw.ellipse(screen, pygame.Color("White"), ball)
      
    pygame.draw.rect(screen, pygame.Color("White"), left_paddle)
    pygame.draw.rect(screen, pygame.Color("White"), right_paddle)
    
    #updates the screen
    pygame.display.update()




while True:
    #quits the game when we press the x button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #difficulty()

    #moving the both paddle
    PADDLE.move(right_paddle)
    PADDLE.move_l(left_paddle)
    
    #movement of the ball
    ball.x += x_speed
    ball.y += y_speed
    
    #collision  
    col = 10
    if ball.bottom >= HEIGHT or ball.top <= 0:
        y_speed *= -1

    if ball.colliderect(left_paddle):
        if abs(left_paddle.right - ball.left) < col:
            x_speed *= -1
    
    if ball.colliderect(right_paddle):
        if abs(right_paddle.left - ball.right) < col:
            x_speed *= -1
    
    if ball.right >= WIDTH or ball.left <= 0:
        ball_res()


    #calling the draws fuwwnction and setting the value of the paddles that pass in the draw function
    draw()

    #collision(left_paddle, right_paddle, ball=BA)
    #setting the framerate of the game
    time.tick(fps)

