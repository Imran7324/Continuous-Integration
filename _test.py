import pytest

# Function to test square
def square(n):
    return n ** 2

# Function to test cube
def cube(n):
    return n ** 3

# Function to test fourth power
def fourth_power(n):
    return n ** 4

# Testing the square function
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"

# Testing the cube function
def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"

# Testing the fourth power function
def test_fourth_power():
    assert fourth_power(2) == 16, "Test Failed: Fourth power of 2 should be 16"
    assert fourth_power(3) == 81, "Test Failed: Fourth power of 3 should be 81"

# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")