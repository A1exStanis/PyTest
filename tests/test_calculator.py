from Functions.calculator import Calculator
import pytest
from contextlib import nullcontext as does_not_raises


class TestCalculator:
    @pytest.mark.parametrize(
        'x, y, res, expectation',
        [
            (5, 1, 5, does_not_raises()),
            (5, -1, -5, does_not_raises()),
            (5, "1", 5, pytest.raises(TypeError)),
            (5, 0, 5, pytest.raises(ZeroDivisionError)),
            (5, 1, 5, does_not_raises()),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res
