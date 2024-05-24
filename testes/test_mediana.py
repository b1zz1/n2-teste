import pytest
from stat_funcs import StatsN2


@pytest.mark.parametrize("val, res", [("fixture_generica", 3.0), ("fixture_generica2", 3.5 ), ("fixture_generica3", 3.5)])
def test_mediana(val, res, request):
    val = request.getfixturevalue(val)
    o = StatsN2()

    assert o.mediana(val) == res


@pytest.mark.xfail(reason = "String encontrada")
def test_xfail_mediana(fixture_generica_erro):
    o = StatsN2()
    assert o.mediana(fixture_generica_erro) is not float