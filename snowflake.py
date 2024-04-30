import turtle

def koch_snowflake(t, order, size):
    '''
    Calculating snowflake
    '''
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    '''
    Main function, processing inputing params, painting snowflakes
    '''

    order = int(input("Введіть рівень рекурсії (ціле число, від 1 до 5): "))
    if order<1:
        print("Число замале, бажано від 1 до 5")
        return False
    elif order>5:
        print("Це забагато, буде дуже довго малюватись, спробуй від 1 до 5")
        return False
    
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for i in range(3):
        koch_snowflake(t, order, 300)
        t.right(120)

    screen.mainloop()

if __name__ == "__main__":
    main()
