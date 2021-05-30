"""Module for custom exceptions."""


class AppInternalError(Exception):
    pass


class RequestError(AppInternalError):
    pass


class FileError(AppInternalError):
    pass
