from cogent3.app.composable import define_app


@define_app()
class to_upper:
    def main(self, data: str) -> str:
        return data.upper()
