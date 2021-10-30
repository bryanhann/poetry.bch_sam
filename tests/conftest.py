import sys
from pathlib import Path

TESTS=Path(__file__).parent
ROOT=Path(__file__).parent.parent

sys.path.append(str(TESTS/'lib'))
import pytest

class Namespace: pass

@pytest.fixture()
def ROOT():
    ROOT=Path(__file__).parent.parent
    assert (ROOT/'pyproject.toml').is_file()
    return ROOT

@pytest.fixture
def Q(ROOT):
    xx=Namespace()
    xx.root = ROOT
    xx.party = ROOT/'apps/party'
    return xx


