import pytest
from stat_funcs import StatsN2


def test_media_ponderada(fixture_generica, fixture_generica_ponderada):
    o = StatsN2()
    assert o.media_ponderada(fixture_generica, fixture_generica_ponderada) == 3.0000000000000004


@pytest.mark.xfail(reason="Mais de uma moda encontrada")
def test_xfail_media_ponderada(fixture_generica_erro, fixture_generica_ponderada):
    o = StatsN2()
    assert o.media_ponderada(fixture_generica_erro, fixture_generica_ponderada) is not float