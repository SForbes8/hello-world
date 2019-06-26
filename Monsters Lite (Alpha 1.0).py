#Version Alpha 1.0
#Launching before AGF2019
#Will contain the first four league battles and should be stable.
#Not intended for AGF2019 use. Use a later version.
from tkinter import *
from random import *
from time import sleep
import msvcrt
file = 0
data = 0
food = 5
movedir = 0
Selected = False
seconds = float(0)
fp = 0
tp = 0
cp = 0
a = 20
b = 0
train = 0
death = False
level = 1
decision = ''
print ('Version pre-alpha 1.0 launching...')
while file != 1 and file != 2 and file!= 3 and file != 4:
    file = int(input('File number? (1-4) '))
    openf = input('Opening or creating (O/C)')
if openf == 'c' or openf == 'C':
    if file == 1: data = open("mfile1.txt","w")
    if file == 2: data = open("mfile2.txt","w")
    if file == 3: data = open("mfile3.txt","w")
    if file == 4: data = open("mfile4.txt","w")
    data.write("31")
    data.close()
    hp = 31
if openf == 'o' or openf == 'O':
    if file == 1: data = open("mfile1.txt","r")
    if file == 2: data = open("mfile2.txt","r")
    if file == 3: data = open("mfile3.txt","r")
    if file == 4: data = open("mfile4.txt","r")
    hp = int(data.read())
    data.close()
window = Tk()
window.title('Monsters lite')
c = Canvas(window,height=2000,width=2000,bg='skyblue1')
c.pack()
window.update()
mouth1 = c.create_rectangle(0,0,300,100,fill="green",outline="green")
mouth2 = c.create_rectangle(0,0,100,100,fill="green",outline="green")
mouth3 = c.create_rectangle(0,0,100,100,fill="green",outline="green")
eye1 = c.create_rectangle(0,0,100,200,fill="black")
eye2 = c.create_rectangle(0,0,100,200,fill="black")
c.move(eye1, 300,50)
c.move(eye2, 500,50)
c.move(mouth1,300,550)
c.move(mouth2,200,450)
c.move(mouth3,600,450)
height = (window.winfo_height())
def mapa(event):
    global movedir,decision
    if event.keysym == 'Right':
        movedir = 1
    elif event.keysym == 'Left':
        movedir = 2
    elif event.keysym == 'Up':
        movedir = 3
    elif event.keysym == 'Down':
        movedir = 4
    else:
        movedir = 0
    if event.keysym == 'F' or event.keysym == 'f':
        decision = 'F'
    if event.keysym == 'T' or event.keysym == 't':
        decision = 'T'
    if event.keysym == 'C' or event.keysym == 'c':
        decision = 'C'
c.bind_all('<Key>', mapa)
def comp(a):
    b = str(a)
    d = b.split(" ")
    global cp,tp,fp,level
    fp = int(d[0])
    tp = int(d[1])
    cp = int(d[2])
    level = int(d[3])
if file == 1:
    if openf == 'C' or openf == 'c':
        data = open("mfile1a.txt","w")
        name = input('Monster name?')
        data.write(name)
        data.close()
        data = open("mfile1b.txt","w")
        data.write("5")
        food = 5
        data.close()
        data = open("mfile1c.txt","w")
        data.write("00 00 00 1")
        data.close()
    if openf == 'O' or openf == 'o':
        data = open("mfile1a.txt","r")
        name = data.read()
        data.close()
        data = open("mfile1b.txt","r")
        food = int(data.read())
        data.close()
        data = open("mfile1c.txt","r")
        dataa = data.read()
        comp(dataa)
        data.close()
if file == 2:
    if openf == 'C' or openf == 'c':
        data = open ("mfile2a.txt","w")
        name = input('Monster name?')
        data.write(name)
        data.close()
        data = open("mfile2b.txt","w")
        data.write("5")
        food = 5
        data.close()
    if openf == 'O' or openf == 'o':
        data = open("mfile2a.txt","r")
        name = data.read()
        data.close()
        data = open("mfile2b.txt","r")
        food = int(data.read())
        data.close()
