# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class Address(object):

    """Implementation of the 'Address' model.

    TODO: type model description here.

    Attributes:
        address_id (int): Address Id in cards platform.
        address_line_1 (str): Address line1
        address_line_2 (str): Address line2
        address_line_3 (str): AddressLine3
        zip_code (str): ZipCode
        city (str): City
        region_id (int): Region Id of the address.
        country_iso_code (str): Country ISO code of the address
        country (str): Country for the address
        telephone (str): Telephone number of the address contact
        email_address (str): Email address of the address contact
        fax (str): Fax number of the address contact

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_id": 'AddressId',
        "address_line_1": 'AddressLine1',
        "address_line_2": 'AddressLine2',
        "address_line_3": 'AddressLine3',
        "zip_code": 'ZipCode',
        "city": 'City',
        "region_id": 'RegionId',
        "country_iso_code": 'CountryISOCode',
        "country": 'Country',
        "telephone": 'Telephone',
        "email_address": 'EmailAddress',
        "fax": 'Fax'
    }

    _optionals = [
        'address_id',
        'address_line_1',
        'address_line_2',
        'address_line_3',
        'zip_code',
        'city',
        'region_id',
        'country_iso_code',
        'country',
        'telephone',
        'email_address',
        'fax',
    ]

    _nullables = [
        'address_id',
        'address_line_1',
        'address_line_2',
        'address_line_3',
        'zip_code',
        'city',
        'region_id',
        'country_iso_code',
        'country',
        'telephone',
        'email_address',
        'fax',
    ]

    def __init__(self,
                 address_id=APIHelper.SKIP,
                 address_line_1=APIHelper.SKIP,
                 address_line_2=APIHelper.SKIP,
                 address_line_3=APIHelper.SKIP,
                 zip_code=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 region_id=APIHelper.SKIP,
                 country_iso_code=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 telephone=APIHelper.SKIP,
                 email_address=APIHelper.SKIP,
                 fax=APIHelper.SKIP):
        """Constructor for the Address class"""

        # Initialize members of the class
        if address_id is not APIHelper.SKIP:
            self.address_id = address_id 
        if address_line_1 is not APIHelper.SKIP:
            self.address_line_1 = address_line_1 
        if address_line_2 is not APIHelper.SKIP:
            self.address_line_2 = address_line_2 
        if address_line_3 is not APIHelper.SKIP:
            self.address_line_3 = address_line_3 
        if zip_code is not APIHelper.SKIP:
            self.zip_code = zip_code 
        if city is not APIHelper.SKIP:
            self.city = city 
        if region_id is not APIHelper.SKIP:
            self.region_id = region_id 
        if country_iso_code is not APIHelper.SKIP:
            self.country_iso_code = country_iso_code 
        if country is not APIHelper.SKIP:
            self.country = country 
        if telephone is not APIHelper.SKIP:
            self.telephone = telephone 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if fax is not APIHelper.SKIP:
            self.fax = fax 

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
        address_id = dictionary.get("AddressId") if "AddressId" in dictionary.keys() else APIHelper.SKIP
        address_line_1 = dictionary.get("AddressLine1") if "AddressLine1" in dictionary.keys() else APIHelper.SKIP
        address_line_2 = dictionary.get("AddressLine2") if "AddressLine2" in dictionary.keys() else APIHelper.SKIP
        address_line_3 = dictionary.get("AddressLine3") if "AddressLine3" in dictionary.keys() else APIHelper.SKIP
        zip_code = dictionary.get("ZipCode") if "ZipCode" in dictionary.keys() else APIHelper.SKIP
        city = dictionary.get("City") if "City" in dictionary.keys() else APIHelper.SKIP
        region_id = dictionary.get("RegionId") if "RegionId" in dictionary.keys() else APIHelper.SKIP
        country_iso_code = dictionary.get("CountryISOCode") if "CountryISOCode" in dictionary.keys() else APIHelper.SKIP
        country = dictionary.get("Country") if "Country" in dictionary.keys() else APIHelper.SKIP
        telephone = dictionary.get("Telephone") if "Telephone" in dictionary.keys() else APIHelper.SKIP
        email_address = dictionary.get("EmailAddress") if "EmailAddress" in dictionary.keys() else APIHelper.SKIP
        fax = dictionary.get("Fax") if "Fax" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(address_id,
                   address_line_1,
                   address_line_2,
                   address_line_3,
                   zip_code,
                   city,
                   region_id,
                   country_iso_code,
                   country,
                   telephone,
                   email_address,
                   fax)
