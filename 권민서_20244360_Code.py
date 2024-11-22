import turtle as t


def my_flag():
    width = 800
    height = 400

    def draw_Star(start_x, start_y, length, color):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.setheading(72)

        t.color(color)

        for _ in range(7):
            t.forward(length)
            t.right(138)
            t.forward(length)
            t.left(87)

        t.end_fill()

    def draw_circle(x, y, radius, color):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(-90)
        t.begin_fill()
        t.color(color)
        t.circle(radius, 360)
        t.end_fill()

    def draw_rectangle(color, start_x, start_y, width, height):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.color(color)
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

    def draw_bg():
        draw_rectangle("#191970", -width / 2, -height / 2, width, height)

    def draw_KMS_flag():
        t.setup(width, height)
        t.speed(5)
        t.bgcolor("#191970")

        t.speed(150)
        draw_bg()
        draw_rectangle("#87CEFA", -width / 2, -height / 2, 80, height)
        draw_rectangle("#87CEFA", width / 2 - 80, -height / 2, 80, height)
        draw_circle(-115, 0, 115, "#00008B")
        draw_circle(-110, 0, 110, "#000080")
        draw_circle(-105, 0, 105, "#0000CD")
        draw_circle(-100, 0, 100, "#0000FF")
        draw_circle(-95, 0, 95, "#4169E1")
        draw_circle(-90, 0, 90, "#6495ED")
        draw_circle(-85, 0, 85, "#1E90FF")
        draw_circle(-80, 0, 80, "#00BFFF")
        draw_circle(-75, 0, 75, "#1E90FF")
        draw_circle(-70, 0, 70, "#6495ED")
        draw_circle(-65, 0, 65, "#4169E1")
        draw_circle(-60, 0, 60, "#0000FF")
        draw_circle(-55, 0, 55, "#0000CD")
        draw_circle(-50, 0, 50, "#000080")
        draw_circle(-45, 0, 45, "#00008B")
        draw_Star(-8, 15, 20, "#FFFFFF")

        t.hideturtle()


    draw_KMS_flag()


