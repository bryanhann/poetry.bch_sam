import pytest
import pytest
@pytest.fixture(scope='function')
def take_input(request):
    val = input(request.param)
    return val

@pytest.mark.parametrize('prompt',('Enter value here:'), indirect=True)
def test_input(take_input):
    assert take_input == "expected string"
