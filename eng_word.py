# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:16:17 2019

@author: lcy
"""

import openpyxl
import random

def load_xl(wb,row):
    word_list = []
    ws = wb.active
    cell_1 = ws.cell(row,1)
    cell_2 = ws.cell(row,2)
    word_list.append(cell_1.value)
    c_list = cell_2.value.split(',')
    if len(c_list) == 1:
        word_list.append(c_list[0])
    else:
        word_list.append(c_list[0])
        word_list.append(c_list[1])
    
    return word_list
    
if __name__ =="__main__":
    wb = openpyxl.load_workbook("word_list.xlsx")
    
    while True:
        i = random.randint(175,181)
        w_list = load_xl(wb,i)
        print("英文单词：" + w_list[0])#注释
        Cword = input("输入中文意思：")
        if len(w_list) == 2 :
            if Cword == w_list[1]:
                print("You are right!")
                continue
            elif Cword == "quit":
                break
            while Cword != w_list[1]:
                print("You are wrong!Try again!")
                Cword = input("输入中文意思：")
                if Cword == "quit":
                    break
        elif len(w_list) == 3:
            if Cword == w_list[1] or Cword == w_list[2]:
                print("You are right!")
                continue
            elif Cword == "quit":
                break
            while Cword != w_list[1]:
                print("You are wrong!Try again!")
                Cword = input("输入中文意思：")
                if Cword == "quit":
                    break
        
            
            

    