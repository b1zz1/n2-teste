import pytest
from stat_funcs import StatsN2


@pytest.mark.parametrize("val, res", [("fixture_generica", 2.0), ("fixture_generica2", 2.666666666666667  ), ("fixture_generica3", 3.5)])
def test_variancia(val, res, request):
    val = request.getfixturevalue(val)
    o = StatsN2()

    assert o.variancia(val) == res


@pytest.mark.xfail(reason="Mais de uma moda encontrada")
def test_xfail_variancia(fixture_generica_erro):
    o = StatsN2()
    assert o.variancia(fixture_generica_erro) is not float