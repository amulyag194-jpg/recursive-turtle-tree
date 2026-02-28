import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.color("brown")
t.pensize(2)

def tree(branch_length):
    if branch_length < 10:
        return

    # Draw branch
    t.forward(branch_length)

    # Draw leaf
    t.color("green")
    t.circle(3)
    t.color("brown")

    # Right branch
    t.left(30)
    tree(branch_length * 0.75)

    # Left branch
    t.right(60)
    tree(branch_length * 0.75)

    # Return to original position
    t.left(30)
    t.backward(branch_length)

# Start tree
tree(100)

turtle.done()



    
