import pytest
import sys
from pathlib import Path

import sam.context_managers as CM
import sam.expect as EXP
import info.party as party

def test_too_many_inputs_should_raise_exception(Q):
    too_many = ['','','']
    with pytest.raises(EXP.Samantha_AnswersLeft):
        with CM.answers('','',''):
            EXP.wraprun(Q.party, [1])


@pytest.mark.parametrize("age",  party.AGES)
@pytest.mark.parametrize("name", party.NAMES)
@pytest.mark.parametrize("ver",  party.VERSIONS)
def test_usual_guests(ver,name,age,Q,capsys):
    with CM.answers(name,age):
        EXP.wraprun(Q.party, [ver])
    stdout = capsys.readouterr().out
    assert age
    if age>=19:
        assert stdout == party.stdout_legal_age(ver,name,age)
    elif age<19:
        assert stdout == party.stdout_under_age(ver,name,age)

@pytest.mark.parametrize("age",  party.BAD_AGES)
@pytest.mark.parametrize("name", party.NAMES)
@pytest.mark.parametrize("ver",  party.VERSIONS)
def test_unparsable_ages(ver,name,age,Q,capsys):
    with CM.answers(name,age):
        EXP.wraprun(Q.party, [ver])
    assert capsys.readouterr().out == party.stdout_bad_age(ver,name,age)


@pytest.mark.parametrize("age",  party.AGES + party.BAD_AGES)
@pytest.mark.parametrize("name", party.VIP_NAMES )
@pytest.mark.parametrize("ver",  party.VERSIONS)
def test_party_runner2(ver,name,age,Q,capsys):
    with CM.answers(name):
        EXP.wraprun(Q.party, [ver])
    assert capsys.readouterr().out == party.stdout_vip(ver,name,age)

@pytest.mark.parametrize("age",  party.AGES + party.BAD_AGES)
@pytest.mark.parametrize("name", party.VIP_NAMES )
@pytest.mark.parametrize("ver",  party.VERSIONS )
def test_party_runner2_exec(ver,name,age,Q,capsys):
    with CM.argv([Q.party, ver]):
        with CM.answers(name):
            exec(Path(Q.party).read_bytes())
    stdout = capsys.readouterr().out
    assert stdout == party.stdout_vip(ver,name,age)

