# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 07:14:15 2019

@author: Nicholas
"""

def main():
    with open(r"daisychains.txt","r") as file:
        chain = file.read()
    file.close()
    chain = chain.split(" ")
    chain.pop()
    
    decoder = dict()
    with open(r"keys.txt","r") as file:
        for line in file:
            if line:
                line=line[:-1].split(" ")
                decoder[line[1]] = line[0]
                
    file.close()
    
    cards = dict()
    with open(r"Allcardnames.txt","r") as file:
        for line in file:
            if line:
                name = line[:-1]
                line=name.replace(",","").split(" ")
                if line[0] in cards:
                    cards[line[0]].append((line[-1],name))
                else:
                    cards[line[0]] = [(line[-1],name)]
    file.close()
    cardcount = 0
    with open(r"FinalChain.txt","w") as file:
        for i in range(0,len(chain) -1):
            found = False
            for card in cards[decoder[chain[i]]]:
                if card[0] == decoder[chain[i+1]]:
                    file.write(card[1]+"\n")
                    found = True
                    cardcount +=1
            if not found:
                print("Does not work!")
        file.write(str(cardcount))
    file.close()
if __name__ == "__main__":
    main()