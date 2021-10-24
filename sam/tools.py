#!/usr/bin/env python3

import sys
from pathlib import Path

def input_number( prompt='' ):
    x = input(prompt)
    try:
        return int(x)
    except Exception:
        return None

def wraprun(target,args):
    old_argv = sys.argv
    try:
        sys.argv = [target] + args.copy()
        exec(Path(target).read_bytes())
    finally:
        sys.argv=old_argv

