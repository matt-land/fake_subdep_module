import pytest

from fakesubdepmodule import index


def test_foo():
    assert 'bar' == index.foo()