from service.main import mod_function


def test_test_function():
    assert mod_function("val") == "_val_"