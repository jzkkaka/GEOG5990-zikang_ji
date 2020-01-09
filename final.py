# -*- coding: utf-8 -*-#

import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import tkinter
import requests
import bs4
import agentframework
import csv

matplotlib.use('TkAgg')

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class": "y"})
td_xs = soup.find_all(attrs={"class": "x"})
#print(td_ys)
#print(td_xs)

num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(10, 10))
ax = fig.add_axes([0, 0, 1, 1])


# get enviroment
environment = []
with open('in.txt',newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        rowlist = []
        for value in row:
            rowlist.append(int(value))
        environment.append(rowlist)


for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)

    agents.append(agentframework.Agent(environment, agents, y, x))


def update(frame_number):
    fig.clear()
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(20)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        # print(agents[i].x, agents[i].y)
    matplotlib.pyplot.imshow(environment)

carry_on = True

def gen_function(b=[0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on):
        yield a
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=True)

    canvas.draw()

root = tkinter.Tk()
root.wm_title("Model")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


tkinter.mainloop()
