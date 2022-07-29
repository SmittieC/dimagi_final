class EmployeeException(Exception):
    pass


class CityNotFoundException(EmployeeException):
    def __init__(self, message: str):
        super().__init__(message)
