import os
import pandas as pd
import pytest
from faker import Faker
from calculator.calculation_history import CalculationHistory  # Import the CalculationHistory class

# Initialize Faker
fake = Faker()

@pytest.fixture
def setup_calculation_history(tmpdir):
    """Fixture to set up a temporary CalculationHistory object."""
    temp_file = tmpdir.join("temp_history.csv")
    history = CalculationHistory(filename=str(temp_file))
    return history, str(temp_file)

def test_add_entry(setup_calculation_history):
    history, _ = setup_calculation_history
    operation = fake.word()  # Generate a random operation name
    operands = (fake.random_int(), fake.random_int())
    result = sum(operands)  # Example for addition; change based on the operation
    history.add_entry(operation, operands, result)
    assert len(history.history) == 1
    assert history.history.iloc[0]['operation'] == operation
    # Compare the string representation of operands
    assert history.history.iloc[0]['operands'] == str(operands)  # Ensure correct format
    assert history.history.iloc[0]['result'] == result

def test_save_history(setup_calculation_history):
    history, temp_file = setup_calculation_history
    operation = fake.word()  # Generate a random operation name
    operands = (fake.random_int(), fake.random_int())
    result = sum(operands)  # Example for addition; change based on the operation
    history.add_entry(operation, operands, result)
    history.save_history()
    # Load the saved history to verify
    loaded_history = pd.read_csv(temp_file)
    assert len(loaded_history) == 1
    assert loaded_history.iloc[0]['operation'] == operation
    assert loaded_history.iloc[0]['operands'] == str(operands)  # Ensure correct format
    assert loaded_history.iloc[0]['result'] == result

def test_clear_history(setup_calculation_history):
    history, _ = setup_calculation_history
    operation = fake.word()  # Generate a random operation name
    operands = (fake.random_int(), fake.random_int())
    result = sum(operands)  # Example for addition; change based on the operation
    history.add_entry(operation, operands, result)
    history.clear_history()
    assert len(history.history) == 0

def test_load_existing_history(setup_calculation_history):
    history, temp_file = setup_calculation_history
    # Create a sample history file with dynamic data
    sample_data = pd.DataFrame({
        'operation': [fake.word() for _ in range(2)],
        'operands': [str((fake.random_int(), fake.random_int())) for _ in range(2)],  # Store as string
        'result': [sum((fake.random_int(), fake.random_int())) for _ in range(2)]
    })
    sample_data.to_csv(temp_file, index=False)

    # Load the existing history
    new_history = CalculationHistory(filename=str(temp_file))
    assert len(new_history.history) == 2
    assert new_history.history.iloc[0]['operation'] == sample_data.iloc[0]['operation']
    assert new_history.history.iloc[1]['operation'] == sample_data.iloc[1]['operation']