# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:14:43 2019

@author: Nicholas
"""

import json

def main():
    with open("AllCards.json", encoding='utf-8') as file:
        content = json.load(file)
    file.close()
    
    with open("Allcardnames.txt","w") as file:
        for card in content:
            file.write(''.join(e for e in card if e.isalnum() or e == " " or e == "'") + "\n")
    file.close()
    
if __name__ == "__main__":
    main()