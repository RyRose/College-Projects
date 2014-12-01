from tkinter import *
import random
import time
#import winsound
import math

def runPacman():
    root = Tk()
    x = Room(root)
    x.pack()
    root.mainloop()

class Room(Frame):
    lives = 3
    def __init__(self, master):
        Frame.__init__(self, master)

        self.lst = []
        self.foodlst = []
        self.poweruplst = []
        self.allpowerful = 0
        self.still = 0
        self.highScore = 0
        self.starttime = 0
        self.speed = 140
        self.livedisplaylst = []
        
        self.canvas = Canvas(self, width = 600, height = 750, background = 'black')
        self.canvas.grid(row =1, column =0, columnspan = 2)
        self.canvas.bind('<KeyPress>', self.move)
        self.canvas.create_text(300,10, text= 'HIGH     SCORE', fill = 'white', font = 'Arial')         
        self.drawscore = self.canvas.create_text(325, 30, text = '00', font = 'Arial', fill = 'white')
        for i in range(0, 120, 40):
            self.livedisplaylst.append(self.canvas.create_arc(20+i, 710, 50+i, 740, start = 50, extent = 260, fill = 'yellow'))
        self.after(100, self.walls)

    def walls(self):
        self.lst.append(self.draw(5, 50, 600, 60))
        self.lst.append(self.draw(297-10, 50, 297 + 10, 150))
        self.lst.append(self.draw(5,50, 15, 210+50))
        self.lst.append(self.draw(55, 100, 115, 150))
        self.lst.append(self.draw(115+50,100, 287-50, 150))
        self.lst.append(self.draw(55, 200, 115,210))
        self.lst.append(self.draw(5,260, 115, 270))
        self.lst.append(self.draw(357,100,429,150))
        self.lst.append(self.draw(429+50,100,429+50+60,150))
        self.lst.append(self.draw(429+50,200,429+50+60,210))
        self.lst.append(self.draw(590,50,600,210+50))
        self.lst.append(self.draw(429+50+5,260,600,270))
        self.lst.append(self.draw(105,260,115,340))
        self.lst.append(self.draw(429+50,260, 479+10,340))
        self.lst.append(self.draw(115+50,200, 165+10, 340))
        self.lst.append(self.draw(429-10, 200, 429, 340))
        self.lst.append(self.draw(115+110, 200,429-10-50, 220))
        self.lst.append(self.draw(297-10, 200, 297+10,270))
        self.lst.append(self.draw(115+50, 270,297-10-50-10, 280))
        self.lst.append(self.draw(429-10, 270, 429-(297-10-50-10-115-50),280))
        self.lst.append(self.draw(115,340,-50,350))
        self.lst.append(self.draw(115,340+50,-50,350+50))
        self.lst.append(self.draw(429+50,340,650,350))
        self.lst.append(self.draw(429+50,340+50,650,350+50))
        self.lst.append(self.draw(115+50+50+15,330,115+50+50+50,335,3))
        self.lst.append(self.draw(115+50+50+50,330,115+50+50+50+50+4,335,0,'pink'))
        self.lst.append(self.draw(115+50+50+50+50+4,330,115+250-10, 335, 3))
        self.lst.append(self.draw(115+50+50+15,330,115+50+50+20,340+50+10,3))
        self.lst.append(self.draw(115+50+50+15,340+50+10,115+250-5,340+50+10+5,3))
        self.lst.append(self.draw(115+50+50+50+50+50-10,330,115+200+50+5-10, 340+50+10, 3))
        self.lst.append(self.draw(105,340+50,115,340+50+(340-260)))
        self.lst.append(self.draw(429+10+50, 340+50, 429+50, 340+50+(340-260)))
        self.lst.append(self.draw(115+50,340+50,115+50+10,340+50+(340-260)))
        self.lst.append(self.draw(429-10,340+50,429, 470))
        self.lst.append(self.draw(115,470,0,460))
        self.lst.append(self.draw(429+50,470,600,429+40-10))
        self.lst.append(self.draw(115+50+50+15,340+50+10+50+8,115+250-5,340+50+10+5+50+5+8))
        self.lst.append(self.draw(290,458,300,528))
        self.lst.append(self.draw(290-50,520+10,290-50-74,510+10))
        self.lst.append(self.draw(240-50-74-50,520+10,240-50-74-5,510+10))
        self.lst.append(self.draw(5,520-10-50,15,520+50+10+100))
        self.lst.append(self.draw(590,520-10-50,600,520+50+10+100))
        self.lst.append(self.draw(290-50+100+50+40,520+10,290-50-74+100+50+40,510+10))
        self.lst.append(self.draw(240-50-74-50+400+15,520+10,240-50-74-5+400+15,510+10))
        self.lst.append(self.draw(240-50-74-5,520+70,240-50-74-5+10,510+10))
        self.lst.append(self.draw(240-50-74-5-50,520+70, 0, 520+60))
        self.lst.append(self.draw(240-50-74-5-50, 520+70+50,240-50-74-5-50+180, 520+70+50+10))
        self.lst.append(self.draw(240-50-74-5-50+470, 520+70+50,240-50-74-5-50+180+110, 520+70+50+10))
        self.lst.append(self.draw(240-50-74-50+400+15,520+70,240-50-74-40+400+15,510+10))
        self.lst.append(self.draw(240-50-74-50+400+15-60,520+70+50,240-50-74-40+400+15-60,70+510+10))
        self.lst.append(self.draw(240-50-74-50+400+15-60-250,520+70+50,-250 + 240-50-74-40+400+15-60,70+510+10))
        self.lst.append(self.draw(5,520+50+10+100+10,600,520+50+10+100+20))
        self.lst.append(self.draw(240-50-74-5-50+180, 520+70,240-50-74-5-50+180+110, 520+70+10))
        self.lst.append(self.draw(240-50-74-5-50+180 + 50-5+5, 520+70,240-50-74-5-50+180 + 50+5+5, 520 +70 +60))
        self.lst.append(self.draw(600-(240-50-74-5-50),520+70, 600, 520+60))
        self.after(100, self.step2)
        
    def step2(self):      
        self.pacman = Pacman(self.canvas)
        self.ghostlist = (Inky(self.canvas), Blinky(self.canvas), Winky(self.canvas), Clyde(self.canvas))
        self.canvas.bind('<KeyPress>', self.move)
        self.canvas.focus_set()
        self.animateghosts()
        self.animatepacman()
        self.animatepowerups()
        self.after(500, self.textdisplay)
        
    def animatepacman(self): 
        self.pacman.animate()
        if self.allpowerful == 1:
            if 0 < time.time() - self.starttime < 10:
                for i in self.ghostlist:
                    if i.fill == 'dark blue':
                        if math.sqrt((self.pacman.x - i.x)**2 + (self.pacman.y - i.y)**2) < 30:
                            for z in i.id:
                                self.canvas.delete(z)
                            self.highscore(200)
                            i.__init__(self.canvas)
            else:
                for i in self.ghostlist:
                    self.canvas.itemconfig(i.id[0], fill = i.ofill)
                    i.fill = i.ofill
                self.allpowerful = 0
        self.after(300, self.animatepacman)

    def layfood(self):
        self.poweruplst.append(Powerup(self.canvas, 34, 120))
        self.poweruplst.append(Powerup(self.canvas, 557, 120))
        self.poweruplst.append(Powerup(self.canvas, 34, 555))
        self.poweruplst.append(Powerup(self.canvas, 557, 555))
        for i in range(0, 21*12, 21):
            self.foodlst.append(self.drawc(30+i,75))
        for i in range(0, 21*26, 21):
            self.foodlst.append(self.drawc(30+i,664))
        for i in range(0, 21*4, 21):
            self.foodlst.append(self.drawc(30, 664-i))
        for i in range(0, 21*5, 21):
            self.foodlst.append(self.drawc(30, 664-21 *5 -i))
        for i in range(0, 21*4, 21):
            self.foodlst.append(self.drawc(30+21+i, 664-21 *9 + 15 ))
        for i in range(0, 21*6, 21):
            self.foodlst.append(self.drawc(30+21*6+i, 664-21 *9 + 15 ))
        for i in range(0, 21*6, 21):
            self.foodlst.append(self.drawc(30+21*14+i, 664-21 *9 + 15 ))
        for i in range(0, 21*4, 21):
            self.foodlst.append(self.drawc(30+21*21+i, 664-21 *9 + 15 ))
        for i in range(0, 21*2, 21):
            self.foodlst.append(self.drawc(30+21+8+i, 664-21 *9 + 15 + 60 ))
        for i in range(0, 21 *2, 21):
            self.foodlst.append(self.drawc(30+21+8+21*1, 664-21*9 +15 +60+i+21))
        for i in range(0, 21 *2, 21):
            self.foodlst.append(self.drawc(30+21+8+21*7, 664-21*9 +15 +60+i+21))
        for i in range(0, 21 *2, 21):
            self.foodlst.append(self.drawc(30+21+8+21*10-10, 664-21*9 +15+i+20))
        for i in range(0, 21 *2, 21):
            self.foodlst.append(self.drawc(30+21+8+21*10-10, 664-21*9 +15+i+80+20+35))
        for i in range(0, 21 *2, 21):
            self.foodlst.append(self.drawc(30+21+8+21*10-10+65, 664-21*9 +15+i+20))
        for i in range(0, 21 *2, 21):
            self.foodlst.append(self.drawc(30+21+8+21*10-10+65, 664-21*9 +15+i+20+80+35))
        for i in range(0, 21 *2, 21):
            self.foodlst.append(self.drawc(30+21+8+21*15, 664-21*9 +15 +60+i+21))
        for i in range(0, 21 *2, 21):
            self.foodlst.append(self.drawc(30+21+8+21*22-10, 664-21*9 +15 +60+i+21))
        for i in range(0, 21*14, 21):
            self.foodlst.append(self.drawc(30+21+8+i+100, 664-21 *9 + 15 + 60 ))
        for i in range(0, 21*2, 21):
            self.foodlst.append(self.drawc(30+21+8+i+100 + 21*16 +15 , 664-21 *9 + 15 + 60 ))
        for i in range(0, 21*4, 21):
            self.foodlst.append(self.drawc(30+21+2+i, 664-21 *9 + 15 + 60 +60))
        for i in range(0, 21*4, 21):
            self.foodlst.append(self.drawc(30+21+2+i+ 21*7, 664-21 *9 + 15 + 60 +60))
        for i in range(0, 21*4, 21):
            self.foodlst.append(self.drawc(30+21+2+i+ 21*13, 664-21 *9 + 15 + 60 +60))
        for i in range(0, 21*4, 21):
            self.foodlst.append(self.drawc(30+21+2+i+ 21*20, 664-21 *9 + 15 + 60 +60))
        for i in range(0, 21*4, 21):
            self.foodlst.append(self.drawc(30 + 21 * 25, 664-i))
        for i in range(0, 21*5, 21):
            self.foodlst.append(self.drawc(30 + 21 * 25, 664-21*5 - i))
        for i in range(0,21*4, 21):
            self.foodlst.append(self.drawc(30 + i + 21, 65 + 21 *5))
        for i in range(0,21*4, 21):
            self.foodlst.append(self.drawc(30 + i + 21, 65 + 21 *5+ 60))
        for i in range(0,21*4, 21):
            self.foodlst.append(self.drawc(30 + i + 21*8, 65 + 21 *5+ 70))
        for i in range(0,21*3, 21):
            self.foodlst.append(self.drawc(30 + 21*8, 65 + 21 *5+ 70-i))
        for i in range(0,21*4, 21):
            self.foodlst.append(self.drawc(30 + i + 21*14, 65 + 21 *5+ 70))
        for i in range(0,21*2, 21):
            self.foodlst.append(self.drawc(30 + 21*3 + 21*14, 65 + 21 *5+ 70-i -21))
        for i in range(0,21*5, 21):
            self.foodlst.append(self.drawc(30 + i + 21 + 21*5, 65 + 21 *5))
        for i in range(0,21*2, 21):
            self.foodlst.append(self.drawc(30 + i + 21 + 21*11, 65 + 21 *5))
        for i in range(0,21*5, 21):
            self.foodlst.append(self.drawc(30 + i + 21 + 21*14, 65 + 21 *5))
        for i in range(0,21*4, 21):
            self.foodlst.append(self.drawc(30 + i + 21 + 21*20, 65 + 21 *5))
        for i in range(0,21*4, 21):
            self.foodlst.append(self.drawc(30 + i + 21 + 21*20, 65 + 21 *5 + 60)) 
        for i in range(0, 21*5, 21):
            self.foodlst.append(self.drawc(30 + 21*11, 75+i+21))
        for i in range(0, 21*9, 21):
            self.foodlst.append(self.drawc(30,75+i))
        for i in range(0, 21*26, 21):
            self.foodlst.append(self.drawc(30 + 5*21, 75+21 + i))
        for i in range(0, 21*12, 21):
            self.foodlst.append(self.drawc(30 + 14*21 + i, 75))
        for i in range(0, 21*6, 21):
            self.foodlst.append(self.drawc(30+ 14 *21, 75 +i))
        for i in range(0, 21*26, 21):
            self.foodlst.append(self.drawc(30 + 20 *21, 75 +i+21))
        for i in range(0, 21* 8, 21):
            self.foodlst.append(self.drawc(30 + 25 *21, 75 + i+21))

    def reset(self):
        self.speed //= 1.4
        self.canvas.delete(self.text)
        Ghost.disabled = 0
        self.count = 0
        self.layfood()
        self.pacman.x = 300
        self.pacman.y = 430
        
        for i in self.ghostlist:
            for z in i.id:
                self.canvas.delete(z)
        for i in self.ghostlist:
                i.__init__(self.canvas)
        Ghost.disabled = 1
        self.stopmovement = 1

    def textdisplay(self):
        self.text = self.canvas.create_text( 300, 430, text= 'READY!', fill = 'yellow', font ='Arial')
        self.after(500, self.playthebeginmusicsound)

    def playthebeginmusicsound(self):
       # winsound.PlaySound('begin.wav', winsound.SND_FILENAME)
        self.reset()
        
    def move(self, event):
        if Ghost.disabled == 1:
            if self.stopmovement == 1:
                for i in self.ghostlist:
                    if i.fill != 'dark blue':
                        if math.sqrt((self.pacman.x - i.x)**2 + (self.pacman.y - i.y)**2) < 30:
                            self.lives -= 1
                            if self.lives < 0:
                                self.canvas.delete(ALL)
                                self.canvas.create_text(300, 300, text = 'Game Over!\nYou have a score of ' + str(self.highScore) +'\nRestart the program to play again!', fill = 'white')
                                Ghost.disabled = 0
                                self.canvas.delete(self.pacman.id)
                                for i in self.ghostlist:
                                    for z in i.id:
                                        self.canvas.delete(z)
                            else:
                                self.speed *= 1.4
                                Ghost.disabled = 0
                                self.canvas.delete(self.livedisplaylst.pop())
                                for i in self.foodlst:
                                    self.canvas.delete(i)
                                    self.foodlst = []
                                for i in self.poweruplst:
                                    self.canvas.delete(i.id)
                                    self.poweruplst = []
                                self.textdisplay()
                                self.stopmovement = 0
                                
            for i in self.foodlst:
                if math.sqrt((self.pacman.x - self.canvas.coords(i)[0])**2 + (self.pacman.y - self.canvas.coords(i)[1])**2) <= 30:
                    self.canvas.delete(i)
                    self.foodlst.remove(i)
                    self.count += 1
                    self.highscore()
            for i in self.poweruplst:
                if math.sqrt((self.pacman.x - self.canvas.coords(i.id)[0])**2 + (self.pacman.y - self.canvas.coords(i.id)[1])**2) <= 30:
                    self.canvas.delete(i.id)
                    self.poweruplst.remove(i)
                    self.count += 1
                    self.highscore(50)
                    self.becomeallpowerful()
            if event.keysym == 'Left':
                if len(self.canvas.find_overlapping(self.pacman.x, self.pacman.y, self.pacman.x - 20, self.pacman.y)) < 2 or self.canvas.find_overlapping(self.pacman.x, self.pacman.y, self.pacman.x - 20, self.pacman.y)[0] not in range(5,61):
                    self.pacman.x -= 5
                    self.canvas.move(self.pacman.id, -5,0)
                if self.pacman.x +15 < 0:
                    self.pacman.x += 630
                    self.canvas.move(self.pacman.id,630,0)
                self.pacman.start = 210
                self.pacman.extent = 300
            elif event.keysym == 'Right':
                if len(self.canvas.find_overlapping(self.pacman.x, self.pacman.y, self.pacman.x + 20, self.pacman.y)) < 2 or self.canvas.find_overlapping(self.pacman.x, self.pacman.y, self.pacman.x + 20, self.pacman.y)[0] not in range(5,61):    
                    self.pacman.x += 5
                    self.canvas.move(self.pacman.id, 5,0)
                if self.pacman.x-15 > 600:
                    self.pacman.x -= 630
                    self.canvas.move(self.pacman.id, -630, 0)
                self.pacman.start = 30
                self.pacman.extent =300
            elif event.keysym == 'Up':
                if len(self.canvas.find_overlapping(self.pacman.x, self.pacman.y, self.pacman.x, self.pacman.y-20)) < 2 or self.canvas.find_overlapping(self.pacman.x, self.pacman.y, self.pacman.x , self.pacman.y -20)[0] not in range(5,61):    
                    self.pacman.y -= 5
                    self.canvas.move(self.pacman.id, 0, -5)
                self.pacman.start = 120
                self.pacman.extent = 300
            elif event.keysym == 'Down':
                if len(self.canvas.find_overlapping(self.pacman.x, self.pacman.y, self.pacman.x, self.pacman.y+20)) < 2 or self.canvas.find_overlapping(self.pacman.x, self.pacman.y, self.pacman.x , self.pacman.y+20)[0] not in range(5,61):    
                    self.pacman.y += 5
                    self.canvas.move(self.pacman.id, 0, 5)
                self.pacman.start = 300
                self.pacman.extent =300
            else:
                print('Sorry, you must use the arrow keys.')
            
    def animatepowerups(self):
        for i in self.poweruplst:
            i.animate()
        self.after(300, self.animatepowerups)
        
    def animateghosts(self):
        for i in self.ghostlist:
            x= i.animate(self.pacman, self.canvas)
            if x=='up':
                for z in i.id:
                    self.canvas.move(z, 0, -4)
                i.y -= 4
            elif x == 'down':
                for z in i.id:
                    self.canvas.move(z, 0, 4)
                i.y += 4
            elif x == 'right':
                for z in i.id:
                    self.canvas.move(z, 4, 0)
                i.x += 4
            elif x == 'left':
                for z in i.id:
                    self.canvas.move(z, -4, 0)
                i.x -= 4
        self.after(int(self.speed), self.animateghosts)
            
    def drawc(self, x,y):
        return self.canvas.create_oval(x, y, x+10, y+10, fill = 'yellow')
    
    def draw(self,x,y,x2,y2, width = 4, fill = 'black'):
        return self.canvas.create_rectangle(x, y, x2, y2, width = width, fill = fill, outline = 'blue')

    def highscore(self, score = 10):
        self.highScore += score
        self.canvas.delete(self.drawscore)
        self.drawscore = self.canvas.create_text(325, 30, text = str(self.highScore), font = 'Arial', fill = 'white')
        if self.count == 263:            
            self.textdisplay()

    def becomeallpowerful(self):
        self.allpowerful = 1
        for i in self.ghostlist:
            i.fill = 'dark blue'
            self.canvas.itemconfig(i.id[0], fill = 'dark blue')
        self.starttime = time.time()
        
