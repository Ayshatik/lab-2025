import unittest
import pytest
from lab4 import MyIterator

def test_iterator_normal_usage():
    data = [1, 2, 3, 4, 5]
    iterator = MyIterator(data)
    result = list(iterator)
    assert result == data

def test_iterator_empty_list():
    data = []
    iterator = MyIterator(data)
    result = list(iterator)
    assert result == data

def test_iterator_single_element():
    data = [42]
    iterator = MyIterator(data)
    result = list(iterator)
    assert result == data

def test_iterator_stop_iteration():
    data = [10, 20, 30]
    iterator = MyIterator(data)
    iterator.__next__()
    iterator.__next__()
    iterator.__next__()
    with pytest.raises(StopIteration):
        iterator.__next__()

def test_iterator_reuse():
    data = [5, 10, 15]
    iterator = MyIterator(data)
    list(iterator)  # Consume iterator
    with pytest.raises(StopIteration):
        iterator.__next__()  # Further calls should raise StopIteration

def test_iterator_multiple_iter_calls():
    data = [7, 14, 21]
    iterator = MyIterator(data)
    first_result = list(iterator)
    iterator.index = 0  # Reset index for new iteration simulation second_result = list(iterator)



