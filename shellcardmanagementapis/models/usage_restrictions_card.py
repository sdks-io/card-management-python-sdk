# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class UsageRestrictionsCard(object):

    """Implementation of the 'UsageRestrictionsCard' model.

    TODO: type model description here.

    Attributes:
        daily_spend (float): Maximum spend value (amount) allowed per day.
            Optional It allows null in the input field. If Values is passed as
            null, apply the card type limit. However, if the card type limit
            is NULL for the same field then No limit will be applied in
            Gateway.
        weekly_spend (float): Maximum spend value (amount) allowed per week.  
            Optional
        monthly_spend (float): Maximum spend value (amount) allowed per month.
            Optional
        per_transaction_spend (float): Maximum spend value (amount) allowed
            per transaction.   Optional
        annual_spend (float): Maximum spend value (amount) allowed per annum. 
            Optional
        life_time_spend (float): Maximum spend value (amount) allowed in
            card’s life time.   Optional
        daily_volume (float): Maximum volume (quantity) allowed per day.  
            Optional
        weekly_volume (float): Maximum volume (quantity) allowed per week.  
            Optional
        monthly_volume (float): Maximum volume (quantity) allowed per month.  
            Optional
        per_transaction_volume (float): Maximum volume (quantity) allowed per
            transaction.   Optional
        annual_volume (float): Maximum volume (quantity) allowed per annum.  
            Optional
        life_time_volume (float): Maximum volume (quantity) allowed in card’s
            life time.   Optional
        daily_transaction_count (float): Maximum number of transactions
            allowed per day.   Optional
        weekly_transaction_count (float): Maximum number of transactions
            allowed per week.   Optional
        monthly_transaction_count (float): Maximum number of transactions
            allowed per month.   Optional.
        annual_transaction_count (float): Maximum number of transactions
            allowed per annum.
        life_time_transaction_count (float): Maximum number of transactions
            allowed in card’s lifetime.   Optional

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "daily_spend": 'DailySpend',
        "weekly_spend": 'WeeklySpend',
        "monthly_spend": 'MonthlySpend',
        "per_transaction_spend": 'PerTransactionSpend',
        "annual_spend": 'AnnualSpend',
        "life_time_spend": 'LifeTimeSpend',
        "daily_volume": 'DailyVolume',
        "weekly_volume": 'WeeklyVolume',
        "monthly_volume": 'MonthlyVolume',
        "per_transaction_volume": 'PerTransactionVolume',
        "annual_volume": 'AnnualVolume',
        "life_time_volume": 'LifeTimeVolume',
        "daily_transaction_count": 'DailyTransactionCount',
        "weekly_transaction_count": 'WeeklyTransactionCount',
        "monthly_transaction_count": 'MonthlyTransactionCount',
        "annual_transaction_count": 'AnnualTransactionCount',
        "life_time_transaction_count": 'LifeTimeTransactionCount'
    }

    _optionals = [
        'daily_spend',
        'weekly_spend',
        'monthly_spend',
        'per_transaction_spend',
        'annual_spend',
        'life_time_spend',
        'daily_volume',
        'weekly_volume',
        'monthly_volume',
        'per_transaction_volume',
        'annual_volume',
        'life_time_volume',
        'daily_transaction_count',
        'weekly_transaction_count',
        'monthly_transaction_count',
        'annual_transaction_count',
        'life_time_transaction_count',
    ]

    _nullables = [
        'daily_spend',
        'weekly_spend',
        'monthly_spend',
        'per_transaction_spend',
        'annual_spend',
        'life_time_spend',
        'daily_volume',
        'weekly_volume',
        'monthly_volume',
        'annual_volume',
        'daily_transaction_count',
        'weekly_transaction_count',
        'monthly_transaction_count',
        'annual_transaction_count',
        'life_time_transaction_count',
    ]

    def __init__(self,
                 daily_spend=APIHelper.SKIP,
                 weekly_spend=APIHelper.SKIP,
                 monthly_spend=APIHelper.SKIP,
                 per_transaction_spend=APIHelper.SKIP,
                 annual_spend=APIHelper.SKIP,
                 life_time_spend=APIHelper.SKIP,
                 daily_volume=APIHelper.SKIP,
                 weekly_volume=APIHelper.SKIP,
                 monthly_volume=APIHelper.SKIP,
                 per_transaction_volume=APIHelper.SKIP,
                 annual_volume=APIHelper.SKIP,
                 life_time_volume=APIHelper.SKIP,
                 daily_transaction_count=APIHelper.SKIP,
                 weekly_transaction_count=APIHelper.SKIP,
                 monthly_transaction_count=APIHelper.SKIP,
                 annual_transaction_count=APIHelper.SKIP,
                 life_time_transaction_count=APIHelper.SKIP):
        """Constructor for the UsageRestrictionsCard class"""

        # Initialize members of the class
        if daily_spend is not APIHelper.SKIP:
            self.daily_spend = daily_spend 
        if weekly_spend is not APIHelper.SKIP:
            self.weekly_spend = weekly_spend 
        if monthly_spend is not APIHelper.SKIP:
            self.monthly_spend = monthly_spend 
        if per_transaction_spend is not APIHelper.SKIP:
            self.per_transaction_spend = per_transaction_spend 
        if annual_spend is not APIHelper.SKIP:
            self.annual_spend = annual_spend 
        if life_time_spend is not APIHelper.SKIP:
            self.life_time_spend = life_time_spend 
        if daily_volume is not APIHelper.SKIP:
            self.daily_volume = daily_volume 
        if weekly_volume is not APIHelper.SKIP:
            self.weekly_volume = weekly_volume 
        if monthly_volume is not APIHelper.SKIP:
            self.monthly_volume = monthly_volume 
        if per_transaction_volume is not APIHelper.SKIP:
            self.per_transaction_volume = per_transaction_volume 
        if annual_volume is not APIHelper.SKIP:
            self.annual_volume = annual_volume 
        if life_time_volume is not APIHelper.SKIP:
            self.life_time_volume = life_time_volume 
        if daily_transaction_count is not APIHelper.SKIP:
            self.daily_transaction_count = daily_transaction_count 
        if weekly_transaction_count is not APIHelper.SKIP:
            self.weekly_transaction_count = weekly_transaction_count 
        if monthly_transaction_count is not APIHelper.SKIP:
            self.monthly_transaction_count = monthly_transaction_count 
        if annual_transaction_count is not APIHelper.SKIP:
            self.annual_transaction_count = annual_transaction_count 
        if life_time_transaction_count is not APIHelper.SKIP:
            self.life_time_transaction_count = life_time_transaction_count 

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
        daily_spend = dictionary.get("DailySpend") if "DailySpend" in dictionary.keys() else APIHelper.SKIP
        weekly_spend = dictionary.get("WeeklySpend") if "WeeklySpend" in dictionary.keys() else APIHelper.SKIP
        monthly_spend = dictionary.get("MonthlySpend") if "MonthlySpend" in dictionary.keys() else APIHelper.SKIP
        per_transaction_spend = dictionary.get("PerTransactionSpend") if "PerTransactionSpend" in dictionary.keys() else APIHelper.SKIP
        annual_spend = dictionary.get("AnnualSpend") if "AnnualSpend" in dictionary.keys() else APIHelper.SKIP
        life_time_spend = dictionary.get("LifeTimeSpend") if "LifeTimeSpend" in dictionary.keys() else APIHelper.SKIP
        daily_volume = dictionary.get("DailyVolume") if "DailyVolume" in dictionary.keys() else APIHelper.SKIP
        weekly_volume = dictionary.get("WeeklyVolume") if "WeeklyVolume" in dictionary.keys() else APIHelper.SKIP
        monthly_volume = dictionary.get("MonthlyVolume") if "MonthlyVolume" in dictionary.keys() else APIHelper.SKIP
        per_transaction_volume = dictionary.get("PerTransactionVolume") if dictionary.get("PerTransactionVolume") else APIHelper.SKIP
        annual_volume = dictionary.get("AnnualVolume") if "AnnualVolume" in dictionary.keys() else APIHelper.SKIP
        life_time_volume = dictionary.get("LifeTimeVolume") if dictionary.get("LifeTimeVolume") else APIHelper.SKIP
        daily_transaction_count = dictionary.get("DailyTransactionCount") if "DailyTransactionCount" in dictionary.keys() else APIHelper.SKIP
        weekly_transaction_count = dictionary.get("WeeklyTransactionCount") if "WeeklyTransactionCount" in dictionary.keys() else APIHelper.SKIP
        monthly_transaction_count = dictionary.get("MonthlyTransactionCount") if "MonthlyTransactionCount" in dictionary.keys() else APIHelper.SKIP
        annual_transaction_count = dictionary.get("AnnualTransactionCount") if "AnnualTransactionCount" in dictionary.keys() else APIHelper.SKIP
        life_time_transaction_count = dictionary.get("LifeTimeTransactionCount") if "LifeTimeTransactionCount" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(daily_spend,
                   weekly_spend,
                   monthly_spend,
                   per_transaction_spend,
                   annual_spend,
                   life_time_spend,
                   daily_volume,
                   weekly_volume,
                   monthly_volume,
                   per_transaction_volume,
                   annual_volume,
                   life_time_volume,
                   daily_transaction_count,
                   weekly_transaction_count,
                   monthly_transaction_count,
                   annual_transaction_count,
                   life_time_transaction_count)