class Pacman(Frame):
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 300
        self.y = 300
        self.id = self.canvas.create_arc(self.x- 20,self.y -20, self.x + 20, self.y + 20, start = 30, extent =300, fill = 'yellow')
        self.dir = 0
        self.start = 0
        self.extent = 0
        
    def animate(self):
        self.canvas.delete(self.id)
        if self.dir == 0:
            self.id =self.canvas.create_arc(self.x- 20,self.y -20, self.x + 20, self.y + 20, start = self.start-10, extent =self.extent+20, fill = 'yellow')
            self.dir = 1
        else:
            self.id =self.canvas.create_arc(self.x- 20,self.y -20, self.x + 20, self.y + 20, start = self.start + 30, extent =self.extent - 60, fill = 'yellow')
            self.dir = 0
            
class Ghost:
    disabled = 0
    def __init__(self, canvas):
        self.prev = 'left'
        self.canvas = canvas
        self.x = 400
        self.y = 300
        self.id = (self.canvas.create_polygon(self.x ,self.y - 15, self.x + 15, self.y - 8, self.x+ 15, self.y+15, self.x + 7.5, self.y + 7, self.x, self.y + 15, self.x-7.5, self.y + 7, self.x -15, self.y +15, self.x - 15, self.y -7.5, fill = 'light blue', outline = 'purple'), self.canvas.create_oval(self.x-10, self.y - 6, self.x - 2, self.y, fill = 'white'),self.canvas.create_oval(self.x+10, self.y - 6, self.x + 2, self.y, fill = 'white', state = DISABLED))

    def animate(self, pacman, canvas):
        if Ghost.disabled ==1:
            oup = list(canvas.find_overlapping(self.x, self.y, self.x, self.y-35))
            oleft = list(canvas.find_overlapping(self.x, self.y, self.x-35, self.y))
            oright = list(canvas.find_overlapping(self.x, self.y, self.x+35, self.y))
            odown = list(canvas.find_overlapping(self.x, self.y, self.x, self.y+35))
            up,left,right,down = [],[],[],[]
            distances = []
            randomdirlist = []
            for x in oup:
                if x < 62:
                    up.append(x)
            for x in odown:
                if x < 62:
                    down.append(x)
            for x in oleft:
                if x < 62:
                    left.append(x)
            for x in oright:
                if x < 62:
                    right.append(x)    

            if self.prev == 'up':
                if len(left) <1 or len(right) < 1:
                    if len(right) < 1:
                        randomdirlist.append('right')
                        distances.append({self.distance(50, 0, pacman):'right'})
                    if len(left) < 1:
                        randomdirlist.append('left')
                        distances.append({self.distance(-50, 0, pacman):'left'})
                    if len(up) < 1:
                        randomdirlist.append('up')
                        distances.append({self.distance(0,-50, pacman):'up'})
                    dir = random.randint(0,1)
                    if dir:
                        self.prev = random.choice(randomdirlist)
                        return self.prev
                    else:           
                        self.prev = self.least(distances)
                        return self.prev
                return self.prev
                
            elif self.prev == 'down':
                if len(left) <1 or len(right) < 1:
                    if len(right) < 1:
                        randomdirlist.append('right')
                        distances.append({self.distance(50, 0, pacman):'right'})
                    if len(left) < 1:
                        randomdirlist.append('left')
                        distances.append({self.distance(-50, 0, pacman):'left'})
                    if len(down) < 1:
                        randomdirlist.append('down')
                        distances.append({self.distance(0,50, pacman):'down'})
                    dir = random.randint(0,1)
                    if dir:
                        self.prev = random.choice(randomdirlist)
                        return self.prev
                    else:           
                        self.prev = self.least(distances)
                        return self.prev
                return self.prev
                
            elif self.prev == 'left':
                if len(up) <1 or len(down) < 1:
                    if len(left) < 1:
                        randomdirlist.append('left')
                        distances.append({self.distance(-50, 0, pacman):'left'})
                    if len(up) < 1:
                        randomdirlist.append('up')
                        distances.append({self.distance(0,-50, pacman):'up'})
                    if len(down) < 1:
                        randomdirlist.append('down')
                        distances.append({self.distance(0,50, pacman):'down'})
                    dir = random.randint(0,1)
                    if dir:
                        self.prev = random.choice(randomdirlist)
                        return self.prev
                    else:           
                        self.prev = self.least(distances)
                        return self.prev
                return self.prev
            
            elif self.prev == 'right':
                if len(up) <1 or len(down) < 1:
                    if len(right) < 1:
                        randomdirlist.append('right')
                        distances.append({self.distance(50, 0, pacman):'right'})
                    if len(up) < 1:
                        randomdirlist.append('up')
                        distances.append({self.distance(0,-50, pacman):'up'})
                    if len(down) < 1:
                        randomdirlist.append('down')
                        distances.append({self.distance(0,50, pacman):'down'})
                    dir = random.randint(0,1)
                    if dir:
                        self.prev = random.choice(randomdirlist)
                        return self.prev
                    else:
                        self.prev = self.least(distances)
                        return self.prev
                return self.prev            
                                
    def least(self, dictionary):
        leastone = 1000000
        for i in dictionary:
            if list(i.keys())[0] < leastone:
                leastone = list(i.keys())[0]
                direction = list(i.values())[0]
        return direction

    def distance(self, x, y, pacman):
        return math.sqrt(((self.x  + x - pacman.x)**2 + (self.y + y - pacman.y)**2))

    def becomeallpowerfulbeing(self):
        self.starttime = time.time()
        
        
