# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 07:13:56 2019

@author: Nicholas
"""
#import csv

def main():
    allwords = []
    keywords = set()
    source = r"Allcardnames.txt"
    with open(source, newline='') as file:
        allwords = file.read().splitlines()
    file.close()
    
    allwords.sort()
    
    dest = r"sortednames.txt"
    with open(dest, "w") as file:
        for i in allwords:
            i = ''.join(e for e in i if e.isalnum() or e == " " or e == "'")
            file.write("%s\n" % i)
            temp = i.split(" ")
            if not temp[0] or not temp[-1]:
                print(temp)
                return
            keywords.add(temp[0])
            keywords.add(temp[-1])
    file.close()
    
    sortkeywords = list(keywords)
    sortkeywords.sort()
    
    counter = 0
    encoder = dict()
    
    dest = r"keys.txt"
    with open(dest, "w") as file:
        for i in sortkeywords:
            file.write("%s %d\n" % (i,counter))
            encoder[i] = counter
            counter += 1
    file.close()
    
    
    dest = r"numericized.txt"
    with open(dest, "w") as file:
        file.write("%d\n" % len(allwords))
        for i in allwords:
            if "," in i:
                i = i.replace(",","")
            temp = i.split(" ")
            if len(temp) == 1:
                file.write("%d,\n" % encoder[temp[0]])
            else:
                file.write("%d,%d\n" % (encoder[temp[0]],encoder[temp[-1]]))
    file.close()   
    
    try:
        tinput = int(input("Enter a number to decode: "))
    except ValueError:
        tinput = -1
    while tinput > -1:
        print(sortkeywords[tinput])
        try:
            tinput = int(input("Enter a number to decode: "))
        except ValueError:
            tinput = -1
if __name__ == "__main__":
    main()
        