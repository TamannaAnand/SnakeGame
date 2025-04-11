# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400  # Delay in milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def move_snake():
   stamper.clearstamps()  # Clear the previous stamps

   new_head = snake[-1].copy() # Copy the last segment to create a new head
   # x coordinate of the new head
   new_head[0] += offsets[snake_direction][0] 
   # y coordinate of the new head
   new_head[1] += offsets[snake_direction][1]
   
   snake.append(new_head)  # Add the new head to the snake
   
   snake.pop(0)  # Remove the tail segment 
   
   # draw the snake 
   for segment in snake:
       stamper.goto(segment[0], segment[1])
       stamper.stamp()
    
   screen.update()

   turtle.ontimer(move_snake, DELAY)  # Schedule the next move    
# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)  # Turn off automatic screen updates

# event handlers for key presses
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()  # Lift the pen to avoid drawing lines

# create snake as list of coordinates
snake = [[0,0], [20, 0], [40,0], [60,0], [80,0]]

snake_direction = "up"

# draw the snake 
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()
    
# set animation in motion 
move_snake()


#finish nicely
turtle.done()