import pytest
from stat_funcs import StatsN2

@pytest.mark.parametrize("val, res", [("fixture_generica", 3), ("fixture_generica2", 5  ), ("fixture_generica3", 'Não é unimodal')])
def test_unimodal(val, res, request):
    val = request.getfixturevalue(val)
    o = StatsN2()

    assert o.unimodal(val) == res


@pytest.mark.xfail(reason="Mais de uma moda encontrada")
def test_xfail_unimodal(fixture_generica_erro_multimodal):
    o = StatsN2()
    assert o.unimodal(fixture_generica_erro_multimodal) is "Não é unimodal"