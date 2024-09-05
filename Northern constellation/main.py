import turtle
import pandas

#screen
screen = turtle.Screen()
image = "Northern Constellations.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.open_csv("northern_constellations(Sheet1).csv")
print(data)


turtle.mainloop()