if file == 3:
    if openf == 'C' or openf == 'c':
        data = open ("mfile3a.txt","w")
        name = input('Monster name?')
        data.write(name)
        data.close()
        data = open("mfile3b.txt","w")
        data.write("5")
        food = 5
        data.close()
    if openf == 'O' or openf == 'o':
        data = open("mfile3a.txt","r")
        name = data.read()
        data.close()
        data = open("mfile3b.txt","r")
        food = int(data.read())
        data.close()
if file == 4:
    if openf == 'C' or openf == 'c':
        data = open ("mfile4a.txt","w")
        name = input('Monster name?')
        data.write(name)
        data.close()
        data = open("mfile4b.txt","w")
        data.write("5")
        food = 5
        data.close()
    if openf == 'O' or openf == 'o':
        data = open("mfile4a.txt","r")
        name = data.read()
        data.close()
        data = open("mfile4b.txt","r")
        food = int(data.read())
        data.close()
print ('Your monster is called',name, '.')

def updatemon(hp,oldhp):
    if oldhp > 20:
        if hp < 21 and oldhp > 10:
            c.move(mouth2,0,100)
            c.move(mouth3,0,100)
            c.itemconfig(mouth2,fill="yellow")
            c.itemconfig(mouth1,fill="yellow")
            c.itemconfig(mouth3,fill="yellow")
            c.itemconfig(mouth2,outline="yellow")
            c.itemconfig(mouth1,outline="yellow")
            c.itemconfig(mouth3,outline="yellow")
        if hp < 11:
            c.move(mouth2,0,200)
            c.move(mouth3,0,200)
            c.itemconfig(mouth1,fill="red")
            c.itemconfig(mouth2,fill="red")
            c.itemconfig(mouth3,fill="red")
            c.itemconfig(mouth1,outline="red")
            c.itemconfig(mouth2,outline="red")
            c.itemconfig(mouth3,outline="red")
    if oldhp < 21 and oldhp > 10:
        if hp > 20:
            c.move(mouth2,0,-100)
            c.move(mouth3,0,-100)
            c.itemconfig(mouth2,fill="green")
            c.itemconfig(mouth1,fill="green")
            c.itemconfig(mouth3,fill="green")
            c.itemconfig(mouth2,outline="green")
            c.itemconfig(mouth1,outline="green")
            c.itemconfig(mouth3,outline="green")
        if hp < 11:
            c.move(mouth2,0,100)
            c.move(mouth3,0,100)
            c.itemconfig(mouth1,fill="red")
            c.itemconfig(mouth2,fill="red")
            c.itemconfig(mouth3,fill="red")
            c.itemconfig(mouth1,outline="red")
            c.itemconfig(mouth2,outline="red")
            c.itemconfig(mouth3,outline="red")
    if oldhp < 11:
        if hp > 20:
            c.move(mouth2,0,-200)
            c.move(mouth3,0,-200)
            c.itemconfig(mouth2,fill="green")
            c.itemconfig(mouth1,fill="green")
            c.itemconfig(mouth3,fill="green")
            c.itemconfig(mouth2,outline="green")
            c.itemconfig(mouth1,outline="green")
            c.itemconfig(mouth3,outline="green")
        if hp < 21 and hp > 10:
            c.move(mouth2,0,-100)
            c.move(mouth3,0,-100)
            c.itemconfig(mouth2,fill="yellow")
            c.itemconfig(mouth1,fill="yellow")
            c.itemconfig(mouth3,fill="yellow")
            c.itemconfig(mouth2,outline="yellow")
            c.itemconfig(mouth1,outline="yellow")
            c.itemconfig(mouth3,outline="yellow")
updatemon(hp,31)
if height > 800:
    menua = c.create_text(350,800,text='<')
    menub = c.create_text(400,800,text='Feed (Food = '+str(food)+')')
    menuc = c.create_text(450,800,text='>')
else:
    menua = c.create_text(800,350,text='<')
    menub = c.create_text(850,350,text='Feed (Food = '+str(food)+')')
    menuc = c.create_text(900,350,text='>')
