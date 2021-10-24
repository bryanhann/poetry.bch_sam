#!/usr/bin/env python3
import sys
import sam.tools

def wraprun():
    target = sys.argv[1]
    args = sys.argv[2:].copy()
    sam.tools.wraprun(target, args)
