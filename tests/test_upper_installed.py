from cogent3 import get_app


def test_app_installed():
    app = get_app("to_upper")
    got = app("dfgh")
    assert got == "DFGH"