def algeria():
    width = 500
    height = 250
    swidth = width + 100
    sheight = height + 100

    def draw_border():
        t.penup()
        t.goto(-width / 2, -height / 2)
        t.pendown()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)

    def draw_rectangle(color, start_x, start_y):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.color(color)
        t.setheading(0)
        for _ in range(2):
            t.left(90)
            t.forward(height)
            t.left(90)
            t.forward(width // 2)
        t.end_fill()

    def draw_moon():
        t.penup()
        t.goto(-83, 0)
        t.pendown()
        t.setheading(-90)
        t.begin_fill()
        t.color("#D21034")
        t.circle(83)
        t.end_fill()

        t.begin_fill()
        t.color("white")
        # 내부 원호 그리기
        t.penup()
        t.goto(-45, 0)
        t.setheading(-90)
        t.pendown()
        t.circle(66)
        t.end_fill()
        t.color("#006233")
        t.begin_fill()
        t.penup()
        t.goto(0, 63.2)
        t.pendown()
        t.setheading(196)
        t.circle(66, 148)
        t.goto(0, 63.2)
        t.end_fill()

        # 외부 원호로 이동하여 마무리

    def draw_star():
        t.color("#D21034")
        t.penup()
        t.goto(30, 0)
        t.pendown()
        t.begin_fill()
        t.fillcolor("#D21034")  # 내부 색상을 노란색으로 지정
        t.setheading(240)
        for _ in range(5):
            t.forward(30)
            t.left(144)
            t.forward(30)
            t.right(72)
        t.end_fill()

    def draw_algerian_flag():
        t.setup(width=swidth, height=sheight)
        t.speed(100)
        t.bgcolor("white")
        start_x = 0
        start_y = - (height / 2)

        # 달 그리기
        draw_border()
        draw_rectangle("#006233", start_x, start_y)
        draw_moon()
        draw_star()

        t.hideturtle()


    draw_algerian_flag()


def antigua():
    width = 690
    height = 460
    swidth = width + 100
    sheight = height + 100

    def draw_red_triangle():
        t.penup()
        t.goto(-width / 2, -height / 2)
        t.setheading(0)

        t.color("#CE1126")

        t.begin_fill()
        t.forward(345)
        t.left(127)
        t.forward(573.252)
        t.left(143)
        t.forward(460)
        t.end_fill()
        t.penup()
        t.goto(width / 2, -height / 2)
        t.setheading(180)
        t.begin_fill()
        t.forward(345)
        t.right(127)
        t.forward(573.252)
        t.right(143)
        t.forward(460)
        t.end_fill()

    def draw_black_triangle():
        t.penup()
        t.goto(0, -height / 2)
        t.setheading(127)

        t.color("#000000")

        t.begin_fill()
        t.forward(575.966)
        t.right(127)
        t.forward(693)
        t.right(127)
        t.forward(575.966)
        t.end_fill()

    def draw_blue_triangle():
        t.penup()
        t.goto(0, -height / 2)
        t.setheading(127)

        t.color("#0072C6")

        t.begin_fill()
        t.forward(350.588)
        t.right(127)
        t.forward(421.96)
        t.right(127)
        t.forward(350.588)
        t.end_fill()

    def draw_white_triangle():
        t.penup()
        t.goto(0, -height / 2)
        t.setheading(127)

        t.color("#FFFFFF")

        t.begin_fill()
        t.forward(225.378)
        t.right(127)
        t.forward(271.26)
        t.right(127)
        t.forward(225.378)
        t.end_fill()

    def draw_sun():
        t.penup()
        t.goto(-75, 50)
        t.pendown()
        t.setheading(-90)
        t.begin_fill()
        t.color("#FCD116")
        t.circle(75, 360)
        t.end_fill()

        t.penup()
        t.goto(-75, 50)
        t.pendown()
        t.setheading(180)
        t.begin_fill()
        t.color("#FCD116")
        t.forward(75)
        t.right(169)
        t.forward(76.4025)
        t.left(135.4)

        for _ in range(7):
            t.forward(76.4025)
            t.right(158)
            t.forward(76.4025)
            t.left(135.5)

        t.forward(76.4025)
        t.right(169)
        t.forward(300)
        t.end_fill()

    def draw_AntiguaBarbuda_flag():
        t.setup(width=swidth, height=sheight)
        t.speed(100)
        t.bgcolor("#FFFFFF")

        draw_black_triangle()
        draw_sun()
        draw_blue_triangle()
        draw_white_triangle()
        draw_red_triangle()

        t.hideturtle()



    draw_AntiguaBarbuda_flag()


def australia():
    u_width = 300
    u_height = 150
    width = 600
    height = 300
    swidth = width + 100
    sheight = height + 100

    def draw_rectangle(color, start_x, start_y, width, height):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.color(color)
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

    def draw_Star(start_x, start_y, length):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.setheading(72)

        t.color("#FFFFFF")

        for _ in range(7):
            t.forward(length)
            t.right(138)
            t.forward(length)
            t.left(87)

        t.end_fill()

    def draw_star():
        t.color("#FFFFFF")
        t.penup()
        t.goto(180, -10)
        t.pendown()
        t.begin_fill()
        t.setheading(254.5)
        for _ in range(5):
            t.forward(8)
            t.left(144)
            t.forward(8)
            t.right(72)
        t.end_fill()

    def draw_white_x():
        # 작은 국기의 하얀 대각선 X 형태
        t.penup()
        t.goto(-width / 2, 133.23)
        t.setheading(-27)

        t.color("#FFFFFF")

        t.begin_fill()
        t.forward(298.40228)
        t.left(27)
        t.forward(34.04)
        t.left(90)
        t.forward(16.77)
        t.left(63)
        t.forward(298.40228)
        t.left(27)
        t.forward(34.04)
        t.left(90)
        t.forward(16.77)

        t.end_fill()
        t.setheading(0)

        t.penup()
        t.goto(-width / 2, 0)
        t.setheading(0)

        t.color("#FFFFFF")

        t.begin_fill()
        t.forward(34.04)
        t.left(27)
        t.forward(298.40228)
        t.left(63)
        t.forward(16.77)
        t.left(90)
        t.forward(34.04)
        t.left(27)
        t.forward(298.40228)
        t.left(63)
        t.forward(16.77)

        t.end_fill()
        t.setheading(0)

    def draw_red_x():
        # 작은 국기의 빨간 대각선 X 형태
        t.penup()
        t.goto(-width / 2, 138.82)
        t.setheading(-27)

        t.color("#CF142B")

        t.begin_fill()
        t.forward(167.7)
        t.left(117)
        t.forward(11.18)
        t.left(63)
        t.forward(167.7)
        t.left(117)
        t.forward(11.18)

        t.end_fill()
        t.setheading(0)

        t.penup()
        t.goto(0, 9.68)
        t.setheading(153)

        t.color("#CF142B")

        t.begin_fill()
        t.forward(167.7)
        t.left(117)
        t.forward(11.18)
        t.left(63)
        t.forward(167.7)
        t.left(117)
        t.forward(11.18)

        t.end_fill()
        t.setheading(0)

        t.penup()
        t.goto(-width / 2, 0)
        t.setheading(0)

        t.color("#CF142B")

        t.begin_fill()
        t.forward(22.36)
        t.left(27)
        t.forward(167.7)
        t.left(153)
        t.forward(22.36)
        t.left(27)
        t.forward(167.7)

        t.end_fill()
        t.setheading(0)

        t.penup()
        t.goto(0, height / 2)
        t.setheading(180)

        t.color("#CF142B")

        t.begin_fill()
        t.forward(22.36)
        t.left(27)
        t.forward(167.7)
        t.left(153)
        t.forward(22.36)
        t.left(27)
        t.forward(167.7)

        t.end_fill()
        t.setheading(0)

    def draw_white_cross():
        # 작은 국기의 중앙의 하얀 십자가
        draw_rectangle("#FFFFFF", -width / 2, 50, u_width, 50)
        draw_rectangle("#FFFFFF", -175, 0, 50, u_height)

    def draw_red_cross():
        # 작은 국기의 중앙의 빨간 십자가
        draw_rectangle("#CF142B", -width / 2, 60, u_width, 30)
        draw_rectangle("#CF142B", -165, 0, 30, u_height)

    def draw_u_bg():
        # 파란 배경
        draw_rectangle("#00247D", -width / 2, -height / 2, width, height)

    def draw_Australia_flag():
        t.setup(width=swidth, height=sheight)
        t.speed(5)
        t.bgcolor("white")

        t.speed(100)
        draw_u_bg()
        draw_white_x()
        draw_red_x()
        draw_white_cross()
        draw_red_cross()

        draw_Star(-150, -70, 25)
        draw_Star(70, 20, 10)
        draw_Star(150, 110, 10)
        draw_Star(220, 50, 10)
        draw_Star(150, -100, 10)
        draw_star()

        t.hideturtle()


    draw_Australia_flag()


def canada():
    t.begin_fill()
    t.color('#FF0000')
    width = 500
    height = 250
    swidth = width + 100
    sheight = height + 100
    t.setup(width=swidth, height=sheight)
    t.shape('turtle')
    t.speed(50)
    t.penup()
    t.goto(0, -height + 150)
    t.pendown()
    t.forward(10)
    t.left(93)
    t.forward(50)
    t.right(103)
    t.forward(50)
    t.left(120)
    t.forward(25)
    t.right(75)
    t.forward(70)
    t.left(120)
    t.forward(20)
    t.right(95)
    t.forward(30)
    t.left(135)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.left(115)
    t.forward(40)
    t.right(135)
    t.forward(60)
    t.left(135)
    t.forward(20)
    t.right(95)
    t.forward(48)

    t.penup()
    t.goto(0, -height + 150)
    t.setheading(-180)
    t.pendown()
    t.pendown()
    t.forward(10)
    t.right(93)
    t.forward(50)
    t.left(103)
    t.forward(50)
    t.right(120)
    t.forward(25)
    t.left(75)
    t.forward(70)
    t.right(120)
    t.forward(20)
    t.left(95)
    t.forward(30)
    t.right(135)
    t.forward(30)
    t.left(90)
    t.forward(20)
    t.right(115)
    t.forward(40)
    t.left(135)
    t.forward(60)
    t.right(135)
    t.forward(20)
    t.left(95)
    t.forward(48)
    t.end_fill()

    t.penup()
    t.goto(-width / 2 / 2, -height / 2)
    t.pendown()
    t.begin_fill()
    t.goto(-width / 2 / 2, height / 2)
    t.goto(-width / 2, height / 2)
    t.goto(-width / 2, -height / 2)
    t.goto(-width / 2 / 2, -height / 2)
    t.end_fill()

    t.penup()
    t.goto(width / 2 / 2, height / 2)
    t.pendown()
    t.begin_fill()
    t.goto(width / 2 / 2, height / 2)
    t.goto(width / 2, height / 2)
    t.goto(width / 2, -height / 2)
    t.goto(width / 2 / 2, -height / 2)
    t.end_fill()

    t.penup()
    t.color('black')
    t.goto(-width / 2, height / 2)
    t.pendown()
    t.setheading(0)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)

    t.hideturtle()



