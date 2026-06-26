import pytest
from divides import divide
def test_divide():
        assert divide(9)
        with pytest.raises(ValueError):
                divide(-9)