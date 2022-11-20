import turtle

def main():
    print('Please enter number of squares: ')
    n = int(input())
    total_fan_of_squares(n,100)
    turtle.hideturtle()
    turtle.done()

def turtle_square(side_len):
     for i in range(4):
        turtle.forward(side_len)
        turtle.left(90)

def total_fan_of_squares(num_of_sqrs, side_len):
    for count in range(num_of_sqrs):
        turtle_square(side_len)
        turtle.left(360/num_of_sqrs)


main()