class Winky(Ghost):
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 295
        self.y = 370
        self.prev = 'left'
        self.ofill = 'light blue'
        self.fill= 'light blue'
        self.id = (self.canvas.create_polygon(self.x ,self.y - 15, self.x + 15, self.y - 8, self.x+ 15, self.y+15, self.x + 7.5, self.y + 7, self.x, self.y + 15, self.x-7.5, self.y + 7, self.x -15, self.y +15, self.x - 15, self.y -7.5, fill = 'light blue'), self.canvas.create_oval(self.x-10, self.y - 6, self.x - 2, self.y, fill = 'white'),self.canvas.create_oval(self.x+10, self.y - 6, self.x + 2, self.y, fill = 'white'))

class Inky(Ghost):
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 295
        self.y = 370
        self.prev = 'left'
        self.ofill = 'red'
        self.fill = 'red'
        self.id = (self.canvas.create_polygon(self.x ,self.y - 15, self.x + 15, self.y - 8, self.x+ 15, self.y+15, self.x + 7.5, self.y + 7, self.x, self.y + 15, self.x-7.5, self.y + 7, self.x -15, self.y +15, self.x - 15, self.y -7.5, fill = 'red'), self.canvas.create_oval(self.x-10, self.y - 6, self.x - 2, self.y, fill = 'white'),self.canvas.create_oval(self.x+10, self.y - 6, self.x + 2, self.y, fill = 'white'))

