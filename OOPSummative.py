##############################
# Kelton Figurski
# OOP Summative
# Moving Square
##############################

import pygame

#sets colors
SQUARE = (140, 20, 80)
BACKROUND = (60,200,90)

# class for the square object
class Square:
    #initialization function
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    #function that draws the square
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
    
    # function that changes the x and y coordinates of the square
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

#class that controls the movement of the square
class Movement(Square):
    #initialization function
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.speed = 20
    
    #function that calls the move method to move it to the left
    def move_left(self):
        self.move(-self.speed, 0)
    
    #function that calls the move method to move it to the right
    def move_right(self):
        self.move(self.speed, 0)
    
    #function that calls the move method to move it up
    def move_up(self):
        self.move(0, -self.speed)
    
    #function that calls the move method to move it down
    def move_down(self):
        self.move(0, self.speed)

#initialize pygame
pygame.init()

#create pygame screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# variable for movement class
movement = Movement(100, 100, 50, 50, (SQUARE))

#starts loop until running is false
running = True
while running:
    for event in pygame.event.get():
        #ends loop if user hits the x button
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #calls move_left method if user hits left arrow key
            if event.key == pygame.K_LEFT:
                movement.move_left()
            
            #calls move_right method if user hits right arrow key
            elif event.key == pygame.K_RIGHT:
                movement.move_right()
            
            #calls move_up method if user hits up arrow key
            elif event.key == pygame.K_UP:
                movement.move_up()
            
            #calls move_down method if user hits down arrow key
            elif event.key == pygame.K_DOWN:
                movement.move_down()
    
    #draws the screen
    screen.fill(BACKROUND)
    movement.draw(screen)
    pygame.display.update()
    
#exits pygame after the loop is over
pygame.quit()