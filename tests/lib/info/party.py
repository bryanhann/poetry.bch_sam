AGES=[18, 19]
BAD_AGES=['', 'x']
VERSIONS="0 1 2 3 4".split()
VIP_NAMES="Bryan Samantha Steve".split()
NAMES=["Mary"]
def stdout_vip(version,name,age): return f"""\
version {version}
Please enter your name: {name}
Welcome back {name}. Enjoy the party!!
"""

def stdout_legal_age(version,name,age): return f"""\
version {version}
Please enter your name: {name}
How old are you?{age}
Enjoy the party {name}. The bar is open!
"""

def stdout_under_age(version,name,age): return f"""\
version {version}
Please enter your name: {name}
How old are you?{age}
Enjoy the party {name}, but no alcohol!
"""

def stdout_bad_age(version,name,age): return f"""\
version {version}
Please enter your name: {name}
How old are you?{age}
That is not an age. Get out of here!
"""

