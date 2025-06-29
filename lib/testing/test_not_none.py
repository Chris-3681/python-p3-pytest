#!/usr/bin/env python3

from not_none_functions import return_not_none

def test_return_not_none():
    result = return_not_none()
    assert result is not None, "Expected return_not_none() to return something other than None"

    # '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
    # assert False
