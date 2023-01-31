from my_functions import return_strings_twice

def test_return_strings():
    test_strings = "Hello, World."
    actual = return_strings_twice(message = test_strings)
    expected = "Hello, World.Hello, World."
    assert actual == expected

def test_return_strings_again():
    test_strings = "Hello, GitHub."
    actual = return_strings_twice(message = test_strings)
    expected = "Hello, GitHub.Hello, GitHub."
    assert actual == expected