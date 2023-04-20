import sys 
import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(150, 210, 217),(self.x,self.y,self.w,self.h))
    
    def setx(self,x=0):
        self.x = x
    def getx(self):
        return self.x
    
    def sety(self,y=0):
        self.y = y
    def gety(self):
        return self.y

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
box = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    box.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม w
            box.setx(box.getx()+1)
            print("Key w down")
        if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม a
            box.setx(box.getx()-1)
            print("Key a up") 
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม s
            box.sety(box.gety()+5)
            print("Key s down")
        if event.type == pg.KEYUP and event.key == pg.K_d: #ปุ่มถูกปล่อยและเป็นปุ่ม d
            box.sety(box.gety()-5)
            print("Key d up") 