menupos = 1
menu = True
def Select(event=None):
    global Selected
    Selected = True
window.bind('<space>', Select)
def save():
    if file == 1:
        data = open("mfile1.txt","w")
        data.write(str(hp))
        data.close()
        data = open("mfile1a.txt","w")
        data.write(name)
        data.close()
        data = open("mfile1b.txt","w")
        data.write(str(food))
        data.close()
        data = open("mfile1c.txt","w")
        if fp < 10:
            fpstring = '0'+str(fp)
        else:
            fpstring = str(fp)
        if tp < 10:
            tpstring = '0'+str(tp)
        else:
            tpstring = str(tp)
        if cp < 10:
            cpstring = '0'+str(cp)
        else:
            cpstring = str(cp)
        levelstring = str(level)
        finalstring = fpstring + ' ' + tpstring + ' ' + cpstring + ' ' + levelstring
        data.write(finalstring)
        data.close()
    if file == 2:
        data = open ("mfile2a.txt","w")
        data.write(name)
        data.close()
        data = open("mfile2b.txt","w")
        data.write(str(food))
        data.close()
    if file == 3:
        data = open ("mfile3a.txt","w")
        data.write(name)
        data.close()
        data = open("mfile3b.txt","w")
        data.write(str(food))
        data.close()
    if file == 4:
        data = open ("mfile4a.txt","w")
        data.write(name)
        data.close()
        data = open("mfile4b.txt","w")
        data.write(str(food))
        data.close()
hpdisplay = c.create_text(500,100,text=name+'\'s hp is '+str(hp))
def feed():
    global food,hp
    starthp = hp
    food = int(food)
    if food != 0:
        food -= 1
        hp += 10
        if hp > 31:
            hp = 31
        recovered = hp - starthp
        if recovered != 0: fed = c.create_text(800,600,text='Monster ate the food and recovered '+str(recovered)+' hp!')
        else: fed = c.create_text(800,600,text='Monster ate the food, but recovered no hp as he was already full.')
        window.update()
        sleep(2)
        c.delete(fed)
    else:
        fed = c.create_text(800,600,text='You have no food left.')
        window.update()
        sleep(2)
        c.delete(fed)
def Train():
    global fp,tp,cp,hp,a,b,train
    if a != 100:
        c.delete(train)
    type = randint(0,2)
    if type == 0: traintype = ' fighting power!'
    if type == 1: traintype = ' trick ability!'
    if type == 2: traintype = ' coolness!'
    train = c.create_text(400,690,text='Monster trained its'+traintype)
    if height < 800:
        c.move(train,450,-450)
    if type == 0:
        fp += 1
    if type == 1:
        tp += 1
    if type == 2:
        cp += 1
    hp -= 2
    updatemon(hp,hp+2)
    window.update()
    a = 0
    b = 1
def Minigame():
    c.move(menua,10000,0)
    c.move(menub,10000,0)
    c.move(menuc,10000,0)
    c.move(eye1,10000,0)
    c.move(eye2,10000,0)
    c.move(mouth1,10000,0)
    c.move(mouth2,10000,0)
    c.move(mouth3,10000,0)
    c.move(hpdisplay,10000,0)
    c.move(menua,10000,0)
    c.move(menub,10000,0)
    c.move(menuc,10000,0)
    catchera = c.create_rectangle(0,0,60,40,fill='white')
    catcherb = c.create_rectangle(20,0,40,20,fill='skyblue1')
    window.update()
    end = False
    c.move(catchera,200,650)
    c.move(catcherb,200,650)
    global minigame,movedir
    minigame = True
    catcherpos = 200
    foodexists = False
    foodquantity = 0
    foodY = 200
    foodfallen = 0
    while end != True:
        if movedir == 1 and catcherpos <= 350:
            c.move(catchera,50,0)
            c.move(catcherb,50,0)
            catcherpos += 50
        if movedir == 2 and catcherpos >= 250:
            c.move(catchera,-50,0)
            c.move(catcherb,-50,0)
            catcherpos -= 50
        if foodexists == True:
            foodY += 50
            c.move(fooda,0,50)
            window.update()
            sleep(0.25)
        if foodY >= 600:
            foodexists = False
            c.delete(fooda)
            if foodpos == catcherpos:
                foodquantity += 1
            foodfallen += 1
            if foodfallen == 5:
                break
        if foodexists == False:
            foodpos = (50*randint(1,5))+150
            fooda = c.create_rectangle(foodpos+20,200,foodpos+40,240,fill='green')
            foodexists = True
            foodY = 200
        movedir = 0
        window.update()
    global food
    food += foodquantity
    sleep(0.1)
    minigame = False
    c.delete(catchera,catcherb)
    c.move(menua,-10000,0)
    c.move(menub,-10000,0)
    c.move(menuc,-10000,0)
    c.move(eye1,-10000,0)
    c.move(eye2,-10000,0)
    c.move(mouth1,-10000,0)
    c.move(mouth2,-10000,0)
    c.move(mouth3,-10000,0)
    c.move(hpdisplay,-10000,0)
    c.move(menua,-10000,0)
    c.move(menub,-10000,0)
    c.move(menuc,-10000,0)
