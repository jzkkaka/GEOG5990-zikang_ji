# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# File  : agentframework.py
# Author:zikang ji
# Date  : 2019-11-21 08:27
# Desc  : 
# -------------------------------------------------------------------------------

import random


class Agent:
    def __init__(self, environment, agents,y,x):
        self.environment = environment
        self.store = 0
        self.agents = agents
        if x != None:
            self.x = x
        else:
            self.x = random.randint(0,300)
        if y != None:
            self.y = y
        else:
            self.y = random.randint(0,300)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_store(self,store):
        self.store = store

    def get_store(self):
        return self.store

    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

    def distance_between(self, agent):
        return (((self.x - agent.x) ** 2) +
                ((self.y - agent.y) ** 2)) ** 0.5

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum / 2
                self.store = ave
                agent.store = ave
