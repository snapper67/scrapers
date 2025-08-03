# Search API
## URL
https://www.chefswarehouse.com/products/dairy-and-eggs/dairy-products//search

## Payload
```json
{
    "search": {
        "page": 2,
        "pageSize": 15,
        "includeZStockingItems": false,
        "facets": [],
        "sortBy": null,
        "direction": null
    }
}
```

## Response
```json
{
    "facets": [
        {
            "name": "DietaryPreferences",
            "displayName": "Dietary Preference",
            "values": [
                {
                    "value": "Contains Nuts",
                    "displayName": "Contains Nuts",
                    "count": 12
                },
                {
                    "value": "CowMilk",
                    "displayName": "Cow Milk",
                    "count": 58
                },
                {
                    "value": "Pasteurized",
                    "displayName": "Pasteurized",
                    "count": 2
                }
            ]
        }
    ],
    "results": [
        {
            "brand": "Cabot Creamery",
            "category": "Sour Cream & Crème Fraiche",
            "subcategory": "Dairy Products",
            "subsubcategory": "Sour Cream & Crème Fraiche",
            "sku": "10303734",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_10303734-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "76594423",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "6 x 5 LB Case",
                    "inStock": 172,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "10303734",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_10303734-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "6 x 5 LB Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                },
                {
                    "code": "JDE_10303734-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "76594423",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "6 x 5 LB Case",
                    "inStock": 1035,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "10303734",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_10303734-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "6 x 5 LB Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "10303734",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            },
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_10303734-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "6 x 5 LB Case",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Cabot+Creamery",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_280ba5f6-e6ab-4d0e-b5be-43e48217d57d_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Sour Cream",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/sour-cream-crème-fraiche/10303734_0.jpg",
            "url": "/products/10303734/",
            "altImage": null
        },
        {
            "brand": "Grand Reserve",
            "category": "Milk & Cream",
            "subcategory": "Milk & Cream",
            "subsubcategory": "Heavy Cream",
            "sku": "DM116",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_DM116-200001",
                    "brokenCaseFlag": "002",
                    "primaryUnitOfMeasureCode": "PC",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "1303767",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "1 Quart Each",
                    "inStock": 7126,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "DM116",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_DM116-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "PC",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "1 Quart Each",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": "Top Pick",
                        "color": "cyan-700"
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "DM116",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Piece",
                        "options": [
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_DM116-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "PC",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "1 Quart Each",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Grand+Reserve",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_addd42f2-60bc-4640-ada1-923651e522cf_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "40% Heavy Cream",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/heavy-cream/dm116_0.jpg",
            "url": "/products/DM116/",
            "altImage": null
        },
        {
            "brand": "Magnolia",
            "category": "Milk & Cream",
            "subcategory": "Dairy Products",
            "subsubcategory": "Milk & Cream",
            "sku": "GD205",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_GD205-200001",
                    "brokenCaseFlag": "001",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "1298427",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "24x14 Oz Case",
                    "inStock": 66,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "GD205",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_GD205-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "24x14 Oz Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "GD205",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_GD205-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "24x14 Oz Case",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Magnolia",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_45ca9c0b-e491-4d56-9c18-1382aab8887a_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Sweetened Condensed Milk",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/milk-cream/gd205_0.jpg",
            "url": "/products/GD205/",
            "altImage": null
        },
        {
            "brand": "Oatly",
            "category": "Plant Based Dairy ",
            "subcategory": "Plant Based Dairy ",
            "subsubcategory": "Plant Based Dairy",
            "sku": "10615236",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_10615236-200001",
                    "brokenCaseFlag": "001",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "9492028",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "12 x 32 Oz Case",
                    "inStock": 2176,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "10615236",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_10615236-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "12 x 32 Oz Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "10615236",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_10615236-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "12 x 32 Oz Case",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Oatly",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_3a2c3494-3d85-4b39-a8af-76288cab1de4_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Barista Oat Milk",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/plant-based-dairy2/10615236_0.jpg",
            "url": "/products/10615236/",
            "altImage": null
        },
        {
            "brand": "Byrne Dairy",
            "category": "Milk & Cream",
            "subcategory": "Dairy Products",
            "subsubcategory": "Milk & Cream",
            "sku": "DM120",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_DM120-200001",
                    "brokenCaseFlag": "002",
                    "primaryUnitOfMeasureCode": "PC",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "60361",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "1 Quart Each",
                    "inStock": 27418,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "DM120",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_DM120-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "PC",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "1 Quart Each",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "DM120",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Piece",
                        "options": [
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_DM120-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "PC",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "1 Quart Each",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Byrne+Dairy",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_84d68308-17b2-44fb-b1a5-a817915598b0_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "40% Heavy Cream UHT",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/milk-cream/dm120_0.jpg",
            "url": "/products/DM120/",
            "altImage": null
        },
        {
            "brand": "Smithfield",
            "category": "Cream Cheese ",
            "subcategory": "Loaves, Slices, & Shreds ",
            "subsubcategory": "Cream Cheese",
            "sku": "CC230",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_CC230-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "244128",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "10 x 3 LB Case",
                    "inStock": 0,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "CC230",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_CC230-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "10 x 3 LB Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                },
                {
                    "code": "JDE_CC230-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "244128",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "10 x 3 LB Case",
                    "inStock": 0,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "CC230",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_CC230-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "10 x 3 LB Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "CC230",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            },
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_CC230-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "10 x 3 LB Case",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Smithfield",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_fefa5b0b-8f38-432b-bf42-e5c5273e4d0d_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Cream Cheese",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/cream-cheese/cc230_0.jpg",
            "url": "/products/CC230/",
            "altImage": null
        },
        {
            "brand": "Grand Reserve",
            "category": "Sour Cream & Crème Fraiche",
            "subcategory": "Dairy Products",
            "subsubcategory": "Sour Cream & Crème Fraiche",
            "sku": "D112",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_D112-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "76594423",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "4 x 3 LB Case",
                    "inStock": 272,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "D112",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_D112-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "4 x 3 LB Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": "Top Pick",
                        "color": "cyan-700"
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                },
                {
                    "code": "JDE_D112-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "76594423",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "4 x 3 LB Case",
                    "inStock": 1090,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "D112",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_D112-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "4 x 3 LB Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": "Top Pick",
                        "color": "cyan-700"
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "D112",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            },
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_D112-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "4 x 3 LB Case",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Grand+Reserve",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_0b38c3c9-d2ee-4168-9804-f04f1507737c_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Crème Fraiche",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/sour-cream-crème-fraiche/d112_0.jpg",
            "url": "/products/D112/",
            "altImage": null
        },
        {
            "brand": "Grand Reserve",
            "category": "Milk & Cream",
            "subcategory": "Milk & Cream",
            "subsubcategory": "Heavy Cream",
            "sku": "DM115",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_DM115-200001",
                    "brokenCaseFlag": "002",
                    "primaryUnitOfMeasureCode": "PC",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "1303767",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "24x1 QT Piece",
                    "inStock": 7368,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "DM115",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_DM115-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "PC",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "24x1 QT Piece",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": "Top Pick",
                        "color": "cyan-700"
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "DM115",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Piece",
                        "options": [
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_DM115-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "PC",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "24x1 QT Piece",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Grand+Reserve",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_61637446-ad45-47ad-aa32-c102c930e344_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "36% Heavy Cream Quart",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/heavy-cream/dm115_0.jpg",
            "url": "/products/DM115/",
            "altImage": null
        },
        {
            "brand": "Ryt-Way",
            "category": "Milk & Cream",
            "subcategory": "Dairy Products",
            "subsubcategory": "Milk & Cream",
            "sku": "GD218N",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_GD218N-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "106366",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "6x5 LB Case BC",
                    "inStock": 111,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "GD218N",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_GD218N-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "6x5 LB Case BC",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                },
                {
                    "code": "JDE_GD218N-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "106366",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "6x5 LB Case BC",
                    "inStock": 668,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "GD218N",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_GD218N-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "6x5 LB Case BC",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "GD218N",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            },
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_GD218N-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "6x5 LB Case BC",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Ryt-Way",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_7ec642a7-7097-45a1-83de-210b25cee6a2_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Non-Fat Instant Milk Powder",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/milk-cream/gd218n_0.jpg",
            "url": "/products/GD218N/",
            "altImage": null
        },
        {
            "brand": "Wuthrich",
            "category": "Butter",
            "subcategory": "Butter",
            "subsubcategory": "Butter",
            "sku": "BB101",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_BB101-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "1143804",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "4x5 LB TUB BC",
                    "inStock": 258,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "BB101",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_BB101-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "4x5 LB TUB BC",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                },
                {
                    "code": "JDE_BB101-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "1143804",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "4x5 LB TUB BC",
                    "inStock": 1032,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "BB101",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_BB101-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "4x5 LB TUB BC",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "BB101",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            },
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_BB101-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "4x5 LB TUB BC",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Wuthrich",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_d906d96d-e6dc-4d17-a26c-6ebda0c811a5_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Clarified Butter",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/butter/bb101_0.jpg",
            "url": "/products/BB101/",
            "altImage": null
        },
        {
            "brand": "Califia Farms",
            "category": "Plant Based Dairy ",
            "subcategory": "Plant Based Dairy ",
            "subsubcategory": "Plant Based Dairy",
            "sku": "10522662N",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_10522662N-200001",
                    "brokenCaseFlag": "001",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "1118300",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "12x32 Oz Case",
                    "inStock": 2216,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "10522662N",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_10522662N-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "12x32 Oz Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "10522662N",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_10522662N-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "12x32 Oz Case",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Califia+Farms",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_0e25af67-1123-4e4d-ba7d-1f8b79a3006d_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Oat Barista Blend",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/plant-based-dairy2/10522662n_0.jpg",
            "url": "/products/10522662N/",
            "altImage": null
        },
        {
            "brand": "Alp Senn",
            "category": "Cream Cheese ",
            "subcategory": "Swiss & Alpine Style ",
            "subsubcategory": "Cream Cheese",
            "sku": "108601",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": true,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_108601-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "50226",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "2 x 6 LB Case",
                    "inStock": 122,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "108601",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_108601-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "2 x 6 LB Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                },
                {
                    "code": "JDE_108601-200001",
                    "brokenCaseFlag": "003",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "50226",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "2 x 6 LB Case",
                    "inStock": 244,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "108601",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_108601-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "2 x 6 LB Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "108601",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            },
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_108601-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "2 x 6 LB Case",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Alp+Senn",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_9ef475be-8616-4c01-b367-bf6a2c78edfb_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Gruyere Cheese",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/cream-cheese/108601_0.jpg",
            "url": "/products/108601/",
            "altImage": null
        },
        {
            "brand": "Grand Crest",
            "category": "Milk & Cream",
            "subcategory": "Dairy Products",
            "subsubcategory": "Milk & Cream",
            "sku": "GD206",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_GD206-200001",
                    "brokenCaseFlag": "001",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "106366",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "24 x 12 Oz Case",
                    "inStock": 134,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "GD206",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_GD206-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "24 x 12 Oz Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "GD206",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_GD206-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "24 x 12 Oz Case",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Grand+Crest",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_bd9099b4-f8a9-43a1-9731-40b387b981b4_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Evaporated Milk",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/milk-cream/gd206_0.jpg",
            "url": "/products/GD206/",
            "altImage": null
        },
        {
            "brand": "Skotidakis",
            "category": "Yogurt & Cottage Cheese",
            "subcategory": "Dairy Products",
            "subsubcategory": "Yogurt & Cottage Cheese",
            "sku": "104130",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_104130-200001",
                    "brokenCaseFlag": "002",
                    "primaryUnitOfMeasureCode": "PC",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "PC",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "51278",
                        "productionItem": false
                    },
                    "text": "Piece",
                    "weight": "1x11 LB Piece",
                    "inStock": 580,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "104130",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Piece",
                                "options": [
                                    {
                                        "text": "Piece",
                                        "value": "Piece"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_104130-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "PC",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "1x11 LB Piece",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "104130",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Piece",
                        "options": [
                            {
                                "text": "Piece",
                                "value": "Piece"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_104130-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "PC",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "1x11 LB Piece",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Skotidakis",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_6608b0f1-474d-48fc-949e-b9ee95584da5_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Kontos 9% Milk Fat Greek Yogurt",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/yogurt-cottage-cheese/104130_0.jpg",
            "url": "/products/104130/",
            "altImage": null
        },
        {
            "brand": "Coco Lopez",
            "category": "Plant Based Dairy",
            "subcategory": "Dairy Products",
            "subsubcategory": "Plant Based Dairy",
            "sku": "927680",
            "description": null,
            "isFrozen": false,
            "hasDualTolerance": false,
            "isRestricted": false,
            "variants": [
                {
                    "code": "JDE_927680-200001",
                    "brokenCaseFlag": "001",
                    "primaryUnitOfMeasureCode": "CS",
                    "secondaryUnitOfMeasureCode": null,
                    "tertiaryUnitOfMeasureCode": null,
                    "quaternaryUnitOfMeasureCode": null,
                    "packSize": null,
                    "metadata": {
                        "unitOfMeasure": "CS",
                        "productKey": null,
                        "productClassificationCode": null,
                        "chefItemFlag": false,
                        "bto": false,
                        "supermarket": false,
                        "stockingType": "P",
                        "lineType": "S",
                        "vendorId": "388551",
                        "productionItem": false
                    },
                    "text": "Case",
                    "weight": "25 x 15 Oz Case",
                    "inStock": 211,
                    "isReserve": false,
                    "isRestricted": false,
                    "isDropShipRestricted": false,
                    "notifyFormPrefill": [
                        {
                            "field": "product.itemNumber",
                            "prefill": {
                                "value": "927680",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uom",
                            "prefill": {
                                "value": "Case",
                                "options": [
                                    {
                                        "text": "Case",
                                        "value": "Case"
                                    }
                                ]
                            }
                        },
                        {
                            "field": "variant.code",
                            "prefill": {
                                "value": "JDE_927680-200001",
                                "options": null
                            }
                        },
                        {
                            "field": "product.uomcode",
                            "prefill": {
                                "value": "CS",
                                "options": null
                            }
                        },
                        {
                            "field": "product.packSize",
                            "prefill": {
                                "value": "25 x 15 Oz Case",
                                "options": null
                            }
                        }
                    ],
                    "stockingType": "P",
                    "checkAvailabilityFlag": true,
                    "businessUnit": null,
                    "isSecondaryBusinessUnit": false,
                    "businessUnitModel": {
                        "id": "200001",
                        "type": 0,
                        "crossDockRouteCode": null
                    },
                    "sellByMultiple": 1,
                    "cutInstructions1": null,
                    "cutInstructions2": null,
                    "customerFacingName": null,
                    "cutOffMessage": "",
                    "tag1": {
                        "name": null,
                        "color": null
                    },
                    "tag2": {
                        "name": null,
                        "color": null
                    },
                    "specialOrderFlag": false,
                    "isAvailabilityChecked": false,
                    "isExpired": false,
                    "displayOnlyCatchWeight": false,
                    "minQuantity": 1,
                    "maxQuantity": 10000,
                    "minMaxExpirationDate": null,
                    "itemRestriction": null,
                    "isSubsRestricted": false
                }
            ],
            "unableToBeAddedOrShownInOrderGuide": false,
            "salePrice": false,
            "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
            "minimumQuantityWarningMessage": null,
            "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
            "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
            "notifyFormPrefill": [
                {
                    "field": "product.itemNumber",
                    "prefill": {
                        "value": "927680",
                        "options": null
                    }
                },
                {
                    "field": "product.uom",
                    "prefill": {
                        "value": "Case",
                        "options": [
                            {
                                "text": "Case",
                                "value": "Case"
                            }
                        ]
                    }
                },
                {
                    "field": "variant.code",
                    "prefill": {
                        "value": "JDE_927680-200001",
                        "options": null
                    }
                },
                {
                    "field": "product.uomcode",
                    "prefill": {
                        "value": "CS",
                        "options": null
                    }
                },
                {
                    "field": "product.packSize",
                    "prefill": {
                        "value": "25 x 15 Oz Case",
                        "options": null
                    }
                }
            ],
            "brandSearchQuery": "/search/?q=Coco+Lopez",
            "trackingInfo": {
                "id": null,
                "query": "",
                "hitId": "Chefs_Web_ContentTypes_Commerce_ProductData/CatalogContent_300f0f0d-6b8d-4ddb-8f2e-580471d4275f_en"
            },
            "similarProductSliders": [],
            "weightDescription": null,
            "name": "Cream of Coconut",
            "imageUrl": "https://www.chefswarehouse.com/siteassets/pim-images/plant-based-dairy2/927680_0.jpg",
            "url": "/products/927680/",
            "altImage": null
        }
    ],
    "suggestedSearches": null,
    "total": 213,
    "queryId": null,
    "abTestVariantID": 0,
    "abTestID": 0,
    "nextPageToken": null,
    "filters": null,
    "attributionToken": null,
    "googleEventResultIds": null
}
```
# Sub Category
##

