# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:37:09 2016

@author: eimantas
"""
import sys

def stillAvailable():
    for boy in boys:
        if boy.spouse is None:
            return 1
    return 0

class Boy:
    spouse = None
    pref_index = 0
    def __init__(self, name, preference):
        self.name = name
        self.preference = preference

class Girl:
    spouse = None
    def __init__(self, name, preference):
        self.name = name
        self.preference = preference

boys = []
girls = []
marriages = []

def initPeople():    
    with open(sys.argv[1]) as graph_input_file:
        graph = [line.split() for line in graph_input_file]    
    for i in range(len(graph)/2):
        boys.append(Boy(i, graph[i]))        
    for i in xrange(len(boys),len(graph)):
        girls.append(Girl(i-len(boys),graph[i]))        
    graph_input_file.closed

def printout():
    sys.stdout = open(sys.argv[2],'w')
    marriages.sort(key=lambda x: x[0])
    for marriage in marriages:
        print marriage[0],marriage[1]

def stableMarriage():

    initPeople()

    while stillAvailable():
        for boy in boys:
            if boy.spouse == None:
                if girls[int(boy.preference[boy.pref_index])].spouse == None:
                    marriages.append([boy.name,girls[int(boy.preference[boy.pref_index])].name, ])
                    boy.spouse = girls[int(boy.preference[boy.pref_index])].name
                    girls[int(boy.preference[boy.pref_index])].spouse = boy.name  
                else:
                    if girls[int(boy.preference[boy.pref_index])].preference.index(str(girls[int(boy.preference[boy.pref_index])].spouse)) > girls[int(boy.preference[boy.pref_index])].preference.index(str(boy.name)):
                        marriages[girls[int(boy.preference[boy.pref_index])].spouse][0] = boy.name
                        boy.spouse = girls[int(boy.preference[boy.pref_index])].name
                        boys[girls[int(boy.preference[boy.pref_index])].spouse].spouse = None
                        girls[int(boy.preference[boy.pref_index])].spouse = boy.name    
                    else:
                        boy.pref_index += 1
    printout()

def main():
    stableMarriage()
    
if __name__ == "__main__":
    main()