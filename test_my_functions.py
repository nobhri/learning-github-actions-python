from my_functions import return_strings_twice

def test_return_strings():
    test_strings = "Hello, World."
    actual = return_strings_twice(message = test_strings)
    expected = "Hello, World.Hello, World."
    assert actual == expected