## Response
{
    "contentLink": {
        "id": 1073742226,
        "workId": 0,
        "guidValue": "141f2371-7a5f-4fec-9dcc-e4ebe1050973",
        "providerName": "CatalogContent",
        "url": "/products/meat-and-poultry/"
    },
    "name": "Meat & Poultry",
    "language": {
        "link": "/products/meat-and-poultry/",
        "displayName": "English",
        "name": "en"
    },
    "contentType": [
        "Node",
        "CategoryData"
    ],
    "routeSegment": "meat-and-poultry",
    "url": "/products/meat-and-poultry/",
    "displayName": "Meat & Poultry",
    "visibleInMenu": true,
    "thumbnailImage": {
        "id": 5156,
        "workId": 0,
        "guidValue": "a64e30a6-d512-47e7-a45e-58e7ca9c74f2",
        "url": "/siteassets/meat-poultry_330.png",
        "expanded": {
            "contentLink": {
                "id": 5156,
                "workId": 0,
                "guidValue": "a64e30a6-d512-47e7-a45e-58e7ca9c74f2",
                "url": "/siteassets/meat-poultry_330.png"
            },
            "name": "Meat & Poultry_330.png",
            "language": {
                "link": "/siteassets/meat-poultry_330.png",
                "displayName": "Invariant Language (Invariant Country)",
                "name": ""
            },
            "existingLanguages": [],
            "contentType": [
                "Image",
                "Media",
                "ImageFile"
            ],
            "parentLink": {
                "id": 3,
                "workId": 0,
                "guidValue": "e56f85d0-e833-4e02-976a-2d11fe4d598c"
            },
            "routeSegment": "meat-poultry_330.png",
            "url": "/siteassets/meat-poultry_330.png",
            "changed": "2022-02-14T15:14:55Z",
            "created": "2022-02-14T15:14:55Z",
            "startPublish": "2022-02-14T15:14:55Z",
            "saved": "2022-02-14T15:14:55Z",
            "status": "Published",
            "category": [],
            "pimberlyAssetUrl": "",
            "alt": "",
            "hasBeenConvertedToWebp": null,
            "hasPreviouslyFailedWebpConversion": null,
            "largeThumbnail": "",
            "authRequired": false,
            "currentUser": {
                "sessionId": "9d0b0137-15fd-4b7b-bcbd-870f9853948a",
                "algoliaIndexName": "Variants",
                "userName": "",
                "displayName": "",
                "customerContactId": "6c98d90c-1d9a-41dd-b7c3-a293438b34a7",
                "isAuthenticated": false,
                "isPunchoutSession": false,
                "isCSRUser": false,
                "validStockingTypes": [
                    "J",
                    "P",
                    "U"
                ],
                "customerStatus": {
                    "canOrder": false,
                    "shouldCheckCreditBalance": false,
                    "creditBalance": 0,
                    "errors": []
                },
                "permissions": {
                    "canViewOrders": false,
                    "canViewOrderGuides": false,
                    "canViewCatalog": false,
                    "userRole": "user"
                },
                "role": "user",
                "createdSessionDate": "2025-07-25T22:37:04.6700508Z",
                "isImpersonationActive": false,
                "hidePricing": false,
                "showInvoices": false,
                "websiteUrl": "https://www.chefswarehouse.com",
                "orderOnlyFromOrderGuideRestriction": false
            },
            "site": {
                "name": "Chefs'  Warehouse"
            }
        }
    },
    "sortOrder": 2,
    "cardImage": {
        "id": 5156,
        "workId": 0,
        "guidValue": "a64e30a6-d512-47e7-a45e-58e7ca9c74f2",
        "url": "/siteassets/meat-poultry_330.png",
        "expanded": {
            "contentLink": {
                "id": 5156,
                "workId": 0,
                "guidValue": "a64e30a6-d512-47e7-a45e-58e7ca9c74f2",
                "url": "/siteassets/meat-poultry_330.png"
            },
            "name": "Meat & Poultry_330.png",
            "language": {
                "link": "/siteassets/meat-poultry_330.png",
                "displayName": "Invariant Language (Invariant Country)",
                "name": ""
            },
            "existingLanguages": [],
            "contentType": [
                "Image",
                "Media",
                "ImageFile"
            ],
            "parentLink": {
                "id": 3,
                "workId": 0,
                "guidValue": "e56f85d0-e833-4e02-976a-2d11fe4d598c"
            },
            "routeSegment": "meat-poultry_330.png",
            "url": "/siteassets/meat-poultry_330.png",
            "changed": "2022-02-14T15:14:55Z",
            "created": "2022-02-14T15:14:55Z",
            "startPublish": "2022-02-14T15:14:55Z",
            "saved": "2022-02-14T15:14:55Z",
            "status": "Published",
            "category": [],
            "pimberlyAssetUrl": "",
            "alt": "",
            "hasBeenConvertedToWebp": null,
            "hasPreviouslyFailedWebpConversion": null,
            "largeThumbnail": "",
            "authRequired": false,
            "currentUser": {
                "sessionId": "9d0b0137-15fd-4b7b-bcbd-870f9853948a",
                "algoliaIndexName": "Variants",
                "userName": "",
                "displayName": "",
                "customerContactId": "6c98d90c-1d9a-41dd-b7c3-a293438b34a7",
                "isAuthenticated": false,
                "isPunchoutSession": false,
                "isCSRUser": false,
                "validStockingTypes": [
                    "J",
                    "P",
                    "U"
                ],
                "customerStatus": {
                    "canOrder": false,
                    "shouldCheckCreditBalance": false,
                    "creditBalance": 0,
                    "errors": []
                },
                "permissions": {
                    "canViewOrders": false,
                    "canViewOrderGuides": false,
                    "canViewCatalog": false,
                    "userRole": "user"
                },
                "role": "user",
                "createdSessionDate": "2025-07-25T22:37:04.6700508Z",
                "isImpersonationActive": false,
                "hidePricing": false,
                "showInvoices": false,
                "websiteUrl": "https://www.chefswarehouse.com",
                "orderOnlyFromOrderGuideRestriction": false
            },
            "site": {
                "name": "Chefs'  Warehouse"
            }
        }
    },
    "rightContentArea": [
        {
            "displayOption": "",
            "contentLink": {
                "id": 497086,
                "workId": 0,
                "guidValue": "21ccfabe-f322-4933-9a7f-bee404d9bf80",
                "expanded": {
                    "contentLink": {
                        "id": 497086,
                        "workId": 0,
                        "guidValue": "21ccfabe-f322-4933-9a7f-bee404d9bf80"
                    },
                    "name": "Nav_Right_CTA_Freebird",
                    "language": {
                        "displayName": "English",
                        "name": "en"
                    },
                    "existingLanguages": [
                        {
                            "displayName": "English",
                            "name": "en"
                        }
                    ],
                    "masterLanguage": {
                        "displayName": "English",
                        "name": "en"
                    },
                    "contentType": [
                        "Block",
                        "CallToActionBlock"
                    ],
                    "parentLink": {
                        "id": 497080,
                        "workId": 0,
                        "guidValue": "29aa6bbd-6ac7-4025-9253-5ca12794e6c9"
                    },
                    "changed": "2025-06-23T16:58:10Z",
                    "created": "2025-06-23T16:56:32Z",
                    "startPublish": "2025-06-30T07:00:00Z",
                    "saved": "2025-06-30T20:45:45Z",
                    "status": "Published",
                    "category": [],
                    "aspectRatio": "16/9",
                    "desktopImage": {
                        "id": 3029,
                        "workId": 0,
                        "guidValue": "763790e5-66c0-4443-8294-a4ec6e14c210",
                        "providerName": "bynder-assets-provider"
                    },
                    "mobileImage": null,
                    "heading": "",
                    "description": "<p><strong><span><span class=\"ui-provider a b c d e f g h i j k l m n o p q r s t u v w x y z ab ac ae af ag ah ai aj ak\" dir=\"ltr\">FreeBird chicken begins with vegetarian-fed poultry never given antibiotics or growth hormones.</span></span></strong></p>\n<p><a href=\"/shop-freebird/\" title=\"Shop Now\" class=\"btn btn-primary\">Shop Now</a></p>",
                    "linkColorScheme": "",
                    "backgroundColor": "cyan-700",
                    "imagePositionHorizontal": "left",
                    "imagePositionVertical": "top",
                    "viewModel": {
                        "aspectRatio": "16/9",
                        "desktopImageUrl": "https://media.chefswarehouse.com/transform/9201b990-3d1e-41ea-b66b-7d4259e976f4/Freebird-Logo_walzog_Roasted-Chicken_633?io=transform%3Afit%2Cwidth%3A1400",
                        "mobileImageUrl": "https://media.chefswarehouse.com/transform/9201b990-3d1e-41ea-b66b-7d4259e976f4/Freebird-Logo_walzog_Roasted-Chicken_633?io=transform%3Afit%2Cwidth%3A767",
                        "heading": "",
                        "description": "<p><strong><span><span class=\"ui-provider a b c d e f g h i j k l m n o p q r s t u v w x y z ab ac ae af ag ah ai aj ak\" dir=\"ltr\">FreeBird chicken begins with vegetarian-fed poultry never given antibiotics or growth hormones.</span></span></strong></p>\n<p><a href=\"/link/7012cb676e544276af87311733354b4f.aspx\" title=\"Shop Now\" class=\"btn btn-primary\">Shop Now</a></p>",
                        "linkCssClass": "btn btn-secondary btn-outline",
                        "backgroundColor": "cyan-700",
                        "imagePositionHorizontal": "left",
                        "imagePositionVertical": "top",
                        "contentLink": "497086",
                        "contentType": [
                            "Block",
                            "CallToActionBlock"
                        ]
                    },
                    "authRequired": false,
                    "currentUser": {
                        "sessionId": "9d0b0137-15fd-4b7b-bcbd-870f9853948a",
                        "algoliaIndexName": "Variants",
                        "userName": "",
                        "displayName": "",
                        "customerContactId": "6c98d90c-1d9a-41dd-b7c3-a293438b34a7",
                        "isAuthenticated": false,
                        "isPunchoutSession": false,
                        "isCSRUser": false,
                        "validStockingTypes": [
                            "J",
                            "P",
                            "U"
                        ],
                        "customerStatus": {
                            "canOrder": false,
                            "shouldCheckCreditBalance": false,
                            "creditBalance": 0,
                            "errors": []
                        },
                        "permissions": {
                            "canViewOrders": false,
                            "canViewOrderGuides": false,
                            "canViewCatalog": false,
                            "userRole": "user"
                        },
                        "role": "user",
                        "createdSessionDate": "2025-07-25T22:37:04.6700508Z",
                        "isImpersonationActive": false,
                        "hidePricing": false,
                        "showInvoices": false,
                        "websiteUrl": "https://www.chefswarehouse.com",
                        "orderOnlyFromOrderGuideRestriction": false
                    },
                    "site": {
                        "name": "Chefs'  Warehouse"
                    }
                }
            }
        }
    ],
    "lowerContentArea": [
        {
            "displayOption": "",
            "contentLink": {
                "id": 497675,
                "workId": 0,
                "guidValue": "6518538c-4246-48cd-8f49-7c5ecd053e99",
                "expanded": {
                    "contentLink": {
                        "id": 497675,
                        "workId": 0,
                        "guidValue": "6518538c-4246-48cd-8f49-7c5ecd053e99"
                    },
                    "name": "Nav_July_25_JIT - SID, NY, LA",
                    "language": {
                        "displayName": "English",
                        "name": "en"
                    },
                    "existingLanguages": [
                        {
                            "displayName": "English",
                            "name": "en"
                        }
                    ],
                    "masterLanguage": {
                        "displayName": "English",
                        "name": "en"
                    },
                    "contentType": [
                        "Block",
                        "HeroBannerBlock"
                    ],
                    "parentLink": {
                        "id": 497080,
                        "workId": 0,
                        "guidValue": "29aa6bbd-6ac7-4025-9253-5ca12794e6c9"
                    },
                    "changed": "2025-06-30T18:52:25Z",
                    "created": "2025-06-30T18:50:19Z",
                    "startPublish": "2025-06-30T18:52:25Z",
                    "saved": "2025-07-02T15:21:07Z",
                    "status": "Published",
                    "category": [],
                    "desktopImage": {
                        "id": 6538,
                        "workId": 0,
                        "guidValue": "11d66c69-0b4e-44ea-911d-20b754ad09e4",
                        "providerName": "bynder-assets-provider"
                    },
                    "mobileImage": null,
                    "heading": "",
                    "description": "<h2>From Block to Spec. Every Time.</h2>\n<p><strong>Explore cut-to-order proteins tailored for the flame.</strong></p>\n<p><a href=\"/cut-to-order/\" title=\"Explore\" class=\"btn btn-primary\" target=\"_blank\" rel=\"noopener\">Discover Cut-to-Order Proteins</a></p>",
                    "textAlignment": "left",
                    "viewModel": {
                        "desktopImageUrl": "https://media.chefswarehouse.com/transform/d15efbd0-fa1c-4309-b6db-869a3d24d5d5/Lifestyle_29?io=transform%3Afit%2Cwidth%3A1400",
                        "mobileImageUrl": "https://media.chefswarehouse.com/transform/d15efbd0-fa1c-4309-b6db-869a3d24d5d5/Lifestyle_29?io=transform%3Afit%2Cwidth%3A767",
                        "heading": "",
                        "description": "<h2>From Block to Spec. Every Time.</h2>\n<p><strong>Explore cut-to-order proteins tailored for the flame.</strong></p>\n<p><a href=\"/link/34c4936606334942abe0e41fbf0dbdfd.aspx\" title=\"Explore\" class=\"btn btn-primary\" target=\"_blank\" rel=\"noopener\">Discover Cut-to-Order Proteins</a></p>",
                        "textAlignment": "left",
                        "contentLink": "497675",
                        "contentType": [
                            "Block",
                            "HeroBannerBlock"
                        ]
                    },
                    "authRequired": false,
                    "currentUser": {
                        "sessionId": "9d0b0137-15fd-4b7b-bcbd-870f9853948a",
                        "algoliaIndexName": "Variants",
                        "userName": "",
                        "displayName": "",
                        "customerContactId": "6c98d90c-1d9a-41dd-b7c3-a293438b34a7",
                        "isAuthenticated": false,
                        "isPunchoutSession": false,
                        "isCSRUser": false,
                        "validStockingTypes": [
                            "J",
                            "P",
                            "U"
                        ],
                        "customerStatus": {
                            "canOrder": false,
                            "shouldCheckCreditBalance": false,
                            "creditBalance": 0,
                            "errors": []
                        },
                        "permissions": {
                            "canViewOrders": false,
                            "canViewOrderGuides": false,
                            "canViewCatalog": false,
                            "userRole": "user"
                        },
                        "role": "user",
                        "createdSessionDate": "2025-07-25T22:37:04.6700508Z",
                        "isImpersonationActive": false,
                        "hidePricing": false,
                        "showInvoices": false,
                        "websiteUrl": "https://www.chefswarehouse.com",
                        "orderOnlyFromOrderGuideRestriction": false
                    },
                    "site": {
                        "name": "Chefs'  Warehouse"
                    }
                }
            }
        }
    ],
    "seoInformation": {
        "title": "Wholesale Meat & Poultry for Restaurants",
        "description": "Chefs’ Warehouse is a premier supplier of wholesale meat for restaurants. Check out our supply of beef, poultry, pork, game, lamb and more."
    },
    "seoUri": "Meat-Poultry-en.aspx",
    "code": "1meatpoultry",
    "metaClassId": 6,
    "catalogId": 2,
    "viewModel": {
        "heroBanner": {
            "heading": "Meat & Poultry",
            "hideTitle": false,
            "image": {
                "desktopImageUrl": "",
                "mobileImageUrl": ""
            },
            "showBackgroundColor": false
        },
        "subCategories": [
            {
                "name": "Bacon & Sausage ",
                "imageUrl": "https://media.chefswarehouse.com/transform/9a991854-4272-4d61-b619-ac7b37bca1b7/Bacon_Sausage",
                "url": "/products/meat-and-poultry/bacon-and-sausage/"
            },
            {
                "name": "Cut to Order",
                "imageUrl": "https://media.chefswarehouse.com/transform/a07d1a8f-364a-420c-b4c1-e1af98ce7e89/Cowgirl_Cement-and-Knife",
                "url": "/products/meat-and-poultry/cut-to-order/"
            },
            {
                "name": "Foie Gras",
                "imageUrl": "/siteassets/foie-gras_330.png",
                "url": "/products/meat-and-poultry/foie-gras/"
            },
            {
                "name": "Lamb & Veal ",
                "imageUrl": "https://media.chefswarehouse.com/transform/c530be5f-6932-46a4-a18f-268a38fad529/Lamb_Veal",
                "url": "/products/meat-and-poultry/lamb-and-veal/"
            },
            {
                "name": "Meat & Game ",
                "imageUrl": "https://media.chefswarehouse.com/transform/0432a05e-08f1-480e-b34a-599d3bae096a/Meat_Game",
                "url": "/products/meat-and-poultry/meat-and-game/"
            },
            {
                "name": "Plant Based Proteins ",
                "imageUrl": "https://media.chefswarehouse.com/transform/a93d6028-fe56-427a-bcd0-728f8b8cc61e/Plant_Based_Protiens",
                "url": "/products/meat-and-poultry/plant-based-proteins/"
            },
            {
                "name": "Pork",
                "imageUrl": "/siteassets/pork_330.png",
                "url": "/products/meat-and-poultry/pork/"
            },
            {
                "name": "Poultry",
                "imageUrl": "/siteassets/categories-and-subcategories/poultry-copy.jpg",
                "url": "/products/meat-and-poultry/poultry/"
            },
            {
                "name": "Smoked & Cooked Meats ",
                "imageUrl": "https://media.chefswarehouse.com/transform/a2b456e2-35fe-4e21-8793-cdaf8ff526f5/smoked_cooked_meats",
                "url": "/products/meat-and-poultry/smoked-and-cooked-meats/"
            }
        ],
        "contentType": [
            "Node",
            "CategoryData"
        ]
    },
    "authRequired": false,
    "currentUser": {
        "sessionId": "9d0b0137-15fd-4b7b-bcbd-870f9853948a",
        "algoliaIndexName": "Variants",
        "userName": "",
        "displayName": "",
        "customerContactId": "6c98d90c-1d9a-41dd-b7c3-a293438b34a7",
        "isAuthenticated": false,
        "isPunchoutSession": false,
        "isCSRUser": false,
        "validStockingTypes": [
            "J",
            "P",
            "U"
        ],
        "customerStatus": {
            "canOrder": false,
            "shouldCheckCreditBalance": false,
            "creditBalance": 0,
            "errors": []
        },
        "permissions": {
            "canViewOrders": false,
            "canViewOrderGuides": false,
            "canViewCatalog": false,
            "userRole": "user"
        },
        "role": "user",
        "createdSessionDate": "2025-07-25T22:37:04.6700508Z",
        "isImpersonationActive": false,
        "hidePricing": false,
        "showInvoices": false,
        "websiteUrl": "https://www.chefswarehouse.com",
        "orderOnlyFromOrderGuideRestriction": false
    },
    "site": {
        "name": "Chefs'  Warehouse"
    }
}


