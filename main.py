# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:33:30 2019

@author: Nicholas
"""
import cdm,alphabetize,decypher

def main():
    print("Calling alphabetize.py")
    alphabetize.main()
    print("Calling cdm.py")
    cdm.main()
    print("Decyphering...")
    decypher.main()
    print("Finished!")
    
if __name__ == "__main__":
    main()