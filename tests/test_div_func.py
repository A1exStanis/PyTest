from Functions.div_func import div
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 5, 2),
                                                   (12, -2, -6),
                                                   (7, 2, 3.5)])
def test_div_good(a, b, expected_result):
    assert div(a, b) == expected_result


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)


@pytest.mark.parametrize('expected_result, divider, division', [(TypeError, 'q', 1),
                                                                (TypeError, [1, 2, 3], 18),
                                                                (ZeroDivisionError, 0, 21)
                                                                ])
def test_type_error(expected_result, divider, division):
    with pytest.raises(expected_result):
        assert div(division, divider)
