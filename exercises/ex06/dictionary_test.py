"""EX06- Testing the Dictionary Functions."""
_author__ = "730237027"


from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_colors
from exercises.ex06.dictionary import count


def test_invert_empty() -> None:
    """Checks that empty list is returned when empty list is passed through invert function."""
    assert invert({}) == {}


def test_invert_many_items() -> None:
    """Given dictionary a with multiple key, value pairs, invert creates new dict with the inverted key, value pair.""" 
    assert invert({"a": "aa", "b": "bb", "c": "cc", "d": "dd"}) == {"aa": "a", "bb": "b", "cc": "c", "dd": "d"}
  

def test_invert_KeyError() -> None:
    """If given dictionary has keys with the same values, the first key associated with this value appears in the inverted dict.
    
    Test for invert function and its handling of dict with two or more of the same value.
    """
    assert invert({"a": "aa", "b": "aa"}) == {"aa": "a"}


def test_favorite_color_empty() -> None:
    """Test whether empty dictonary passed through favorite_color function, an emoty string should be returned."""
    assert favorite_colors({}) == ""


def test_favorite_color_many_items() -> None:
    """Tests whether favorite_color functions works with multiple dict items."""
    assert favorite_colors({"John": "blue", "Ellie": "pink", "Taylor": "green", "Grace": "blue"}) == "blue"


def test_favorite_color_many_items2() -> None:
    """Tests whether favorite_color function works when tie occurs for favorite color."""
    assert favorite_colors({"John": "blue", "Ellie": "pink", "Taylor": "green", "Grace": "blue", "Beth": "pink"}) == "pink"


def test_count_empty() -> None:
    """Checks that a passing an empty list through the count function will return an empty dictionary."""
    assert count([]) == {}


def test_count_many_items() -> None:
    """Function tests count works with dict of multiple items."""
    assert count({"dog", "cat", "dog", "frog"}) == {"dog": 2, "cat": 1, "frog": 1} 


def test_count_many_items2() -> None:
    """Function tests count works with dict of multiple items."""
    assert count({"dog", "cat", "dog", "frog", "dog", "cat"}) == {"dog": 3, "cat": 2, "frog": 1}