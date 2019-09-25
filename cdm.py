# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 07:10:33 2019

@author: Nicholas
"""
from copy import deepcopy
class Node:
    def __init__(self,int0,int1,ismark=False):
        self.id = int0
        if int1 or int1 == 0:        
            self.children = [int1]
            self.numchildren = 1
        else:
            self.children = []
            self.numchildren = 0
        self.hasparent = False
        self.ismarker = ismark
        self.parents = []

        #idea added later. Every search is given a searchid. Removes need to unmark nodes
        self.searchids = set()
        #self.subtreesize = -1 #for visit children
        
        self.dfstreesize = 1
        self.chains = [[self.id]]
        
        #For Hope Against Hope and similar cards
        self.copies = 0
    def add(self,int0):
        if int0 == self.id:
            self.copies += 1
            #return
        self.children.append(int0)
        self.numchildren += 1
    def addparent(self,node):
        if node.id == self.id:
            return
        self.hasparent = True
        self.parents.append(node)
        #self.ismarker = False
    def __repr__(self):
        return str(self.id)
    def deadend(self):
        #called if this is a deadend
        for parent in self.parents:
            parent.condense(self,self.dfstreesize,self.maxchain())
            
        #pretend to be a marker to be ignored later
        self.ismarker = True
    def maxchain(self):
        return max(self.chains,key=len)
            
    def condense(self,node,childsize,chain):
        self.dfstreesize += childsize
        #print("New size is: " + str(self.dfstreesize))
        #print("Losing child: " + str(node.id))
        self.chains.append([self.id]+chain)
        try:
            self.children.remove(node)
        except ValueError:
            try:
                self.children.remove(node.id)
            except ValueError:
                print(self.children)
                print(self.id)
                print(node)
                print(node.id)
                raise ValueError
        if not self.children:
            self.deadend()
            
    def visited(self,searchid):
        if searchid == -1:
            return len(self.searchids)
        else:
            tbool = searchid in self.searchids   
            if self.copies:
                self.copies -= 1
                self.children.remove(self)
                return False
            else:
                self.searchids.add(searchid)
                return tbool


def main():
    source = r"numericized.txt"
    
    nodes = [None]
    prev = -1
    
    #Create a list of nodes and placeholders equal to the length of the list. 
    #this is also used for the index on nodes
    #Use placeholders to mark which have parents
    #previous is used because list is in numerical order.
    
    with open(source,"r") as file:
        #first line is number of lines but has a newline
        numkeys = int(file.readline()[:-1])
        nodes = nodes * numkeys
        for line in file:
            line = line[:-1].split(",")
            index = int(line[0])
            if line[-1]:
                index2 = int(line[-1])
                if index == prev:
                    #nodes[-1]
                    nodes[prev].add(index2)
                else:
                    #nodes.append(Node(int(line[-1])))
                    if nodes[index]:
                        nodes[index].ismarker = False
                        nodes[index].add(index2)
                    else:                        
                        nodes[index] = Node(index,index2)
                if not nodes[index2]:
                    nodes[index2] = Node(index2,None,ismark=True)
                    nodes[index2].addparent(nodes[index])
                else:
                    nodes[index2].addparent(nodes[index])
            elif index != prev:
                #nodes.append(Node(line[-1]))
                nodes[index] = Node(index,None)
            prev = index
    file.close()
    
    with open(r"temp.txt","w") as file:
        for index,i in enumerate(nodes):
            if i and not i.ismarker:
                file.write(str(index) + ":" + str(i.children)+":"+str(i.hasparent)+"\n")
    file.close()
    
    #turn all children into actual references so that later calls can not rely on nodes list
    #also try to recursively push up all dead ends as far as they go
    for i in nodes:
        if i and not i.ismarker:
            temp = []
            
            for child in i.children:
                #get rid of placeholders
                if not nodes[child].ismarker:
                    temp.append(nodes[child])
            if not temp:
                i.deadend()
            i.numchildren = len(temp)
            i.children = temp

    count = 0
    maxest = []
    for i in nodes:
        maxchain = []
        #if graphsizes[index] < 200:
            #safely ignore
        #    pass
        if i and not i.ismarker:
            count += 1
            graph = [i]
            
            chain = []
            graphlevel =[0]
            chainlevel = []
            currlevel = 0
            
            while graph:
                nextnode = graph.pop()
                currlevel = graphlevel.pop()
                if not nextnode.visited(i.id):
                    #if it has a maxchain and that is the longest chain, then add it separately and continue
                    temp = nextnode.maxchain()
                    if len(chain) + len(temp) > len(maxchain):
                        maxchain = deepcopy(chain + temp)                            
                    chain.append(nextnode.id)
                    chainlevel.append(currlevel)


                    if nextnode.children:
                        graph.extend(nextnode.children)
                        currlevel += 1
                        graphlevel.extend([currlevel]*len(nextnode.children))
                
                    else:
                        #the graph hit a dead end, so remove all on this branch
                        if len(chain) > len(maxchain):
                            maxchain = deepcopy(chain)
                        chain.pop()
                        currlevel = chainlevel.pop()
                        #remove all the words in the chain until it gets back to the next valid parent with children
                        while len(chainlevel) > 1 and len(graph) and chainlevel[-1] >= graphlevel[-1]:
                            currlevel = chainlevel.pop()
                            chain.pop()

                else:
                    #remove all the words in the chain until it gets back to the next valid parent with children
                    while len(chainlevel) > 1 and len(graph) and chainlevel[-1] >= graphlevel[-1]:
                        currlevel = chainlevel.pop()
                        chain.pop()

                if not len(graphlevel):
                    break
                    
            #print(str(maxchain))
            
        if len(maxchain) > len(maxest):
            maxest = deepcopy(maxchain)
        if count > 1000:
            count = 0
            print("Still calculating.")
            print("Currently on node: " +str(nextnode.id))
            
        
    with open(r"daisychains.txt","w") as file:    
        for key in maxest:
                file.write(str(key) + " ")
    file.close()
        
        
if __name__ == "__main__":
    main()