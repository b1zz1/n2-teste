import pytest
from stat_funcs import StatsN2


@pytest.mark.parametrize("val, res", [("fixture_generica", "Distribuição normal"), ("fixture_generica2", 'Distribuição negativa'  ), ("fixture_generica3", 'Distribuição normal')])
def test_skew(val, res, request):
    val = request.getfixturevalue(val)
    o = StatsN2()

    assert o.skew(val) == res


@pytest.mark.xfail(reason="Mais de uma moda encontrada")
def test_xfail_skw(fixture_generica_erro):
    o = StatsN2()
    assert o.skew(fixture_generica_erro) is not string