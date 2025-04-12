# Import the Turtle Graphics and random modules
import turtle
import random

# Define program constants
WIDTH = 800
HEIGHT = 600
DELAY = 100  # Milliseconds
FOOD_SIZE = 32
SNAKE_SIZE = 20

offsets = {
    "up": (0, SNAKE_SIZE),
    "down": (0, -SNAKE_SIZE),
    "left": (-SNAKE_SIZE, 0),
    "right": (SNAKE_SIZE, 0)
}

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

        # Draw snake 
        stamper.shape("circle")
        stamper.goto(snake[-1][0], snake[-1][1])
        stamper.stamp()
        stamper.shape("circle")
        # Draw the rest of the snake body.
        # We need to skip the last segment of the snake, which is the head
        for segment in snake[:-1]:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Refresh screen
        screen.title(f"Snake Game. Score: {score}")
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1  # score = score + 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
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


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
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
food.shape("triangle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Set animation in motion
reset()

# Finish nicely
turtle.done()