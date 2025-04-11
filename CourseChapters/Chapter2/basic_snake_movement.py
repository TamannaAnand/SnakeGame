# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400  # Delay in milliseconds

def move_snake():
   stamper.clearstamps()  # Clear the previous stamps

   new_head = snake[-1].copy() # Copy the last segment to create a new head
   new_head[0] += 20  # Move the head to the right by 20 units
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

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()  # Lift the pen to avoid drawing lines

# create snake as list of coordinates
snake = [[0,0], [20, 0], [40,0], [60,0], [80,0]]

# draw the snake 
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()
    
# set animation in motion 
move_snake()


#finish nicely
turtle.done()