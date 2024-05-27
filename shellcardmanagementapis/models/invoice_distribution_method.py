# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class InvoiceDistributionMethod(object):

    """Implementation of the 'InvoiceDistributionMethod' model.

    TODO: type model description here.

    Attributes:
        is_primary (bool): If True then this distribution method is the
            default distribution method.
        frequency_type (str): Frequency type unit Id & description  E.g.:  1-
            Daily  2-Weekly  3-Monthly  4-Invoicing  6-Calendar quarter
        distribution_method (str): Invoice Distribution Method
            (Id-Description)  E.g.:  1-e-mail  2-Fax  3-Courier to Customer 
            4-Courier to Client  5-Print  6-FTP  7-SMS
        output_type (str): Invoice output type (Id - Description)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_primary": 'IsPrimary',
        "frequency_type": 'FrequencyType',
        "distribution_method": 'DistributionMethod',
        "output_type": 'OutputType'
    }

    _optionals = [
        'is_primary',
        'frequency_type',
        'distribution_method',
        'output_type',
    ]

    _nullables = [
        'frequency_type',
        'distribution_method',
        'output_type',
    ]

    def __init__(self,
                 is_primary=True,
                 frequency_type=APIHelper.SKIP,
                 distribution_method=APIHelper.SKIP,
                 output_type=APIHelper.SKIP):
        """Constructor for the InvoiceDistributionMethod class"""

        # Initialize members of the class
        self.is_primary = is_primary 
        if frequency_type is not APIHelper.SKIP:
            self.frequency_type = frequency_type 
        if distribution_method is not APIHelper.SKIP:
            self.distribution_method = distribution_method 
        if output_type is not APIHelper.SKIP:
            self.output_type = output_type 

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
        is_primary = dictionary.get("IsPrimary") if dictionary.get("IsPrimary") else True
        frequency_type = dictionary.get("FrequencyType") if "FrequencyType" in dictionary.keys() else APIHelper.SKIP
        distribution_method = dictionary.get("DistributionMethod") if "DistributionMethod" in dictionary.keys() else APIHelper.SKIP
        output_type = dictionary.get("OutputType") if "OutputType" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(is_primary,
                   frequency_type,
                   distribution_method,
                   output_type)
