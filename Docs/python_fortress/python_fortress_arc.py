import turtle as t
import random

def turn_up(cannon_range):            # ↑를 눌렀을 때 호출되는 함수
  t.left(2)
  cannon_range += 2

def turn_down(cannon_range):          #↓를 눌렀을 때 호출되는 함수
  t.right(2)
  cannon_range -= 2

# 현재 거북이의 위치로 포물선 궤적의 y좌표 구하자 
# 표준형 : y = -(x-a)^2 + a^2 = -x(x-2a) 
# 일반형 : y = -x^2 + 2*a*x 
def calculate_pos_y(turtle_pos_x, cannon_range):
  a = cannon_range / 2
  turtle_pos_y = -1*turtle_pos_x**2 + 2*a*turtle_pos_x
  return turtle_pos_y

def fire(turtle_pos_x, turtle_pos_y):  # SpaceBar를 누르면 거북이 대포를 발사합니다.
  while t.xcor() <= cannon_range:      # 거북이가 땅 위에 있는 동안 반복합니다.
    t.setpos(turtle_pos_x, turtle_pos_y)
    turtle_pos_x += 1
    turtle_pos_y = calculate_pos_y(turtle_pos_x, cannon_range)

  # while 반복문을 빠져나오면 거북이가 땅에 닿은 상태입니다.
  d = t.distance(target, 0)       # 거북이와 목표 지점과의 거리를 구합니다.
  t.sety(random.randint(10, 100)) # 성공 또는 실패를 표시할 위치를 지정합니다.
  if d < 25: # 거리 차이가 25보다 작으면 목표 지점에 명중한 것으로 처리합니다.
    t.color("blue")
    t.write("Good!", False, "center", ("", 15))

  else:     # 그렇지 않으면 실패한 것으로 처리합니다.
    t.color("red")
    t.write("Bad!", False, "center", ("", 15))

  t.color("black")    # 거북이 색을 검은색으로 되돌립니다.
  t.goto(-200, 10)    # 거북이 위치를 처음 발사했던 곳으로 되돌립니다.

 

# 주의 : 여기서부터는 들여쓰기를 하지 마세요.
# 발사거리
# 거북이 위치
cannon_range = 0
turtle_pos_x = 0
turtle_pos_y = 0


# 땅을 그립니다.
t.goto(-300, 0)
t.down()
t.goto(300, 0)

 

# 목표 지점을 설정하고 그립니다.
target = random.randint(50, 150) # 목표 지점을 50~150 사이에 있는 임의의 수로 지정합니다.
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

# 거북이 색을 검은색으로 지정하고 처음 발사했던 곳으로 되돌립니다.
t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

# 거북이가 동작하는 데 필요한 설정을 합니다.
t.onkeypress(turn_up(cannon_range), "Up")      # ↑를 누르면 turn_up 함수를 실행합니다.
t.onkeypress(turn_down(cannon_range), "Down")  # ↓를 누르면 turn_down 함수를 실행합니다.
t.onkeypress(fire(turtle_pos_x, turtle_pos_y), "space")      # SpaceBar를 누르면 fire 함수를 실행합니다.
t.listen()                       # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.