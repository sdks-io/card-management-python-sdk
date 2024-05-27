
# Create Bundle Request

## Structure

`CreateBundleRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `col_co_id` | `int` | Optional | Collecting Company Id  of the selected payer.<br>Optional if ColCoCode is passed else Mandatory.<br>Example:<br>1-Philippines<br>5-UK |
| `payer_id` | `int` | Optional | Payer Id of the selected payer.<br>Optional if PayerNumber is passed else Mandatory<br>Example: 123456 |
| `account_id` | `int` | Optional | Account ID of the customer.<br>Either AccountId or AccountNumber or both must be passed.<br>Example: 123456 |
| `external_bundle_id` | `str` | Optional | Identifier of the bundle in external system.<br>Optional. |
| `description` | `str` | Required | A bundle description.<br>Optional. |
| `cards` | `List[str]` | Required | List of Card PANs to be added in the bundle.<br>Mandatory.<br>Example: 7002051006629890645<br>When PAN matches with multiple cards, the restriction will be applied on the latest issued card. |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer.<br>Mandatory for serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other countries if ColCoID is provided.<br>Example:<br>86-Philippines<br>5-UK |
| `payer_number` | `str` | Optional | Payer Number (Ex: GB000000123) of the selected payer.<br>Optional if PayerId is passed else Mandatory |
| `account_number` | `str` | Optional | Account Number of the customer.<br>Either AccountId or AccountNumber or both must be passed.<br>Example: GB000000123 |
| `restrictions` | [`CreateBundleRequestRestrictions`](../../doc/models/create-bundle-request-restrictions.md) | Optional | Restrictions to be applied on the bundle.<br>Mandatory |

## Example (as JSON)

```json
{
  "ColCoId": 246,
  "PayerId": 38,
  "AccountId": 98,
  "ExternalBundleId": "ExternalBundleId8",
  "Description": "Description4",
  "Cards": [
    "Cards3",
    "Cards2",
    "Cards1"
  ],
  "ColCoCode": 4
}
```

