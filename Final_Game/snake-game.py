# Import the Turtle Graphics and random modules
import turtle
import random
import os

# Define program constants
WIDTH = 800
HEIGHT = 600
FOOD_SIZE = 32
SNAKE_SIZE = 20

# Define image directory path
image_dir = r"C:\Users\Anand\SnakeGame\Final_Game"

offsets = {
    "up": (0, SNAKE_SIZE),
    "down": (0, -SNAKE_SIZE),
    "left": (-SNAKE_SIZE, 0),
    "right": (SNAKE_SIZE, 0)
}

# high score
high_score = 0
delay = 200  # Initial delay in milliseconds

# load high score if it exists 
try:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    pass

def update_high_score():
    global high_score
    if score > high_score:
        high_score = score
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))

# decrease delay if score is greater than 5 
def decrease_delay():
    global delay
    if score > 5:
        delay = 100  # Decrease delay to 500ms
    elif score > 10:
        delay = 80
    elif score > 15:
        delay = 60

def register_shapes():
    # Register custom shapes from the images
    screen.register_shape(os.path.join(image_dir, "apple.gif"))
    screen.register_shape(os.path.join(image_dir, "snake-head.gif"))
    screen.register_shape(os.path.join(image_dir, "bg2.gif"))

def setup_background():
    # Create a background turtle
    background = turtle.Turtle()
    background.hideturtle()
    background.penup()
    background.goto(0, 0)
    # Set the background image
    screen.bgpic(os.path.join(image_dir, "bg2.gif"))

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")

def set_snake_direction(direction):
    global snake_direction
    # Prevent the snake from going in the opposite direction
    # e.g., if the snake is going up, it can't go down.
    if (direction == "up" and snake_direction != "down") or \
       (direction == "down" and snake_direction != "up") or \
       (direction == "left" and snake_direction != "right") or \
       (direction == "right" and snake_direction != "left"):
        snake_direction = direction

def game_loop():
    stamper.clearstamps()  # Remove existing stamps made by stamper.

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        # Add new head to snake body.
        snake.append(new_head)

        # Check food collision
        if not food_collision():
            snake.pop(0)  # Keep the snake the same length unless fed.

        # Draw snake head (use snake_head.gif for the head)
        if USE_IMAGES:
            stamper.shape(os.path.join(image_dir, "snake-head.gif"))
        else:
            stamper.shape("circle")
            
        stamper.goto(snake[-1][0], snake[-1][1])
        
        # Rotate the snake head based on direction
        if USE_IMAGES:
            if snake_direction == "up":
                stamper.setheading(90)
            elif snake_direction == "down":
                stamper.setheading(270)
            elif snake_direction == "left":
                stamper.setheading(180)
            elif snake_direction == "right":
                stamper.setheading(0)
                
        stamper.stamp()
        
        # Draw the rest of the snake body.
        stamper.shape("circle")  # Use circle for the body
        stamper.color("#009EF1")  # Blue color for snake body
        
        # We need to skip the last segment of the snake, which is the head
        for segment in snake[:-1]:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Refresh screen
        screen.title(f"Snake Game. Score: {score} High Score: {high_score}")
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, delay)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1  # score = score + 1 
        update_high_score()  # Update high score if necessary
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        decrease_delay()  # Decrease delay if score is greater than 5
        return True
    return False

def get_random_food_pos():
    x = random.randint(- WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras' Theorem
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [SNAKE_SIZE, 0], [SNAKE_SIZE * 2, 0], [SNAKE_SIZE * 3, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()

# Flag to toggle using images
USE_IMAGES = True

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")

# Debug information to verify paths
print(f"Image directory: {image_dir}")
print(f"Directory exists: {os.path.exists(image_dir)}")
if os.path.exists(image_dir):
    print(f"Files in directory: {os.listdir(image_dir)}")

# Set up images if using them
if USE_IMAGES:
    # Add the ability to use GIF files for images
    apple_path = os.path.join(image_dir, "apple.gif")
    snake_head_path = os.path.join(image_dir, "snake-head.gif")
    bg_path = os.path.join(image_dir, "bg2.gif")
    
    print(f"Apple image exists: {os.path.exists(apple_path)}")
    print(f"Snake head image exists: {os.path.exists(snake_head_path)}")
    print(f"Background image exists: {os.path.exists(bg_path)}")
    
    screen.addshape(apple_path)
    screen.addshape(snake_head_path)
    screen.bgpic(bg_path)
else:
    screen.bgcolor("yellow")

screen.tracer(0)  # Turn off automatic animation.

# Event handlers
screen.listen()
bind_direction_keys()

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("#009EF1")
stamper.penup()

# Food
food = turtle.Turtle()
if USE_IMAGES:
    food.shape(os.path.join(image_dir, "apple.gif"))
else:
    food.shape("triangle")
    food.color("red")
    food.shapesize(FOOD_SIZE / 20)
food.penup()

# Set animation in motion
reset()

# Finish nicely
turtle.done()