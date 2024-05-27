
# Summary of Bundle Response Data Items Card Bundles Items

## Structure

`SummaryOfBundleResponseDataItemsCardBundlesItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bundle_id` | `str` | Optional | Gateway assigned unique identifier for the Card Bundle. |
| `external_bundle_id` | `str` | Optional | External system allocated Card Bundle identifier for Card Bundle. |
| `description` | `str` | Optional | Card Bundle Description. |
| `total_cards` | `int` | Optional | No of Card PAN added to the card bundle. |

## Example (as JSON)

```json
{
  "BundleId": "BundleId0",
  "ExternalBundleId": "ExternalBundleId4",
  "Description": "Description8",
  "TotalCards": 126
}
```

