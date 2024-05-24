import pytest
from stat_funcs import StatsN2

# media = 3, mediana = 3, moda = 3
@pytest.fixture()
def fixture_generica():
    return [1, 2, 3, 3, 4, 5]


@pytest.fixture()
def fixture_generica2():
    return [1, 5, 2, 3, 4, 5]


@pytest.fixture()
def fixture_generica3():
    return [1, 2, 3, 4, 5, 6]


@pytest.fixture()
def fixture_generica_erro():
    return [1, 'A', 'B', 3, 4, 5]


@pytest.fixture()
def fixture_generica_erro_amodal():
    return [1, 2, 3, 4, 5]


@pytest.fixture()
def fixture_generica_erro_multimodal():
    return [1, 2, 3, 3, 4, 4, 5]


@pytest.fixture()
def fixture_generica_ponderada():
    return [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]


