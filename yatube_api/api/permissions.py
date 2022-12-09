from rest_framework import permissions, status
from rest_framework.exceptions import APIException


class GenericAPIException(APIException):
    """
    raises API exceptions with custom messages and custom status codes
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'error'

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code


class CreateGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            raise GenericAPIException(
                detail='Добавлять группу может только админ!', status_code=405,
            )
        return True