def world():
    global fp,cp,tp,level
    if level == 1:
        tutorial = True
    else:
        tutorial = False
    c.move(menua,10000,0)
    c.move(menub,10000,0)
    c.move(menuc,10000,0)
    c.move(eye1,10000,0)
    c.move(eye2,10000,0)
    c.move(mouth1,10000,0)
    c.move(mouth2,10000,0)
    c.move(mouth3,10000,0)
    c.move(hpdisplay,10000,0)
    c.move(menua,10000,0)
    c.move(menub,10000,0)
    c.move(menuc,10000,0)
    #Coding for world (if a new thing), then return below
    c.move(menua,-10000,0)
    c.move(menub,-10000,0)
    c.move(menuc,-10000,0)
    c.move(eye1,-10000,0)
    c.move(eye2,-10000,0)
    c.move(mouth1,-10000,0)
    c.move(mouth2,-10000,0)
    c.move(mouth3,-10000,0)
    c.move(hpdisplay,-10000,0)
    c.move(menua,-10000,0)
    c.move(menub,-10000,0)
    c.move(menuc,-10000,0)
def league():
    global fp,cp,tp,level,hp,decision
    if level == 1:
        tutorial = True
    else:
        tutorial = False
    c.move(menua,10000,0)
    c.move(menub,10000,0)
    c.move(menuc,10000,0)
    c.move(eye1,10000,0)
    c.move(eye2,10000,0)
    c.move(mouth1,10000,0)
    c.move(mouth2,10000,0)
    c.move(mouth3,10000,0)
    c.move(hpdisplay,10000,0)
    c.move(menua,10000,0)
    c.move(menub,10000,0)
    c.move(menuc,10000,0)
    ohp = hp
    if tutorial == True:
        exit = False
        text = c.create_text(400,350,text='Welcome to league mode! Here you put your monster\'s skills to the test in the league against other monsters!')
        for i in range(30):
            sleep(0.1)
            window.update()
        c.delete(text)
        if fp == 0:
            text = c.create_text(400,350,text='But it looks like your monster has no fighting power... Use the train mode to train your monster\'s three stats!')
            for i in range(30):
                sleep(0.1)
                window.update()
            c.delete(text)
            exit = True
        if exit != True:
            text = c.create_text(400,350,text='You\'ve already trained your monster! Let\'s get started in the league!')
            for i in range(30):
                sleep(0.1)
                window.update()
            c.delete(text)
            text = c.create_text(400,350,text='The first thing: your monster has three stats, Fighting Power (FP), Trick Ability (TP) and Coolness in battle (CP)!')
            for i in range(30):
                sleep(0.1)
                window.update()
            c.delete(text)
            text = c.create_text(400,150,text='Let\'s get right into a battle, I will show you how it works!')
            Mon1 = list()
            Mon1.append(c.create_rectangle(300,300,400,400,fill='white',outline='black'))
            Mon1.append(c.create_rectangle(330,320,340,340,fill='black'))
            Mon1.append(c.create_rectangle(360,320,370,340,fill='black'))
            Mon1.append(c.create_rectangle(320,370,330,380,fill='green'))
            Mon1.append(c.create_rectangle(370,370,380,380,fill='green'))
            Mon1.append(c.create_rectangle(330,380,370,390,fill='green'))
            Mon2 = list()
            Mon2.append(c.create_rectangle(600,300,700,400,fill='blue',outline='black'))
            Mon2.append(c.create_rectangle(630,320,640,340,fill='black'))
            Mon2.append(c.create_rectangle(660,320,670,340,fill='black'))
            Mon2.append(c.create_rectangle(620,390,630,400,fill='red'))
            Mon2.append(c.create_rectangle(670,390,680,400,fill='red'))
            Mon2.append(c.create_rectangle(630,380,670,390,fill='red'))
            ehp = 10
            etp = 1
            ecp = 1
            efp = 1
            if hp <= 20:
                if hp <= 10:
                    for i in range(3):
                        c.itemconfig(Mon1[i+3],fill='red')
                    c.move(Mon1[3],0,20)
                    c.move(Mon1[4],0,20)
                else:
                    for i in range(3):
                        c.itemconfig(Mon1[i+3],fill='yellow')
                    c.move(Mon1[3],0,10)
                    c.move(Mon1[4],0,10)
            text2 = c.create_text(350,420,text=(str(hp)+' hp'))
            text3 = c.create_text(650,420,text=(str(ehp)+' hp'))
            text4 = c.create_text(350,270,text=(name))
            text5 = c.create_text(650,270,text='Monster')
            for i in range(30):
                sleep(0.1)
                window.update()
            c.delete(text)
            text=c.create_text(400,150,text='Below the Monsters you can see their HP. FP,TP and CP are hidden though!')
            for i in range(30):
                sleep(0.1)
                window.update()
            c.delete(text)
            decision = ''
            text = c.create_text(400,150,text='Now pick a move. The decription of each move type is below your monsters at the moment.')
            while ehp > 0 and hp > 0:
                text10 = c.create_text(400,500,text='F (Fight) attacks with the damage of your FP.')
                text7 = c.create_text(400,520,text='T (Trick) has a chance, depending on your TP, of dealing double damage and blocking the opposing attack!')
                text8 = c.create_text(400,540,text='C (Cool attack) deals less damage but has a chance of preventing an opponent blocking it or attacking!')
                while decision == '':
                    sleep(0.01)
                    window.update()
                c.delete(text)
                if decision == 'F':
                    movetype = 'attack'
                if decision == 'T':
                    movetype = 'trick'
                if decision == 'C':
                    movetype = 'cool attack'
                decision = ''
                emovetype = 'attack'
                success = 1
                if movetype == 'attack':
                    text = c.create_text(400,150,text='Great! You chose to attack!')
                    text6 = c.create_text(400,500,text=name+' attacked and dealt '+str(fp)+' damage!')
                    damage = fp
                if movetype == 'trick':
                    text = c.create_text(400,150,text='Great! You chose to do a trick!')
                    if tp != 0:
                        text6 = c.create_text(400,500,text=name+' used a trick attack and dealt '+str(2*fp)+' damage!')
                        damage = 2*fp
                    else:
                        text6 = c.create_text(400,500,text=name+' tried to use a trick, but it failed as they have no TP.')
                        success = 0
                if movetype == 'cool attack':
                    text = c.create_text(400,150,text='Great! You chose to do a cool attack to surprise your opponent!')
                    if cp != 0:
                        text6 = c.create_text(400,500,text=name+' used a cool attack and dealt '+str(round(0.5*fp))+' damage!')
                        damage = 0.5*fp
                    else:
                        text6 = c.create_text(400,500,text=name+' tried to use a cool attack, but failed as they have no CP.')
                        success = 0
                ehp -= damage
            
                damage = 0
                c.delete(text,text3,text10,text7,text8)
                text3 = c.create_text(650,420,text=(str(ehp)+' hp'))
                for i in range(30):
                    sleep(0.1)
                    window.update()
                if ehp < 1:
                    break
                c.delete(text6,text)
                text = c.create_text(400,150,text='Now your opponent attacks.')
                sleep(0.2)
                if movetype == 'attack':
                    text6 = c.create_text(400,500,text='Monster attacked and dealt 1 damage!')
                    damage = 1
                elif movetype == 'trick' and success == 1: text6 = c.create_text(400,500,text='Monster failed to attack because he was dazed from the powerful trick!')
                elif movetype == 'cool attack': text6 = c.create_text(400,500,text='Monster failed to attack because he was dazzled by the cool attack!')
                hp -= damage
                c.delete(text2)
                text2 = c.create_text(350,420,text=(str(hp)+' hp'))
                for i in range(30):
                    sleep(0.1)
                    window.update()
                c.delete(text6)
            c.delete(text,text2,text3,text4,text5,text6)
            for i in range(6):
                c.delete(Mon1[i],Mon2[i])
            if hp < 1:
                hp = 1
                win = False
            else: win = True
            if win == True:
                text = c.create_text(400,500,text='Great! You beat my monster in battle! After a battle, your monster keeps the same hp unless they lose in which case it is 1. Feed your monster before their next battle!')
                level = 2
            else:
                text = c.create_text(400,500,text='Your monster lost... Try training your monster\'s stats and try again! Also, your monster is now on 1hp so feed them quickly!')
            for i in range(40):
                window.update()
                sleep(0.1)
            c.delete(text)
    else:
        damage = 0
        if level == 2:
            opponent = 'Bob'
            ehp = 12
            text = c.create_text(400,500,text='Your first league battle is against Bob! Good luck!')
            efp = 3
            etp = 4
            ecp = 2
            eprob = [50,25,25]
        elif level == 3:
            opponent = 'Michael'
            ehp = 15
            efp = 4
            etp = 4
            ecp = 3
            eprob = [30,30,40]
        elif level == 4:
            opponent = 'Warrior'
            ehp = 15
            efp = 7
            etp = 2
            ecp = 3
            eprob = [50,40,10]
        if level != 2:
            text = c.create_text(400,500,text='Your next battle is against '+opponent+'! Good luck!')
        for i in range(30):
            window.update()
            sleep(0.1)
        text2 = c.create_text(350,420,text=(str(hp)+' hp'))
        text3 = c.create_text(650,420,text=(str(ehp)+' hp'))
        text4 = c.create_text(350,270,text=(name))
        text5 = c.create_text(650,270,text=opponent)
        Mon1 = list()
        Mon1.append(c.create_rectangle(300,300,400,400,fill='white',outline='black'))
        Mon1.append(c.create_rectangle(330,320,340,340,fill='black'))
        Mon1.append(c.create_rectangle(360,320,370,340,fill='black'))
        Mon1.append(c.create_rectangle(320,370,330,380,fill='green'))
        Mon1.append(c.create_rectangle(370,370,380,380,fill='green'))
        Mon1.append(c.create_rectangle(330,380,370,390,fill='green'))
        Mon2 = list()
        Mon2.append(c.create_rectangle(600,300,700,400,fill='blue',outline='black'))
        Mon2.append(c.create_rectangle(630,320,640,340,fill='black'))
        Mon2.append(c.create_rectangle(660,320,670,340,fill='black'))
        Mon2.append(c.create_rectangle(620,390,630,400,fill='red'))
        Mon2.append(c.create_rectangle(670,390,680,400,fill='red'))
        Mon2.append(c.create_rectangle(630,380,670,390,fill='red'))
        if hp <= 20:
            if hp <= 10:
                for i in range(3):
                    c.itemconfig(Mon1[i+3],fill='red')
                c.move(Mon1[3],0,20)
                c.move(Mon1[4],0,20)
            else:
                for i in range(3):
                    c.itemconfig(Mon1[i+3],fill='yellow')
                c.move(Mon1[3],0,10)
                c.move(Mon1[4],0,10)
        if ehp <= 20:
            if ehp <= 10:
                for i in range(3):
                        c.itemconfig(Mon2[i+3],fill='red')
                c.move(Mon2[3],0,20)
                c.move(Mon2[4],0,20)
            else:
                for i in range(3):
                    c.itemconfig(Mon2[i+3],fill='yellow')
                c.move(Mon2[3],0,10)
                c.move(Mon2[4],0,10)
        c.delete(text)
        while ehp > 0 and hp > 0:
                text6 = 0
                text10 = c.create_text(400,500,text='F (Fight) attacks with the damage of your FP.')
                text7 = c.create_text(400,520,text='T (Trick) has a chance, depending on your TP and your opponent\'s TP, of dealing double damage and blocking the opposing attack!')
                text8 = c.create_text(400,540,text='C (Cool attack) deals less damage but has a chance of preventing an opponent blocking it or attacking, depending on both of your CPs!')
                while decision == '':
                    sleep(0.01)
                    window.update()
                c.delete(text)
                blocked = False
                eblocked = False
                if decision == 'F':
                    movetype = 'attack'
                if decision == 'T':
                    movetype = 'trick'
                if decision == 'C':
                    movetype = 'cool attack'
                decision = ''
                prob = randint(1,100)
                if prob < eprob[0]: #Fight
                    emovetype = 'attack'
                elif prob < eprob[0] + eprob[1]: #Trick
                    emovetype = 'trick'
                else: #Cool attack
                    emovetype = 'cool attack'
                if movetype == 'trick':
                    successpercent = (tp/etp)*50
                    num = randint(1,100)
                    if num <= successpercent:
                        success = True
                    else:
                        success = False
                if emovetype == 'trick':
                    if tp != 0:successpercent = (etp/tp)*50
                    else: successpercent = 90
                    num = randint(1,100)
                    if num <= successpercent:
                        esuccess = True
                if movetype == 'cool attack':
                    successpercent = (cp/ecp)*50
                    num = randint(1,100)
                    if num <= successpercent:
                        success = True
                    else:
                        success = False
                if emovetype == 'cool attack':
                    if cp != 0:successpercent = (ecp/cp)*50
                    else: successpercent = 90
                    num = randint(1,100)
                    if num <= successpercent:
                        esuccess = True
                    else:
                        esuccess = False
                if movetype == 'attack':
                    if emovetype == 'attack' or esuccess == False:
                        text6 = c.create_text(400,500,text=name+' attacked and dealt '+str(fp)+' damage!')
                        damage = fp
                    else:
                        blocked = True
                if movetype == 'trick':
                    emovetype = 'cool attack'
                    esuccess = True
                    if success == True and (emovetype != 'cool attack' or esuccess != True): #Attack succeeded
                        if tp != 0:
                            text6 = c.create_text(400,500,text=name+' used a trick attack and dealt '+str(2*fp)+' damage!')
                            damage = 2*fp
                            eblocked = True
                        else:
                            text6 = c.create_text(400,500,text=name+' tried to use a trick, but it failed as they have no TP.')
                            success = False
                    elif success == False: #Attack failed
                        text6 = c.create_text(400,500,text=name+' tried to use a trick attack but failed...')
                    else: #Enemy used cool attack successfully
                        blocked = True
                if movetype == 'cool attack':
                    if cp != 0:
                        text6 = c.create_text(400,500,text=name+' used a cool attack and dealt '+str(round(0.5*fp))+' damage!')
                        damage = 0.5*fp
                        if success == True: eblocked = True
                    else:
                        text6 = c.create_text(400,500,text=name+' tried to use a cool attack, but failed as they have no CP.')
                        success = False
                ehp -= damage
            
                damage = 0
                c.delete(text3,text10,text7,text8)
                text3 = c.create_text(650,420,text=(str(ehp)+' hp'))
                if blocked == False:
                    for i in range(30):
                        sleep(0.1)
                        window.update()
                if ehp < 1:
                    break
                c.delete(text6,text)
                if eblocked == True:
                    if movetype == 'trick' and success == True: text6 = c.create_text(400,500,text=opponent+' failed to attack because they were dazed from the powerful trick!')
                    elif movetype == 'cool attack' and success == True: text6 = c.create_text(400,500,text=opponent+' failed to attack because they were dazzled by the cool attack!')
                elif emovetype == 'attack':
                    text6 = c.create_text(400,500,text=opponent+' attacked and dealt 1 damage.')
                    damage = efp
                elif emovetype == 'trick':
                    text6 = c.create_text(400,500,text=opponent+' used a trick attack and dealt '+str(2*efp)+' damage.')
                    damage = 2*efp
                hp -= damage
                c.delete(text2)
                text2 = c.create_text(350,420,text=(str(hp)+' hp'))
                for i in range(30):
                    sleep(0.1)
                    window.update()
                c.delete(text6)
                if blocked == True:
                    if emovetype == 'trick' and success == True: text6 = c.create_text(400,500,text=name+' failed to attack because they were dazed from the powerful trick!')
                    elif emovetype == 'cool attack' and success == True: text6 = c.create_text(400,500,text=name+' failed to attack because they were dazzled by the cool attack!')
                    for i in range(30):
                        sleep(0.1)
                        window.update()
        c.delete(text,text2,text3,text4,text5,text6)
        for i in range(6):
            c.delete(Mon1[i],Mon2[i])
        if hp < 1:
            hp = 1
            win = False
        else: win = True
        if win == True:
            text = c.create_text(400,500,text='Great! You beat '+opponent+' in battle! After a battle, your monster keeps the same hp unless they lose in which case it is 1. Feed your monster before their next battle!')
            level += 1
        else:
            text = c.create_text(400,500,text='Your monster lost... Try training your monster\'s stats and try again! Also, your monster is now on 1hp so feed them quickly!')
        for i in range(40):
            window.update()
            sleep(0.1)
        c.delete(text)
    updatemon(hp,ohp)
    #Coding for league, then return below
    c.move(menua,-10000,0)
    c.move(menub,-10000,0)
    c.move(menuc,-10000,0)
    c.move(eye1,-10000,0)
    c.move(eye2,-10000,0)
    c.move(mouth1,-10000,0)
    c.move(mouth2,-10000,0)
    c.move(mouth3,-10000,0)
    c.move(hpdisplay,-10000,0)
    c.move(menua,-10000,0)
    c.move(menub,-10000,0)
    c.move(menuc,-10000,0)