def cuba():
    width = 600
    height = 300
    swidth = width + 100
    sheight = height + 100

    def draw_rectangle(color, start_x, start_y, width, height):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.color(color)
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

    def draw_triangle():
        t.penup()
        t.goto(-width / 2, height / 2)
        t.setheading(-30)

        t.color("#CF142B")

        t.begin_fill()
        t.forward(300)
        t.right(120)
        t.forward(300)
        t.right(120)
        t.forward(300)
        t.end_fill()
        t.setheading(0)

    def draw_star(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.fillcolor("#FFFFFF")
        t.setheading(180)
        for _ in range(5):
            t.forward(30)
            t.left(144)
            t.forward(30)
            t.right(72)
        t.end_fill()

    def draw_cuba_flag():
        t.setup(width=swidth, height=sheight)
        t.speed(100)
        t.bgcolor("#FFFFFF")
        start_x = -width / 2
        start_y = 90
        stripe_height = 60

        # Draw stripes
        for i in range(5):
            if i % 2 == 0:
                color = "#002A8F"
            else:
                color = "#FFFFFF"
            draw_rectangle(color, start_x, start_y - i * stripe_height, 600, stripe_height)

        t.speed(100)
        draw_triangle()
        draw_star(-width / 2 + 100, 13)

        t.hideturtle()


    draw_cuba_flag()


def greece():
    width = 675
    height = 450
    swidth = width + 100
    sheight = height + 100

    def draw_rectangle(color, start_x, start_y, width, height):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.color(color)
        for _ in range(2):
            t.forward(width)
            t.right(90)
            t.forward(height)
            t.right(90)
        t.end_fill()

    def draw_square():
        draw_rectangle("#0D5EAF", -width / 2, height / 2, 248, 248)

    def draw_cross():
        draw_rectangle("#FFFFFF", -width / 2, 125, 248, 48)
        draw_rectangle("#FFFFFF", -width / 2 + 100, height / 2, 48, 250)

    def draw_greece_flag():
        t.setup(width=swidth, height=sheight)
        t.speed(100)
        t.bgcolor("#FFFFFF")
        start_x = -width / 2
        start_y = height / 2
        stripe_height = 50

        # Draw stripes
        for i in range(9):
            if i % 2 == 0:
                color = "#0D5EAF"
            else:
                color = "#FFFFFF"
            draw_rectangle(color, start_x, start_y - i * stripe_height, 675, stripe_height)

        t.speed(100)
        draw_square()
        draw_cross()

        t.hideturtle()


    draw_greece_flag()


def korea():
    width = 360
    height = 240
    swidth = width + 130
    sheight = height + 150
    t.shape('turtle')
    t.setup(width=swidth, height=sheight)
    t.speed(100)
    t.bgcolor("white")

    def draw_border():

        t.penup()
        t.goto(-200, -150)
        t.pendown()
        t.color("black")
        t.setheading(0)
        t.forward(width + 50)
        t.left(90)
        t.forward(height + 50)
        t.left(90)
        t.forward(width + 50)
        t.left(90)
        t.forward(height + 50)

    # 태극문양 큰 원
    t.goto(width / 6, 0)
    t.setheading(90)
    t.begin_fill()
    t.color("#CD313A")
    t.circle(width / 6, 180)
    t.end_fill()

    t.setheading(-90)
    t.begin_fill()
    t.color("#0047A0")
    t.circle(width / 6, 180)
    t.end_fill()

    # 태극문양 작은 원
    t.begin_fill()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color("#0047A0")
    t.setheading(-90)
    t.circle(width / 12)
    t.end_fill()
    t.begin_fill()
    t.setheading(90)
    t.color("#CD313A")
    t.circle(width / 12)
    t.end_fill()

    # 왼쪽 위 검정 바 작성
    t.penup()
    t.goto(-155, 40)
    t.setheading(180 - 33.69)

    t.color('black')

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.right(90)
        t.forward(82.8)
        t.right(90)
    t.end_fill()
    t.goto(-135, 28)
    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.right(90)
        t.forward(82.8)
        t.right(90)
    t.end_fill()

    t.goto(-115, 16)
    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.right(90)
        t.forward(82.8)
        t.right(90)
    t.end_fill()

    # 오른쪽 위 검정 바 작성
    t.penup()
    t.goto(155, 40)
    t.setheading(33.69)

    t.color('black')

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.left(90)
        t.forward(37)
        t.left(90)
    t.end_fill()

    t.left(90)
    t.forward(45)
    t.right(90)

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.left(90)
        t.forward(37)
        t.left(90)
    t.end_fill()

    t.goto(135, 28)
    t.begin_fill()
    t.color('black')
    for _ in range(2):
        t.forward(13.8)
        t.left(90)
        t.forward(82.8)
        t.left(90)
    t.end_fill()

    t.goto(115, 16)
    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.left(90)
        t.forward(37)
        t.left(90)
    t.end_fill()

    t.left(90)
    t.forward(45)
    t.right(90)

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.left(90)
        t.forward(37)
        t.left(90)
    t.end_fill()

    # 왼쪽 아래 검정 바 작성

    t.penup()
    t.goto(-75, -110)
    t.setheading(33.69)

    t.color('black')

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.left(90)
        t.forward(82.8)
        t.left(90)
    t.end_fill()

    t.goto(-95, -122)
    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.left(90)
        t.forward(37)
        t.left(90)
    t.end_fill()

    t.left(90)
    t.forward(45)
    t.right(90)

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.left(90)
        t.forward(37)
        t.left(90)
    t.end_fill()

    t.goto(-115, -134)
    t.begin_fill()
    t.color('black')
    for _ in range(2):
        t.forward(13.8)
        t.left(90)
        t.forward(82.8)
        t.left(90)
    t.end_fill()

    t.goto(0, 0)

    # 오른쪽 아래 검정바
    t.penup()
    t.goto(75, -110)
    t.setheading(180 - 33.69)

    t.color('black')

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.right(90)
        t.forward(37)
        t.right(90)
    t.end_fill()

    t.right(90)
    t.forward(45)
    t.left(90)

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.right(90)
        t.forward(37)
        t.right(90)
    t.end_fill()

    t.goto(95, -122)
    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.right(90)
        t.forward(37)
        t.right(90)
    t.end_fill()

    t.right(90)
    t.forward(45)
    t.left(90)

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.right(90)
        t.forward(37)
        t.right(90)
    t.end_fill()

    t.goto(115, -134)
    # ----------------------------#
    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.right(90)
        t.forward(37)
        t.right(90)
    t.end_fill()

    t.right(90)
    t.forward(45)
    t.left(90)

    t.begin_fill()
    for _ in range(2):
        t.forward(13.8)
        t.right(90)
        t.forward(37)
        t.right(90)
    t.end_fill()

    draw_border()

    t.hideturtle()



def macedonia():
    width = 700
    height = 350
    swidth = width + 100
    sheight = height + 100

    def draw_rectangle(color, start_x, start_y, width, height):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.color(color)
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

    def draw_line():
        t.penup()
        t.goto(-width / 2, height / 2)
        t.pendown()
        t.begin_fill()
        t.color("#F8E92E")
        t.setheading(0)
        t.forward(105)
        t.right(36)
        t.forward(302.8347)
        t.right(171)
        t.forward(391.3)
        t.end_fill()

        t.penup()
        t.goto(-width / 2, -height / 2)
        t.pendown()
        t.begin_fill()
        t.color("#F8E92E")
        t.setheading(0)
        t.forward(105)
        t.left(36)
        t.forward(302.8347)
        t.left(171)
        t.forward(391.3)
        t.end_fill()

        t.penup()
        t.goto(width / 2, height / 2)
        t.pendown()
        t.begin_fill()
        t.color("#F8E92E")
        t.setheading(180)
        t.forward(105)
        t.left(36)
        t.forward(302.8347)
        t.left(171)
        t.forward(391.3)
        t.end_fill()

        t.penup()
        t.goto(width / 2, -height / 2)
        t.pendown()
        t.begin_fill()
        t.color("#F8E92E")
        t.setheading(180)
        t.forward(105)
        t.right(36)
        t.forward(302.8347)
        t.right(171)
        t.forward(391.3)
        t.end_fill()

        t.penup()
        t.goto(-width / 2, 30)
        t.pendown()
        t.begin_fill()
        t.color("#F8E92E")
        t.setheading(-5)
        t.forward(351.33665)
        t.right(170)
        t.forward(351.33665)
        t.right(95)
        t.forward(70)
        t.end_fill()

        t.penup()
        t.goto(width / 2, 30)
        t.pendown()
        t.begin_fill()
        t.color("#F8E92E")
        t.setheading(-175)
        t.forward(351.33665)
        t.left(170)
        t.forward(351.33665)
        t.left(95)
        t.forward(70)
        t.end_fill()

        t.penup()
        t.goto(-35, height / 2)
        t.pendown()
        t.begin_fill()
        t.color("#F8E92E")
        t.setheading(-79)
        t.forward(178.9095)
        t.left(158)
        t.forward(178.9095)
        t.left(101)
        t.forward(70)
        t.end_fill()

        t.penup()
        t.goto(-35, -height / 2)
        t.pendown()
        t.begin_fill()
        t.color("#F8E92E")
        t.setheading(79)
        t.forward(178.9095)
        t.right(158)
        t.forward(178.9095)
        t.right(101)
        t.forward(70)
        t.end_fill()

    def draw_circle():
        t.penup()
        t.goto(-62.5, 0)
        t.pendown()
        t.setheading(-90)
        t.begin_fill()
        t.color("#D82126")
        t.circle(62.5, 360)
        t.end_fill()

        t.penup()
        t.goto(-50, 0)
        t.pendown()
        t.setheading(-90)
        t.begin_fill()
        t.color("#F8E92E")
        t.circle(50, 360)
        t.end_fill()

    def draw_bg():
        # 빨간 배경
        draw_rectangle("#D82126", -width / 2, -height / 2, width, height)

    def draw_Macedonia_flag():
        t.setup(width=swidth, height=sheight)
        t.speed(5)
        t.bgcolor("white")

        t.speed(150)
        draw_bg()
        draw_line()
        draw_circle()

        t.hideturtle()


    draw_Macedonia_flag()


def turkey():
    width = 500
    height = 250
    swidth = width + 100
    sheight = height + 100

    def draw_border():
        t.penup()
        t.goto(-width / 2, -height / 2)
        t.pendown()
        t.begin_fill()
        t.color("#E30A17")
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.end_fill()

    def draw_moon():
        t.penup()
        t.goto(-180, 0)
        t.pendown()
        t.setheading(-90)
        t.begin_fill()
        t.color("white")
        t.circle(70)
        t.end_fill()

        t.begin_fill()
        t.color("#E30A17")
        # 내부 원호 그리기
        t.penup()
        t.goto(-142, 0)
        t.setheading(-90)
        t.pendown()
        t.circle(53)
        t.end_fill()
        t.color("#006233")
        t.begin_fill()
        t.penup()

        # 외부 원호로 이동하여 마무리

    def draw_star():
        t.color("white")
        t.penup()
        t.goto(0, 10)
        t.pendown()
        t.begin_fill()
        t.color("white")
        t.setheading(120)
        for _ in range(5):
            t.forward(25)
            t.left(144)
            t.forward(25)
            t.right(72)
        t.end_fill()

    def draw_turkey_flag():
        t.setup(width=swidth, height=sheight)
        t.speed(100)
        t.bgcolor("white")
        start_x = 0
        start_y = - (height / 2)

        # 달 그리기
        draw_border()
        draw_moon()
        draw_star()

        t.hideturtle()


    draw_turkey_flag()


def uk():
    width = 600
    height = 300
    swidth = width + 100
    sheight = height + 100

    def draw_rectangle(color, start_x, start_y, width, height):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.color(color)
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

    def draw_white_x():
        # 대각선 X 형태
        t.penup()
        t.goto(-width / 2, 116.46)
        t.setheading(-27)

        t.color("#FFFFFF")

        t.begin_fill()
        t.forward(596.80456)
        t.left(27)
        t.forward(68.08)
        t.left(90)
        t.forward(33.54)
        t.left(63)
        t.forward(596.80456)
        t.left(27)
        t.forward(68.08)
        t.left(90)
        t.forward(33.54)

        t.end_fill()
        t.setheading(0)

        t.penup()
        t.goto(-width / 2, -height / 2)
        t.setheading(0)

        t.color("#FFFFFF")

        t.begin_fill()
        t.forward(68.08)
        t.left(27)
        t.forward(596.80456)
        t.left(63)
        t.forward(33.54)
        t.left(90)
        t.forward(68.08)
        t.left(27)
        t.forward(596.80456)
        t.left(63)
        t.forward(33.54)

        t.end_fill()
        t.setheading(0)

    def draw_red_x():
        t.penup()
        t.goto(-width / 2, 127.64)
        t.setheading(-27)

        t.color("#CF142B")

        t.begin_fill()
        t.forward(335.4)
        t.left(117)
        t.forward(22.36)
        t.left(63)
        t.forward(335.4)
        t.left(117)
        t.forward(22.36)

        t.end_fill()
        t.setheading(0)

        t.penup()
        t.goto(width / 2, -130.64)
        t.setheading(153)

        t.color("#CF142B")

        t.begin_fill()
        t.forward(335.4)
        t.left(117)
        t.forward(22.36)
        t.left(63)
        t.forward(335.4)
        t.left(117)
        t.forward(22.36)

        t.end_fill()
        t.setheading(0)

        t.penup()
        t.goto(-width / 2, -height / 2)
        t.setheading(0)

        t.color("#CF142B")

        t.begin_fill()
        t.forward(44.72)
        t.left(27)
        t.forward(335.4)
        t.left(153)
        t.forward(44.72)
        t.left(27)
        t.forward(335.4)

        t.end_fill()
        t.setheading(0)

        t.penup()
        t.goto(width / 2, height / 2)
        t.setheading(180)

        t.color("#CF142B")

        t.begin_fill()
        t.forward(44.72)
        t.left(27)
        t.forward(335.4)
        t.left(153)
        t.forward(44.72)
        t.left(27)
        t.forward(335.4)

        t.end_fill()
        t.setheading(0)

    def draw_white_cross():
        # 중앙의 하얀 십자가
        draw_rectangle("#FFFFFF", -width / 2, -50, width, 100)
        draw_rectangle("#FFFFFF", -50, -height / 2, 100, height)

    def draw_red_cross():
        # 중앙의 빨간 십자가
        draw_rectangle("#CF142B", -width / 2, -30, width, 60)
        draw_rectangle("#CF142B", -30, -height / 2, 60, height)

    def draw_bg():
        # 파란 배경
        draw_rectangle("#00247D", -width / 2, -height / 2, width, height)

    def draw_UK_flag():
        t.setup(width=swidth, height=sheight)
        t.speed(5)
        t.bgcolor("white")
        start_x = 0
        start_y = - (height / 2)

        t.speed(100)
        draw_bg()
        draw_white_x()
        draw_red_x()
        draw_white_cross()
        draw_red_cross()

        t.hideturtle()


    draw_UK_flag()


def usa():
    width = 494
    height = 262.6
    swidth = width + 100
    sheight = height + 100

    def draw_star(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.fillcolor("white")
        t.setheading(180)
        for _ in range(5):
            t.forward(5)
            t.left(144)
            t.forward(5)
            t.right(72)
        t.end_fill()

    def draw_rectangle(color, start_x, start_y, width, height):
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()
        t.begin_fill()
        t.color(color)
        for _ in range(2):
            t.forward(width)
            t.right(90)
            t.forward(height)
            t.right(90)
        t.end_fill()

    def draw_USA_flag():
        t.setup(width=swidth, height=sheight)
        t.speed(500)
        t.bgcolor("white")
        start_x = -width / 2
        start_y = height / 2
        stripe_height = 20.2
        star_space = 33
        star_row_space = 13.5

        # Draw stripes
        for i in range(13):
            if i % 2 == 0:
                color = "#B22234"  # Red
            else:
                color = "white"
            draw_rectangle(color, start_x, start_y - i * stripe_height, 494, stripe_height)

        # Draw union
        draw_rectangle("#3C3B6E", start_x, start_y, 197.6, 140.01)

        # Draw stars
        t.color("white")
        for row in range(9):
            for col in range(6 if row % 2 == 0 else 5):
                x = start_x + 14 + col * star_space + (0 if row % 2 == 0 else star_space / 2)
                y = start_y - 14 - row * star_row_space
                draw_star(x, y)

        t.hideturtle()


    draw_USA_flag()



country_list = ['로고', '알제리', '마케도니아', '호주', '캐나다', '한국', '미국', '영국', '터키', '쿠바', '그리스', '앤티가바부다']


while True:
    user_input = int(input("""그리고 싶은 항목의 번호를 입력해주세요.\n 1. 로고\n 2. 알제리\n 3. 마케도니아\n 4. 호주\n 5. 캐나다\n 6. 한국\n 7. 미국\n 8. 영국\n 9. 터키\n 10. 쿠바\n 11. 그리스\n 12. 앤티가바부다\n 13. 모든 국기 그리기  \n 14. 프로그램 종료 \n :"""))
    t.reset()
    if user_input == 1:
        my_flag()

    elif user_input == 2:
        algeria()

    elif user_input == 3:
        macedonia()

    elif user_input == 4:
        australia()

    elif user_input == 5:
        canada()

    elif user_input == 6:
        korea()

    elif user_input == 7:
        usa()

    elif user_input == 8:
        uk()

    elif user_input == 9:
        turkey()

    elif user_input == 10:
        cuba()

    elif user_input == 11:
        greece()

    elif user_input == 12:
        antigua()

    elif user_input == 13:
        my_flag()
        t.reset()
        algeria()
        t.reset()
        macedonia()
        t.reset()
        australia()
        t.reset()
        canada()
        t.reset()
        korea()
        t.reset()
        usa()
        t.reset()
        uk()
        t.reset()
        turkey()
        t.reset()
        cuba()
        t.reset()
        greece()
        t.reset()
        antigua()
    elif user_input == 14:
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 번호를 입력해주세요.")







