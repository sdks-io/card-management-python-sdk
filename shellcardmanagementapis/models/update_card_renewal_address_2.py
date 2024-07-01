# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class UpdateCardRenewalAddress2(object):

    """Implementation of the 'UpdateCardRenewalAddress2' model.

    TODO: type model description here.

    Attributes:
        contact_name (str): Contact name Note: Mandatory when
            ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is
            ignored otherwise.   Max Length: 50
        contact_title (str): Title Max Length: 50
        company_name (str): Company name. Note: Mandatory when
            ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is
            ignored otherwise. Max Length: 50
        address_line (str): Address line 1,2 and 3 Note: Mandatory when
            ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is
            ignored otherwise. Max Length: 128 Note: -Each address line should
            be separated by “\r\n”.
        zip_code (str): ZipCode Note: Mandatory when
            ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is
            ignored otherwise. Max Length: 10
        city (str): City Note: Mandatory when ‘UseCustomerDefaultAddress’ is
            set to ‘false’. The field is ignored otherwise. Max Length: 40
        region_id (int): Region id of card.
        country_id (int): Country ID Note: Mandatory when
            ‘UseCustomerDefaultAddress’ is set to ‘false’. The field is
            ignored otherwise.
        email_address (str): Email Address    Max Length: 90  Note: -  Based
            on the international standard that there can be   • Max Length 64
            before the @ (the 'Local part’) =64(minimum of 1)  • Max Lenth
            after the (the domain) = 88 (Minimum of 2)
        phone_number (str): Phone number Optional Max Length: 16

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "contact_name": 'ContactName',
        "company_name": 'CompanyName',
        "address_line": 'AddressLine',
        "zip_code": 'ZipCode',
        "country_id": 'CountryID',
        "contact_title": 'ContactTitle',
        "city": 'City',
        "region_id": 'RegionID',
        "email_address": 'EmailAddress',
        "phone_number": 'PhoneNumber'
    }

    _optionals = [
        'contact_title',
        'city',
        'region_id',
        'email_address',
        'phone_number',
    ]

    def __init__(self,
                 contact_name=None,
                 company_name=None,
                 address_line=None,
                 zip_code=None,
                 country_id=None,
                 contact_title=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 region_id=APIHelper.SKIP,
                 email_address=APIHelper.SKIP,
                 phone_number=APIHelper.SKIP):
        """Constructor for the UpdateCardRenewalAddress2 class"""

        # Initialize members of the class
        self.contact_name = contact_name 
        if contact_title is not APIHelper.SKIP:
            self.contact_title = contact_title 
        self.company_name = company_name 
        self.address_line = address_line 
        self.zip_code = zip_code 
        if city is not APIHelper.SKIP:
            self.city = city 
        if region_id is not APIHelper.SKIP:
            self.region_id = region_id 
        self.country_id = country_id 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number 

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
        contact_name = dictionary.get("ContactName") if dictionary.get("ContactName") else None
        company_name = dictionary.get("CompanyName") if dictionary.get("CompanyName") else None
        address_line = dictionary.get("AddressLine") if dictionary.get("AddressLine") else None
        zip_code = dictionary.get("ZipCode") if dictionary.get("ZipCode") else None
        country_id = dictionary.get("CountryID") if dictionary.get("CountryID") else None
        contact_title = dictionary.get("ContactTitle") if dictionary.get("ContactTitle") else APIHelper.SKIP
        city = dictionary.get("City") if dictionary.get("City") else APIHelper.SKIP
        region_id = dictionary.get("RegionID") if dictionary.get("RegionID") else APIHelper.SKIP
        email_address = dictionary.get("EmailAddress") if dictionary.get("EmailAddress") else APIHelper.SKIP
        phone_number = dictionary.get("PhoneNumber") if dictionary.get("PhoneNumber") else APIHelper.SKIP
        # Return an object of this model
        return cls(contact_name,
                   company_name,
                   address_line,
                   zip_code,
                   country_id,
                   contact_title,
                   city,
                   region_id,
                   email_address,
                   phone_number)