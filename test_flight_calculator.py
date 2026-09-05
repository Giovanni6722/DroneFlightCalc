import pytest

from flight_calculator import calculate_flight_time, flight_time_table


def test_calculate_flight_time_zero_payload():
    assert calculate_flight_time(0) == 180.0


def test_calculate_flight_time_known_payloads():
    assert calculate_flight_time(100) == 170.0
    assert calculate_flight_time(500) == 130.0


def test_calculate_flight_time_fractional_weight():
    assert calculate_flight_time(12.5) == pytest.approx(178.75)
    assert calculate_flight_time(333.3) == pytest.approx(146.67, rel=1e-3)


def test_calculate_flight_time_clamps_to_zero():
    assert calculate_flight_time(1800) == 0.0
    assert calculate_flight_time(5000) == 0.0


def test_calculate_flight_time_negative_weight_raises_value_error():
    with pytest.raises(ValueError, match="must be non-negative"):
        calculate_flight_time(-1)
        
def test_flight_time_table_zero_max():
    assert flight_time_table(0, 10) == [(0, 180.0)]


def test_flight_time_table_standard_sequence():
    expected = [
        (0, 180.0),
        (50, 175.0),
        (100, 170.0),
        (150, 165.0),
        (200, 160.0),
        (250, 155.0),
    ]
    assert flight_time_table(250, 50) == expected


def test_flight_time_table_non_dividing_step():
    expected = [
        (0, 180.0),
        (3, 179.7),
        (6, 179.4),
        (9, 179.1),
    ]
    assert flight_time_table(10, 3) == expected


def test_flight_time_table_clamps_to_zero():
    expected = [
        (0, 180.0),
        (100, 170.0),
        (200, 160.0),
        (300, 150.0),
        (400, 140.0),
        (500, 130.0),
        (600, 120.0),
        (700, 110.0),
        (800, 100.0),
        (900, 90.0),
        (1000, 80.0),
        (1100, 70.0),
        (1200, 60.0),
        (1300, 50.0),
        (1400, 40.0),
        (1500, 30.0),
        (1600, 20.0),
        (1700, 10.0),
        (1800, 0.0),
    ]
    assert flight_time_table(1800, 100) == expected


def test_flight_time_table_negative_max_weight_raises_value_error():
    with pytest.raises(ValueError, match="max_weight_grams must be non-negative"):
        flight_time_table(-1, 10)


def test_flight_time_table_non_positive_step_raises_value_error():
    with pytest.raises(ValueError, match="step_grams must be positive"):
        flight_time_table(100, 0)
    with pytest.raises(ValueError, match="step_grams must be positive"):
        flight_time_table(100, -5)