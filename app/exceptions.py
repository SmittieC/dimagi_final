class EmployeeException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class CityNotFoundException(EmployeeException):
    def __init__(self, message: str):
        super().__init__(message)
