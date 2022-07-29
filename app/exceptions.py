class EmployeeException(Exception):
    pass


class InvalidCityException(EmployeeException):
    def __init__(self, message: str):
        super().__init__(message)
