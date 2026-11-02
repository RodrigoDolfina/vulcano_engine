import pytest
from unittest.mock import patch
from src.vulcano_telemetry.chaos_simulation import ChaosSimulator

def test_chaos_network_latency():
    ChaosSimulator.simulate_network_latency(0.01, 0.05)
    assert True

@patch('src.vulcano_telemetry.chaos_simulation.random.choice')
def test_poison_pill_injection(mock_random_choice):
    mock_random_choice.return_value = True
    assert ChaosSimulator.should_inject_poison_pill() is True
