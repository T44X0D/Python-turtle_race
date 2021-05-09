from turtle import Turtle, Screen
import random

screen = Screen()

szinek = ["red", "orange", "yellow", "green", "blue", "purple", "gold"]

screen.setup(width=500, height=400)
tipp = screen.textinput(title="Tippelj", prompt="Melyik színű teknős ér be hamarabb?")

teki1 = Turtle(shape="turtle")
teki2 = Turtle(shape="turtle")
teki3 = Turtle(shape="turtle")
teki4 = Turtle(shape="turtle")
teki5 = Turtle(shape="turtle")
teki6 = Turtle(shape="turtle")

zero = 180
nyert = True

def init(teki_neve,sorszam):
    szam = sorszam * 60
    teki_neve.penup()
    teki_neve.color(szinek[sorszam])
    teki_neve.goto(-230, (-200 + szam))

def race(teki_neve):
    global nyert
    teki_neve.forward(random.randint(1,20))
    poz = teki_neve.pos()
    if poz[0] >= 170.0:
        nyert = False
        print(teki_neve)
        return teki_neve



tekik = (teki1, teki2, teki3, teki4, teki5, teki6)

s = 1


for i in tekik:
    init(i, s)
    s += 1

while nyert:
    for i in tekik:
        nev = race(i)

print(nev)




screen.exitonclick()