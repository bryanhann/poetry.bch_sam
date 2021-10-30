#!/usr/bin/env python3
import sys
import time
from pathlib import Path

def input_number( prompt='' ):
    x = input(prompt)
    try:
        return int(x)
    except Exception:
        return None

def ufilter(fn,items):
    acc=[]
    passed = list(filter(fn,items))
    if len(passed)<1:
        raise Exception('\nUNIQUE: Missing')
    elif len(passed)>1:
        raise Exception('\nUNIQUE: Dups.')
    else:
        return passed[0]

def slowprint(string,end='',dt=0):
    for ch in string+end:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(dt)
    return string


