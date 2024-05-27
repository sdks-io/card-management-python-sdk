
# Summary of Bundle Response Data Items

## Structure

`SummaryOfBundleResponseDataItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `int` | Optional | Payer Id of the bundles and cards.<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number of the bundles and cards.<br>Example: GB000000123 |
| `account_id` | `int` | Optional | Account ID of the bundle.<br>Example: 123456 |
| `account_number` | `str` | Optional | Account Number of the bundle.<br>Example: GB000000123 |
| `count_of_cards_not_in_bundle` | `int` | Optional | Count of cards that are not part of the bundle in a given account. |
| `card_bundles` | [`List[SummaryOfBundleResponseDataItemsCardBundlesItems]`](../../doc/models/summary-of-bundle-response-data-items-card-bundles-items.md) | Optional | List of Card Bundles |

## Example (as JSON)

```json
{
  "PayerId": 102,
  "PayerNumber": "PayerNumber6",
  "AccountId": 162,
  "AccountNumber": "AccountNumber8",
  "CountOfCardsNotInBundle": 222
}
```

