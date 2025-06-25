from src.simulation import run_simulation

def test_run_simulation_basic():
    # Run the simulation with a specific number of trials (e.g., 1000)
    results = run_simulation(num_trials=1000)

    # Check if the result is a tuple
    assert isinstance(results, tuple), "Result should be a tuple"

    # Check if that the tuple has exactly two elements
    assert len(results) == 2, "Result tuple should have exactly 2 elements"

    # Check that each element is between 0 and 1 (valid win rate)
    for rate in results:
        assert 0 <= rate <= 1, f"Rate {rate} should be between 0 and 1"
