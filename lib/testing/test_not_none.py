#!/usr/bin/env python3



# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False
#!/usr/bin/env python3

from not_none_functions import return_not_none

def test_return_not_none():
    '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
    result = return_not_none()
    assert result is not None, f"Expected non-None value, got {type(result).__name__}"