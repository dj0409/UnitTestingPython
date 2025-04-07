import pytest
from bat_functions import (
    calculate_bat_power,
    signal_strength,
    get_bat_vehicle,
    fetch_joker_info
)


# Exercise 1: Basic Tests

def test_calculate_bat_power():
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(3) == 126
    assert calculate_bat_power(-1) == -42

@pytest.mark.parametrize("distance,expected", [
    (0, 100),
    (1, 90),
    (5, 50),
    (10, 0),
    (15, 0)
])
def test_signal_strength(distance, expected):
    assert signal_strength(distance) == expected

# Exercise 2: Fixtures

@pytest.fixture
def bat_vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle_known(bat_vehicles):
    for name, specs in bat_vehicles.items():
        assert get_bat_vehicle(name) == specs

def test_get_bat_vehicle_unknown():
    with pytest.raises(ValueError) as exc:
        get_bat_vehicle("Batboat")
    assert "Unknown vehicle" in str(exc.value)


# Exercise 3: Mocking

def test_fetch_joker_info_mock(monkeypatch):
    def mock_fetch():
        return {'mischief_level': 0, 'location': 'captured'}

    import bat_functions  
    monkeypatch.setattr(bat_functions, "fetch_joker_info", mock_fetch)
    result = bat_functions.fetch_joker_info()
    assert result == {'mischief_level': 0, 'location': 'captured'}