while True:
    if menu == True:
        if movedir == 1:
            if menupos != 6:
                menupos += 1
        if movedir == 2:
            if menupos != 1:
                menupos -= 1
    movedir = 0
    if menupos == 1:
        c.delete(menub)
        menub = c.create_text(400,800,text='Feed (Food = '+str(food)+')')
    if menupos == 2:
        c.delete(menub)
        menub = c.create_text(400,800,text='Minigame')
    if menupos == 3:
        c.delete(menub)
        menub = c.create_text(400,800,text='Train')
    if menupos == 4:
        c.delete(menub)
        menub = c.create_text(400,800,text='Something')
    if menupos == 5:
        c.delete(menub)
        menub = c.create_text(400,800,text='League')
    if menupos == 6:
        c.delete(menub)
        menub = c.create_text(400,800,text='Save and Quit')
    if height < 800:
        c.move(menub,450,-450)
    if Selected == True:
        if menupos == 1:
            feed()
        if menupos == 2:
            Minigame()
        if menupos == 3 and a == 20:
            Train()
        if menupos == 4:
            world()
        if menupos == 5:
            league()
        if menupos == 6:
            save()
            quit = True
            print ('Saved successfully.')
        Selected = False
    if quit == True:
        print ('Quitting the game.')
        break
    window.update()
    sleep(0.1)
    seconds += 0.1
    if seconds > 60:
        seconds = 0
        hp -= 1
        updatemon(hp,hp+1)
    c.delete(hpdisplay)
    hpdisplay = c.create_text(500,20,text=name+'\'s hp is '+str(hp))
    if a < 20: a += 1
    if a == 20 and b == 1: c.delete(train)
    if hp <= 0:
        death = True
        window.destroy()
        print(name+' died... Start again by creating your file again.')
        save()
        break
if death == False: window.destroy()
