import pytest
from app.functions.lists import sort_list, get_sort_type


def test_get_sort_type_no_input():
    with pytest.raises(Exception):
        get_sort_type([]) == "recent"
