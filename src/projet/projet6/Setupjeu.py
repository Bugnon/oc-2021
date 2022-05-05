from turtle import * 

# def joueraujeu():
    
# def regledujeu():
    
def grille(g,l,z,p):
    for i in range(g):
        x0 = xcor()
        y0 = ycor()
        up()
        setx(x0-p)
        sety(y0-20)
        down()
        for i in range(l):
            up()
            fd(20)
            down()
            for i in range(4):
                fd(z)
                rt(90)