from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

# Initialize Faker
fake = Faker()

# Define the operation mappings
operation_mappings = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

def generate_test_data(num_records):
    """
    Generates test data for arithmetic operations using Faker.
    Yields tuples (a, b, operation_name, operation_func, expected).
    """
    for _ in range(num_records):
        # Generate random numbers for 'a' and 'b'
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))

        # Randomly choose an operation
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Special case for division to avoid zero
        if operation_func == divide and b == 0:
            b = Decimal('1')  # Avoid division by zero

        # Calculate the expected result
        expected = operation_func(a, b)

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """ Adds the custom command-line option to specify the number of records. """
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

def pytest_generate_tests(metafunc):
    """ Dynamically generates test data and parameterizes the test functions. """
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        test_data = list(generate_test_data(num_records))

        metafunc.parametrize("a,b,operation_name,expected", test_data)

# Additional test functions to ensure coverage
def test_generate_test_data():
    """Test the data generation function."""
    test_data = list(generate_test_data(5))
    assert len(test_data) == 5  # Check if 5 records are generated

    # Check for valid operation names
    for _, _, operation_name, _, _ in test_data:
        assert operation_name in operation_mappings

def test_operation_with_negatives():
    """Test operations with negative numbers."""
    assert add(3, -2) == 1
    assert subtract(-3, -2) == -1
    assert multiply(-3, 3) == -9
    assert divide(-6, 2) == -3

def test_large_numbers():
    """Test operations with large numbers."""
    assert add(Decimal('1e6'), Decimal('1e6')) == Decimal('2e6')
    assert subtract(Decimal('1e6'), Decimal('1')) == Decimal('999999')
    assert multiply(Decimal('1e3'), Decimal('1e3')) == Decimal('1e6')
    assert divide(Decimal('1e6'), Decimal('1e3')) == Decimal('1000')

def test_edge_cases():
    """Test edge cases for operations."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(Decimal('1'), Decimal('0'))

    assert add(Decimal('0'), Decimal('0')) == Decimal('0')
    assert subtract(Decimal('0'), Decimal('0')) == Decimal('0')