import unittest
from unittest import TestCase
from unittest.mock import patch
from lab1 import Example

import pytest
from abc import ABC, abstractmethod


# Implementation code

class Example(ABC):
    @abstractmethod
    def abstract_method(self):
        raise NotImplementedError

    def concrete_method(self):
        return True


# Unit tests

class TestExampleImplementation(Example):
    def abstract_method(self):
        return "Implemented"


def test_abstract_method_not_implemented():
    with pytest.raises(TypeError):
        _ = Example()


def test_abstract_method_implemented():
    instance = TestExampleImplementation()
    assert instance.abstract_method() == "Implemented"


def test_concrete_method():
    instance = TestExampleImplementation()
    assert instance.concrete_method() is True


def test_inheritance_check():
    instance = TestExampleImplementation()
    assert isinstance(instance, Example)
