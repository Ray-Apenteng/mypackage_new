from mypackage import myModule

def test_top_n():
    """
    make sure top_n works correctly
    """

    assert top_n ([8, 4, 3, 2, 7], 3) == [8, 7, 4], 'incorrect'
    assert top_n ([5, 10, 16, 3, 8, 1], 4) == [16, 10, 8, 5], 'incorrect'
    assert top_n ([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'