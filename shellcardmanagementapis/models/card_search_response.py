# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.card import Card


class CardSearchResponse(object):

    """Implementation of the 'CardSearchResponse' model.

    Attributes:
        request_id (str): Unique request identifier passed from end user. This
            identifier helps in tracing a transaction
        status (str): Indicates overall status of the request. Allowed values:
            SUCCES, FAILED, PARTIAL_SUCCES
        data (List[Card]): The model property of type List[Card].
        page (int): Specifies the returned page of the results
        page_size (int): Specifies the number of records to be returned which
            could be less than the PageSize in the request
        total_pages (int): Specifies the total pages available in the result
        total_records (int): Specifies the total pages available in the result

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "status": 'Status',
        "data": 'Data',
        "page": 'Page',
        "page_size": 'PageSize',
        "total_pages": 'TotalPages',
        "total_records": 'TotalRecords'
    }

    _optionals = [
        'request_id',
        'status',
        'data',
        'page',
        'page_size',
        'total_pages',
        'total_records',
    ]

    _nullables = [
        'request_id',
        'status',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 data=APIHelper.SKIP,
                 page=APIHelper.SKIP,
                 page_size=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 total_records=APIHelper.SKIP):
        """Constructor for the CardSearchResponse class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if data is not APIHelper.SKIP:
            self.data = data 
        if page is not APIHelper.SKIP:
            self.page = page 
        if page_size is not APIHelper.SKIP:
            self.page_size = page_size 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 
        if total_records is not APIHelper.SKIP:
            self.total_records = total_records 

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
        request_id = dictionary.get("RequestId") if "RequestId" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("Status") if "Status" in dictionary.keys() else APIHelper.SKIP
        data = None
        if dictionary.get('Data') is not None:
            data = [Card.from_dictionary(x) for x in dictionary.get('Data')]
        else:
            data = APIHelper.SKIP
        page = dictionary.get("Page") if dictionary.get("Page") else APIHelper.SKIP
        page_size = dictionary.get("PageSize") if dictionary.get("PageSize") else APIHelper.SKIP
        total_pages = dictionary.get("TotalPages") if dictionary.get("TotalPages") else APIHelper.SKIP
        total_records = dictionary.get("TotalRecords") if dictionary.get("TotalRecords") else APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   status,
                   data,
                   page,
                   page_size,
                   total_pages,
                   total_records)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'data={(self.data if hasattr(self, "data") else None)!r}, '
                f'page={(self.page if hasattr(self, "page") else None)!r}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!r}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!r}, '
                f'total_records={(self.total_records if hasattr(self, "total_records") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'data={(self.data if hasattr(self, "data") else None)!s}, '
                f'page={(self.page if hasattr(self, "page") else None)!s}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!s}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!s}, '
                f'total_records={(self.total_records if hasattr(self, "total_records") else None)!s})')
