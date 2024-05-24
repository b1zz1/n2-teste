import pytest
from stat_funcs import StatsN2

@pytest.mark.parametrize("val, res", [("fixture_generica", 'Existe moda'), ("fixture_generica2", 'Existe moda'  ), ("fixture_generica3", 'Não existe moda')])
def test_amodal(val, res, request):
    val = request.getfixturevalue(val)
    o = StatsN2()

    assert o.amodal(val) == res


@pytest.mark.xfail(reason = "String encontrada")
def test_xfail_amodal(fixture_generica_erro):
    o = StatsN2()
    assert o.amodal(fixture_generica_erro) is float