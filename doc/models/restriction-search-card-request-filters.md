
# Restriction Search Card Request Filters

## Structure

`RestrictionSearchCardRequestFilters`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86 for Philippines<br>5 for UK |
| `col_co_id` | `int` | Optional | Collecting Company Id (in GFN) of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1 for Philippines<br>5 for UK |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br>Optional if PayerId is passed else Mandatory<br>Example: GB000000123 |
| `payer_id` | `int` | Optional | Payer Id  of the selected payer.<br>Optional if PayerNumber is passed else Mandatory<br>Example: 123456 |
| `accounts` | [`Accounts`](../../doc/models/accounts.md) | Optional | - |
| `bundle_id` | `str` | Optional | Identifier of the Card bundle in Gateway.<br>Optional if cards list is given, else mandatory. |
| `cards` | [`List[RestrictionSearchCardRequestFiltersCardsItems]`](../../doc/models/restriction-search-card-request-filters-cards-items.md) | Optional | - |
| `include_location_restrictions` | `bool` | Optional | Whether to include location restriction of the cards in the response<br>**Default**: `False` |
| `include_inherited_limits` | `bool` | Optional | When True: service will return the inherited values for the usage limits (from card-program or account as available) when it is not overridden on the card.<br>**Default**: `False` |
| `include_bundle_details` | `bool` | Optional | When the value is True, API will return bundle Id associated with cards in the response, if available.<br>Note: Use ‘Null’ or ‘False’ for optimum performance. A delay in response is expected when set to ‘True’.<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "IncludeLocationRestrictions": false,
  "IncludeInheritedLimits": false,
  "IncludeBundleDetails": false,
  "ColCoCode": 32,
  "ColCoId": 18,
  "PayerNumber": "PayerNumber2",
  "PayerId": 66,
  "Accounts": {
    "AccountId": 28,
    "AccountNumber": "AccountNumber0"
  }
}
```

