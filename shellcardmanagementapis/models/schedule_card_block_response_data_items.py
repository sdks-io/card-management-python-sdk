# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class ScheduleCardBlockResponseDataItems(object):

    """Implementation of the 'ScheduleCardBlockResponseDataItems' model.

    Attributes:
        card_id (int): Unique Id of the card.
        from_date (str): Effective start date & time of Block / Unblock as
            updated in the intermediate queue table.   Format: yyyyMMdd HH:mm
            Eg: 20230512 12:30
        to_date (str): Effective end date & time of Block / Unblock as updated
            in the intermediate queue table.   Format: yyyyMMdd HH:mm Eg:
            20230512 14:30
        reference_id (int): Effective end date & time of Block / Unblock as
            updated in the intermediate queue table.   Format: yyyyMMdd HH:mm
            Eg: 20230512 14:30

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_id": 'CardId',
        "from_date": 'FromDate',
        "to_date": 'ToDate',
        "reference_id": 'ReferenceId'
    }

    _optionals = [
        'card_id',
        'from_date',
        'to_date',
        'reference_id',
    ]

    def __init__(self,
                 card_id=APIHelper.SKIP,
                 from_date=APIHelper.SKIP,
                 to_date=APIHelper.SKIP,
                 reference_id=APIHelper.SKIP):
        """Constructor for the ScheduleCardBlockResponseDataItems class"""

        # Initialize members of the class
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if from_date is not APIHelper.SKIP:
            self.from_date = from_date 
        if to_date is not APIHelper.SKIP:
            self.to_date = to_date 
        if reference_id is not APIHelper.SKIP:
            self.reference_id = reference_id 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        card_id = dictionary.get("CardId") if dictionary.get("CardId") else APIHelper.SKIP
        from_date = dictionary.get("FromDate") if dictionary.get("FromDate") else APIHelper.SKIP
        to_date = dictionary.get("ToDate") if dictionary.get("ToDate") else APIHelper.SKIP
        reference_id = dictionary.get("ReferenceId") if dictionary.get("ReferenceId") else APIHelper.SKIP
        # Return an object of this model
        return cls(card_id,
                   from_date,
                   to_date,
                   reference_id)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!r}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!r}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!r}, '
                f'reference_id={(self.reference_id if hasattr(self, "reference_id") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!s}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!s}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!s}, '
                f'reference_id={(self.reference_id if hasattr(self, "reference_id") else None)!s})')
