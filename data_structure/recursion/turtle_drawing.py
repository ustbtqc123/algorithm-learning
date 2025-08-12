import turtle

t = turtle.Turtle()


def draw_spiral(t, line_len):
    if line_len > 0:
        t.forward(line_len)
        t.right(90)
        draw_spiral(t, line_len - 5)


if __name__ == '__main__':
    draw_spiral(t, 100)
    turtle.done()
