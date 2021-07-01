from turtle import Turtle

class Wall:
    wall_left = Turtle()
    wall_left.penup()
    wall_left.goto(-280, 0)
    wall_left.color("blue")
    wall_left.shape("square")
    wall_left.shapesize(stretch_len=.5, stretch_wid=28.5)


    wall_right = Turtle()
    wall_right.penup()
    wall_right.goto(280, 0)
    wall_right.color("blue")
    wall_right.shape("square")
    wall_right.shapesize(stretch_len=.5, stretch_wid=28.5)


    wall_top = Turtle()
    wall_top.penup()
    wall_top.goto(0, 280)
    wall_top.color("blue")
    wall_top.shape("square")
    wall_top.shapesize(stretch_len=28.5, stretch_wid=.5)


    wall_bottom = Turtle()
    wall_bottom.penup()
    wall_bottom.goto(0, -280)
    wall_bottom.color("blue")
    wall_bottom.shape("square")
    wall_bottom.shapesize(stretch_len=28.5, stretch_wid=.5)