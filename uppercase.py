from cogent3.app.composable import define_app

@define_app
def to_upper(input: str) -> str:
    return input.upper()
