from datetime import datetime; import random; import re;import sys
from pathlib import Path
from colorama import Fore, Style, init
#Завданя 2
def get_cats_info(path):
    with open(path, 'r', encoding='utf-8') as f:
        count=0; cats_inf=[]; set_3=[]
        for line in f:
            line=line.strip()
            line=re.sub(r'\\n','',line)
            list_text = line.split(',')
            cats_inf.append({'id':list_text[0],'name':list_text[1], 'age':list_text[2]})
        return cats_inf
