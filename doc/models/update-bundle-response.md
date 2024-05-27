
# Update Bundle Response

## Structure

`UpdateBundleResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | API Request Id |
| `status` | `str` | Optional | API Response Status |
| `errors` | [`ErrorDetails`](../../doc/models/error-details.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "RequestId4",
  "Status": "Status0",
  "Errors": {
    "Code": "Code4",
    "Title": "Title6",
    "Detail": "Detail6",
    "AdditionalInfo": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

