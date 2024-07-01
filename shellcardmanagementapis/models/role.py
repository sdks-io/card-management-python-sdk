# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class Role(object):

    """Implementation of the 'Role' model.

    TODO: type model description here.

    Attributes:
        role_name (str): Role Name of the user
        is_customer_admin (bool): Whether the role is an administrator.
        is_customer_user (bool): Whether the role is a customer user.
        is_shell_admin (bool): True if the role is Shell user, else false.
        is_service_account (bool): True/False. True if the role is Service
            accounts, else false.
        is_user_admin (bool): True/False. True, if the role allows user
            administration, else false.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "role_name": 'RoleName',
        "is_customer_admin": 'IsCustomerAdmin',
        "is_customer_user": 'IsCustomerUser',
        "is_shell_admin": 'IsShellAdmin',
        "is_service_account": 'IsServiceAccount',
        "is_user_admin": 'IsUserAdmin'
    }

    _optionals = [
        'role_name',
        'is_customer_admin',
        'is_customer_user',
        'is_shell_admin',
        'is_service_account',
        'is_user_admin',
    ]

    def __init__(self,
                 role_name=APIHelper.SKIP,
                 is_customer_admin=True,
                 is_customer_user=False,
                 is_shell_admin=False,
                 is_service_account=False,
                 is_user_admin=True):
        """Constructor for the Role class"""

        # Initialize members of the class
        if role_name is not APIHelper.SKIP:
            self.role_name = role_name 
        self.is_customer_admin = is_customer_admin 
        self.is_customer_user = is_customer_user 
        self.is_shell_admin = is_shell_admin 
        self.is_service_account = is_service_account 
        self.is_user_admin = is_user_admin 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        role_name = dictionary.get("RoleName") if dictionary.get("RoleName") else APIHelper.SKIP
        is_customer_admin = dictionary.get("IsCustomerAdmin") if dictionary.get("IsCustomerAdmin") else True
        is_customer_user = dictionary.get("IsCustomerUser") if dictionary.get("IsCustomerUser") else False
        is_shell_admin = dictionary.get("IsShellAdmin") if dictionary.get("IsShellAdmin") else False
        is_service_account = dictionary.get("IsServiceAccount") if dictionary.get("IsServiceAccount") else False
        is_user_admin = dictionary.get("IsUserAdmin") if dictionary.get("IsUserAdmin") else True
        # Return an object of this model
        return cls(role_name,
                   is_customer_admin,
                   is_customer_user,
                   is_shell_admin,
                   is_service_account,
                   is_user_admin)
