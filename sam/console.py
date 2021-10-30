#!/usr/bin/env python3
import sys
import sam.expect

def wraprun():
    target = sys.argv[1]
    args = sys.argv[2:].copy()
    sam.expect.wraprun(target, args)
