import turtle as t
import random

# ↑를 누르면 발사각도를 높이는 turn_up 함수
def turn_up():          
  # 거북이를 왼쪽으로 2도 돌립니다  
  t.left(2)             

# ↓를 누르면 발사각도를 낮추는 turn_down 함수
def turn_down():        
  # 거북이를 오른쪽으로 2도 돌립니다  
  t.right(2)            

# SpaceBar를 누르면 거북이 대포를 발사하는 fire 함수
def fire():             
  # 현재 거북이가 바라보는 각도를 기억합니다 
  ang = t.heading()     
  # 거북이가 땅 위에 있는 동안 반복합니다
  while t.ycor() > 0: 
    # 15만큼 앞으로 이동합니다  
    t.forward(15)     
    # 오른쪽으로 5도 회전합니다
    t.right(5)        

  # while 반복문을 빠져나오면 거북이가 땅에 닿은 상태입니다
  # 거북이와 목표 지점과의 거리를 구합니다
  d = t.distance(target, 0)       
  # 성공 또는 실패를 표시할 위치를 지정합니다
  t.sety(random.randint(10, 100)) 
  # 거리 차이가 25보다 작으면 목표 지점에 명중한 것으로 처리합니다
  if d < 25: 
    t.color("blue")
    t.write("Good!", False, "center", ("", 15))
  # 그렇지 않으면 실패한 것으로 처리합니다
  else:     
    t.color("red")
    t.write("Bad!", False, "center", ("", 15))
  
  # 거북이 색을 검은색으로 되돌립니다
  t.color("black")    
  # 거북이 위치를 처음 발사했던 곳으로 되돌립니다
  t.goto(-200, 10)    
  # 각도도 처음 기억해 둔 각도로 되돌립니다
  t.setheading(ang)   

# 주의 : 여기서부터는 들여쓰기를 하지 마세요.

# 땅을 왼쪽부터 그립니다
# (-300, 0)으로 간다
t.goto(-300, 0)
# (300, 0)으로 간다
t.goto(300, 0)

# 목표 지점을 설정하고 그립니다
# 목표 지점을 50~150 사이에 있는 임의의 수로 지정합니다
target = random.randint(50, 150) 
# 펜 굵기는 3으로 강조, 기본이 1입니다
t.pensize(3)
# 색상은 초록색
t.color("green")
# 낙하지점으로 이동합니다
t.up()
t.goto(target - 25, 2)
# 초록색으로 그립니다
t.down()
t.goto(target + 25, 2)

# 거북이 색을 검은색으로 지정하고 처음 발사했던 곳으로 되돌립니다
t.color("black")
t.up()
t.goto(-200, 10)
# 발사각도는 20도로 설정합니다
t.setheading(20)

# 거북이가 동작하는 데 필요한 설정을 합니다
# ↑를 누르면 turn_up 함수를 실행합니다
t.onkeypress(turn_up, "Up")      
# ↓를 누르면 turn_down 함수를 실행합니다
t.onkeypress(turn_down, "Down")  
# SpaceBar를 누르면 fire 함수를 실행합니다
t.onkeypress(fire, "space")      
# 거북이 그래픽 창이 키보드 입력을 받도록 합니다
t.listen()  


