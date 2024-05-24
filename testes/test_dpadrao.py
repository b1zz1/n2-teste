import pytest
from stat_funcs import StatsN2


def test_dpadrao(fixture_generica):
    o = StatsN2()
    res = o.variancia(fixture_generica)

    assert o.dpadrao(res) == 1.4142135623730951

@pytest.mark.xfail(reason = "String encontrada")
def test_xfail_dpadrao(fixture_generica_erro):
    o = StatsN2()
    res = o.variancia(fixture_generica)

    assert o.dpadrao(res) is not float