class Blinky(Ghost):
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 295
        self.y = 370
        self.fill = 'pink'
        self.ofill = 'pink'
        self.prev = 'left'
        self.id = (self.canvas.create_polygon(self.x ,self.y - 15, self.x + 15, self.y - 8, self.x+ 15, self.y+15, self.x + 7.5, self.y + 7, self.x, self.y + 15, self.x-7.5, self.y + 7, self.x -15, self.y +15, self.x - 15, self.y -7.5, fill = 'pink'), self.canvas.create_oval(self.x-10, self.y - 6, self.x - 2, self.y, fill = 'white'),self.canvas.create_oval(self.x+10, self.y - 6, self.x + 2, self.y, fill = 'white'))

class Clyde(Ghost):
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 295
        self.y = 370
        self.prev = 'left'
        self.ofill = 'orange'
        self.fill = 'orange'
        self.id = (self.canvas.create_polygon(self.x ,self.y - 15, self.x + 15, self.y - 8, self.x+ 15, self.y+15, self.x + 7.5, self.y + 7, self.x, self.y + 15, self.x-7.5, self.y + 7, self.x -15, self.y +15, self.x - 15, self.y -7.5, fill = 'orange'), self.canvas.create_oval(self.x-10, self.y - 6, self.x - 2, self.y, fill = 'white'),self.canvas.create_oval(self.x+10, self.y - 6, self.x + 2, self.y, fill = 'white'))

class Powerup:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.id = self.canvas.create_oval(self.x-15, self.y-15, self.x+15, self.y+15, fill = 'yellow')
        self.choice = 1
        
    def animate(self):
        self.canvas.delete(self.id)
        if self.choice == 1:
            self.id = self.canvas.create_oval(self.x-10, self.y-10, self.x+10, self.y+10, fill = 'yellow')
            self.choice = 0
        elif self.choice == 0:
            self.id = self.canvas.create_oval(self.x-15, self.y-15, self.x+15, self.y+15, fill ='yellow')
            self.choice = 1

runPacman()