# Product Detail

## Response

```json
{
    "contentLink": {
        "id": 201924,
        "workId": 0,
        "guidValue": "e0e12224-3fa1-4816-8085-d14b1d61574b",
        "providerName": "CatalogContent",
        "url": "/products/QZ106085/"
    },
    "name": "DECOR EXCLUSIVE DARK CHOC QZ106085",
    "language": {
        "link": "/products/QZ106085/",
        "displayName": "English",
        "name": "en"
    },
    "contentType": [
        "Product",
        "ProductData"
    ],
    "routeSegment": "decor-exclusive-dark-choc-qz106085",
    "url": "/products/QZ106085/",
    "displayName": "Dark Chocolate Decoration",
    "popularity": 72312,
    "seoInformation": {},
    "seoUri": "DECOR-EXCLUSIVE-DARK-CHOC-QZ106085-en.aspx",
    "code": "JDE_QZ106085",
    "secondItemNumber": "QZ106085",
    "brand": "DOBLA",
    "displayBrand": "Dobla",
    "countryOfOrigin": "Vietnam",
    "hasDualTolerance": false,
    "isAllowedBranchBackOrder": true,
    "lineType": "S",
    "manufacturerDisplayLocation": "1775 BRECKINRIDGE PARKWAY DULUTH GA 30096",
    "manufacturerDisplayName": "DOBLA BV CHOCOCENTER",
    "pricingUnitOfMeasureCode": "CS",
    "regionOfOrigin": " ",
    "shippingCondition": 3,
    "hasBottleRedemptionCode": true,
    "manufacturerItemNumber": "817987002114",
    "metaClassId": 7,
    "catalogId": 2,
    "shortItemNumber": "10242935",
    "viewModel": {
        "sku": "QZ106085",
        "description": "Beautiful and delicious dark chocolate decorations that can be used to add a touch of sophistication to any desserts or pastries.",
        "brand": "Dobla",
        "pricingUnitOfMeasure": "Case",
        "storageType": "Temperature Controlled",
        "size": "6x310 Piece BC",
        "isFrozen": false,
        "hasDualTolerance": false,
        "milkType": "Cow",
        "isRestricted": false,
        "isNsi": false,
        "variants": [
            {
                "code": "JDE_QZ106085-200001",
                "brokenCaseFlag": "003",
                "primaryUnitOfMeasureCode": "CS",
                "secondaryUnitOfMeasureCode": "PC",
                "metadata": {
                    "unitOfMeasure": "CS",
                    "chefItemFlag": false,
                    "bto": false,
                    "supermarket": false,
                    "stockingType": "P",
                    "lineType": "S",
                    "vendorId": "9484829",
                    "productionItem": false
                },
                "text": "Case",
                "weight": "6x310 Piece BC",
                "inStock": 1,
                "isReserve": false,
                "isRestricted": false,
                "isDropShipRestricted": false,
                "notifyFormPrefill": [
                    {
                        "field": "product.itemNumber",
                        "prefill": {
                            "value": "QZ106085"
                        }
                    },
                    {
                        "field": "product.uom",
                        "prefill": {
                            "value": "Case",
                            "options": [
                                {
                                    "text": "Case",
                                    "value": "Case"
                                }
                            ]
                        }
                    },
                    {
                        "field": "variant.code",
                        "prefill": {
                            "value": "JDE_QZ106085-200001"
                        }
                    },
                    {
                        "field": "product.uomcode",
                        "prefill": {
                            "value": "CS"
                        }
                    },
                    {
                        "field": "product.packSize",
                        "prefill": {
                            "value": "6x310 Piece BC"
                        }
                    }
                ],
                "stockingType": "P",
                "checkAvailabilityFlag": true,
                "isSecondaryBusinessUnit": false,
                "businessUnitModel": {
                    "id": "200001",
                    "type": 0
                },
                "sellByMultiple": 1,
                "cutOffMessage": "",
                "tag1": {},
                "tag2": {},
                "specialOrderFlag": false,
                "isAvailabilityChecked": false,
                "isExpired": false,
                "displayOnlyCatchWeight": false,
                "minQuantity": 1,
                "maxQuantity": 10000,
                "itemRestriction": "None",
                "isSubsRestricted": false
            },
            {
                "code": "JDE_QZ106085-200001",
                "brokenCaseFlag": "003",
                "primaryUnitOfMeasureCode": "CS",
                "secondaryUnitOfMeasureCode": "PC",
                "metadata": {
                    "unitOfMeasure": "PC",
                    "chefItemFlag": false,
                    "bto": false,
                    "supermarket": false,
                    "stockingType": "P",
                    "lineType": "S",
                    "vendorId": "9484829",
                    "productionItem": false
                },
                "text": "Piece",
                "weight": "6x310 Piece BC",
                "inStock": 6,
                "isReserve": false,
                "isRestricted": false,
                "isDropShipRestricted": false,
                "notifyFormPrefill": [
                    {
                        "field": "product.itemNumber",
                        "prefill": {
                            "value": "QZ106085"
                        }
                    },
                    {
                        "field": "product.uom",
                        "prefill": {
                            "value": "Piece",
                            "options": [
                                {
                                    "text": "Piece",
                                    "value": "Piece"
                                }
                            ]
                        }
                    },
                    {
                        "field": "variant.code",
                        "prefill": {
                            "value": "JDE_QZ106085-200001"
                        }
                    },
                    {
                        "field": "product.uomcode",
                        "prefill": {
                            "value": "CS"
                        }
                    },
                    {
                        "field": "product.packSize",
                        "prefill": {
                            "value": "6x310 Piece BC"
                        }
                    }
                ],
                "stockingType": "P",
                "checkAvailabilityFlag": true,
                "isSecondaryBusinessUnit": false,
                "businessUnitModel": {
                    "id": "200001",
                    "type": 0
                },
                "sellByMultiple": 1,
                "cutOffMessage": "",
                "tag1": {},
                "tag2": {},
                "specialOrderFlag": false,
                "isAvailabilityChecked": false,
                "isExpired": false,
                "displayOnlyCatchWeight": false,
                "minQuantity": 1,
                "maxQuantity": 10000,
                "itemRestriction": "None",
                "isSubsRestricted": false
            }
        ],
        "forRedirecting": false,
        "unableToBeAddedOrShownInOrderGuide": false,
        "quantityWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. {{availableQuantity}} {{variant}} can be added to cart.",
        "quantityInCartWarningMessage": "Requested quantity of {{quantity}} {{variant}} not available. Up to {{availableQuantity}} additional {{variant}} can be added to cart.",
        "quantitySellByMultipleWarningMessage": "Product must be added in multiples of {{sellByMultiple}}",
        "dietaryContains": [
            {
                "name": "Dairy",
                "text": "Dairy",
                "abbreviation": "Dairy"
            },
            {
                "name": "CowMilk",
                "text": "Cow Milk",
                "abbreviation": "CM"
            }
        ],
        "dietaryMayContain": [],
        "dietaryTags": [
            {
                "name": "Kosher",
                "text": "Kosher",
                "abbreviation": "K"
            }
        ],
        "documents": [],
        "category": {
            "href": "/products/baking-and-pastry/chocolate/chocolate-decor/",
            "text": "Chocolate Décor",
            "hasChildren": false,
            "numberOfSubSubcategoryColumns": 0,
            "sortOrder": 0
        },
        "subcategory": "Chocolate",
        "subsubcategory": "Chocolate Décor",
        "notifyFormPrefill": [
            {
                "field": "product.itemNumber",
                "prefill": {
                    "value": "QZ106085"
                }
            },
            {
                "field": "product.uom",
                "prefill": {
                    "value": "Case",
                    "options": [
                        {
                            "text": "Case",
                            "value": "Case"
                        },
                        {
                            "text": "Piece",
                            "value": "Piece"
                        }
                    ]
                }
            },
            {
                "field": "variant.code",
                "prefill": {
                    "value": "JDE_QZ106085-200001"
                }
            },
            {
                "field": "product.uomcode",
                "prefill": {
                    "value": "CS"
                }
            },
            {
                "field": "product.packSize",
                "prefill": {
                    "value": "6x310 Piece BC"
                }
            }
        ],
        "searchQuery": "/search/?q=Dobla",
        "productInterestedHours": 24,
        "productInterestedDays": 30,
        "pageType": "PDP",
        "productViewedDelayedTime": 7,
        "isObsolete": false,
        "hasReplacement": false,
        "hasSubstitutions": false,
        "obsoleteProductMessage": "This Item Is No Longer Available For Purchase",
        "countryRegionOrigin": "Origin: Vietnam",
        "featureList": [],
        "featureListTitle": "Key features",
        "url": "/products/QZ106085/",
        "reportProductReasons": [
            "Missing Image",
            "Wrong Image",
            "Bad Quality Image",
            "Wrong/Missing Product Description",
            "Wrong/Missing Pack Size",
            "Wrong Brand",
            "Wrong Product Title",
            "Other (do not report pricing issues, prices come from JDE)"
        ],
        "learnMoreOptions": [
            "Brand",
            "Quality",
            "Ingredients, Allergens & Nutrition",
            "Applications",
            "Origin & Production",
            "Pack Size",
            "Similar & Related Items",
            "Price"
        ],
        "reportProductSuccessMessage": "Issue successfully reported. Thanks for your feedback! Changes can take up to 14 days.",
        "reportProductFailMessage": "Failed to submit product data issue item. Please try again.",
        "reportProductSubheading": "Please upload any supporting documentation or assets if needed. All applicable requests can be added to the same submission. Changes can take up to 14 days.",
        "showDetailedReportProductIssueFields": false,
        "userIsDomainApproved": false,
        "substitutionModalReplacementTitle": "This item is no longer available for purchase. We think you'll like this alternative.",
        "similarProductSliders": [],
        "name": "Dark Chocolate Decoration",
        "code": "JDE_QZ106085",
        "assets": [
            {
                "featuredSrc": "/siteassets/pim-images/chocolate-décor/qz106085_0.jpg",
                "thumbnailSrc": "/siteassets/pim-images/chocolate-décor/qz106085_0.jpg?w=56&h=56&mode=crop",
                "contentType": [
                    "Media",
                    "Image",
                    "ImageFile"
                ]
            },
            {
                "featuredSrc": "/siteassets/pim-images/chocolate-décor/qz106085_1.jpg",
                "thumbnailSrc": "/siteassets/pim-images/chocolate-décor/qz106085_1.jpg?w=56&h=56&mode=crop",
                "contentType": [
                    "Media",
                    "Image",
                    "ImageFile"
                ]
            },
            {
                "featuredSrc": "/siteassets/pim-images/chocolate-décor/qz106085_2.jpg",
                "thumbnailSrc": "/siteassets/pim-images/chocolate-décor/qz106085_2.jpg?w=56&h=56&mode=crop",
                "contentType": [
                    "Media",
                    "Image",
                    "ImageFile"
                ]
            }
        ],
        "contentType": [
            "Product",
            "ProductData"
        ]
    },
    "authRequired": false,
    "currentUser": {
        "sessionId": "9d0b0137-15fd-4b7b-bcbd-870f9853948a",
        "algoliaIndexName": "Variants",
        "userName": "",
        "displayName": "",
        "customerContactId": "6c98d90c-1d9a-41dd-b7c3-a293438b34a7",
        "isAuthenticated": false,
        "isPunchoutSession": false,
        "isCSRUser": false,
        "validStockingTypes": [
            "J",
            "P",
            "U"
        ],
        "customerStatus": {
            "canOrder": false,
            "shouldCheckCreditBalance": false,
            "creditBalance": 0,
            "errors": []
        },
        "permissions": {
            "canViewOrders": false,
            "canViewOrderGuides": false,
            "canViewCatalog": false,
            "userRole": "user"
        },
        "role": "user",
        "createdSessionDate": "2025-07-25T22:37:04.6700508Z",
        "isImpersonationActive": false,
        "hidePricing": false,
        "showInvoices": false,
        "websiteUrl": "https://www.chefswarehouse.com",
        "orderOnlyFromOrderGuideRestriction": false
    },
    "site": {
        "name": "Chefs'  Warehouse"
    }
}
```