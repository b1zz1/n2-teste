import pytest
from stat_funcs import StatsN2

@pytest.mark.parametrize("val, res", [("fixture_generica", 'Não é multimodal'), ("fixture_generica2", 'Não é multimodal'  ), ("fixture_generica3", [1, 2, 3, 4, 5, 6] )])
def test_multimodal(val, res, request):
    val = request.getfixturevalue(val)
    o = StatsN2()

    assert o.multimodal(val) == res

@pytest.mark.xfail(reason="Nenhuma moda encontrada")
def test_xfail_multimodal(fixture_generica_erro_multimodal):
    o = StatsN2()
    assert o.multimodal(fixture_generica_erro_multimodal) is "Não é multimodal"