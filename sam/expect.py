import sys
from pathlib import Path
from sam.tools import ufilter, slowprint

class ArgvCM:
    def __init__(self, argv_new):
        self._argv_new = argv_new
        self._argv_old = sys.argv
    def __enter__(self):
        sys.argv = self._argv_new
    def __exit__(self,*a,**b):
        sys.argv = self._argv_old

class Answers:
    def __init__(self, answers):
        self._answers=answers
    def __call__(self,prompt):
        sys.stdout.write(prompt)
        answer = self._answers.pop(0)
        sys.stdout.write(answer+'\n')
        return answer
    def is_empty(self):
        return self._answers == []

class AnswersCM:
    def __init__(self, input_new):
        self._input_new = input_new
        self._input_old = __builtins__['input']
    def __enter__(self):
        __builtins__['input'] = self._input_new
    def __exit__(self,*a,**b):
        __builtins__['input'] = self._input_old
        if not self._input_new.is_empty():
            raise Samantha_AnswersLeft

def AnswersCM2(*aList):
    aList = [str(x) for x in aList]
    return AnswersCM(Answers( aList ))


class Exc_Samantha(Exception):
    pass
class Samantha_AnswersLeft(Exc_Samantha):
    pass


def wraprun(target,args):
    with ArgvCM( [target] + args.copy() ):
        exec(Path(target).read_bytes())

