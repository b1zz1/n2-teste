import pytest
from stat_funcs import StatsN2


@pytest.mark.parametrize("val, res", [("fixture_generica", 3.0), ("fixture_generica2", 3.3333333333333335 ), ("fixture_generica3", 3.5)])
def test_media(val, res, request):
    val = request.getfixturevalue(val)
    o = StatsN2()

    assert o.media(val) == res


@pytest.mark.xfail(reason = "String encontrada")
def test_xfail_media(fixture_generica_erro):
    o = StatsN2()
    assert o.media(fixture_generica_erro) is not float
