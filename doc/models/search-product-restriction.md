
# Search Product Restriction

## Structure

`SearchProductRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `products` | [`List[ProductAllOf0]`](../../doc/models/product-all-of-0.md) | Optional | - |
| `product_groups` | [`List[ProductGroup]`](../../doc/models/product-group.md) | Optional | - |

## Example (as JSON)

```json
{
  "Products": [
    {
      "GlobalProductCode": "GlobalProductCode6",
      "Description": "Description8"
    },
    {
      "GlobalProductCode": "GlobalProductCode6",
      "Description": "Description8"
    }
  ],
  "ProductGroups": [
    {
      "ReferenceId": 82,
      "ProductGroupId": "ProductGroupId6",
      "Name": "Name0",
      "IsDefault": false,
      "IsFuelType": false
    }
  ]
}
```

