import sys 
import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,color,(self.x,self.y,self.w,self.h))

  
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
        
    
    def isMouseOn(self):
        mposX,mposY = pg.mouse.get_pos()
        if self.w+self.x >= mposX and self.x <= mposX and self.y+self.h >= mposY and self.y <= mposY:
            return True
        else:
            return False

    def isMousePress(self):
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    
    if btn.isMouseOn() and btn.isMousePress():
        color = (149, 86, 166)
    elif btn.isMouseOn():
        color = (140, 140, 136)
    else:
        color = (140, 3, 3)

    btn.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด 
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        
        

      
        