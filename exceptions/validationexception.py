class ValidationException(Exception):
    def __init__(self, errors=[],*args: object) -> None:
        super().__init__(*args)
        self.errors = errors