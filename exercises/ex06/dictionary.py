"""EX06y- Dictionary Functions."""
_author__ = "730237027"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str,str], function returns dictionary with inverted key,value pairs."""
    check: dict[str, str] = {}
    for key in a:
        if a[key] not in check:
            check[a[key]] = key
        else:
            raise KeyError("Duplicate Keys")
    return check


def favorite_color(colors: dict[str, str]) -> str:
    """Given dictionary colors of names and favorite colors, [str, str], function returns color name that appears most."""
    fav: dict[str, int] = {}
    for key in colors:
        if colors[key] not in fav:
            fav[colors[key]] = 0
        fav[colors[key]] += 1
    fav_color: str = ""
    count: int = 0
    for key in fav:
        if fav[key] > count:
            count = fav[key]
            fav_color = key
    return fav_color


def count(lst: list[str]) -> dict[str, int]:
    """Given list of strings, function returns a dict[str, int].

    Each key is a unique value in given list and each value associated
    is the count of the number of times that value appeared in the input list.
    """
    counter: dict[str, int] = {}
    for item in lst:
        if item not in counter:
            counter[item] = 0
        counter[item] += 1
    return counter