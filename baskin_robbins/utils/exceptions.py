"""
Exceptions
"""

from rest_framework import exceptions, status


class APIException(exceptions.APIException):
    def __init__(self):
        """
        Builds a detail dictionary for the error to give more information to API users.
        """
        detail_dict = {"detail": self.default_detail, "code": self.default_code}

        super().__init__(detail_dict)


class ProductNoInventory(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Product has no inventory"
    default_code = "product_no_inventory"
