# Categories API

## Response

### Single Category
#### Method

```json
{
                "category": {
                    "id": "154067862",
                    "baseName": "produce",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Produce",
                    "sortIndex": "0",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 953,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067863",
                            "name": "Fresh Produce",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 951,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069146",
                            "name": "Lemon Wraps",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            }
```
 
    ### Whole Response    
```json
{
    "data": {
        "catalogCategoryOptions": [
            {
                "category": {
                    "id": "154067862",
                    "baseName": "produce",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Produce",
                    "sortIndex": "0",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 953,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067863",
                            "name": "Fresh Produce",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 951,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069146",
                            "name": "Lemon Wraps",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067892",
                    "baseName": "grocery",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Grocery",
                    "sortIndex": "1",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 1360,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "385186681",
                            "name": "Fruit",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 139,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067907",
                            "name": "Pasta",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 90,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067939",
                            "name": "Syrups",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 36,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067893",
                            "name": "Chocolate & Cocoa",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 104,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067962",
                            "name": "Mayonnaise",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 20,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067940",
                            "name": "Sauces",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 122,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067903",
                            "name": "Snacks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 116,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067896",
                            "name": "Ethnic",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 119,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385186682",
                            "name": "Vegetables",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 198,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067966",
                            "name": "Tortilla",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 24,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067970",
                            "name": "Portion Packs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 71,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067961",
                            "name": "Salad Dressings",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 35,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067897",
                            "name": "Condiments",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 107,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067933",
                            "name": "Baking Mixes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 25,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067904",
                            "name": "Jams, Jelly, And Preserv",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 19,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385186684",
                            "name": "Olives",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 32,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067946",
                            "name": "Cereals",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 38,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067968",
                            "name": "Tomatoes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 48,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067972",
                            "name": "Nut Butters",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 11,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067941",
                            "name": "Stuffing",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067956",
                            "name": "Capers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067894",
                    "baseName": "dry goods",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Dry Goods",
                    "sortIndex": "2",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 702,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067895",
                            "name": "Baking Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 340,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067905",
                            "name": "Nuts",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 39,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067900",
                            "name": "Batter And Breading",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 23,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067906",
                            "name": "Shortening And Oils",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 86,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067901",
                            "name": "Grains And Legumes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 116,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067908",
                            "name": "Vinegar",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 59,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385186683",
                            "name": "Bases",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 37,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067947",
                            "name": "Polenta",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067898",
                    "baseName": "spices",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Spices",
                    "sortIndex": "3",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 236,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067899",
                            "name": "Spices",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 236,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067909",
                    "baseName": "prepared foods",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Prepared Foods",
                    "sortIndex": "4",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 275,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067930",
                            "name": "Appetizers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 66,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068073",
                            "name": "Soups",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 37,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067929",
                            "name": "Entrees",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 27,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219285",
                            "name": "Protein - Deli Meats",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 42,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219292",
                            "name": "Vegetarian",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 36,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219328",
                            "name": "Protein - Meatballs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 8,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067934",
                            "name": "Pizza",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 33,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219324",
                            "name": "Protein - Hot Dogs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 14,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068032",
                            "name": "Salads And Sides",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 12,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067911",
                    "baseName": "seafood",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Seafood",
                    "sortIndex": "5",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 212,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067912",
                            "name": "Protein - Seafood",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 212,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067913",
                    "baseName": "meat + game",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Meat + Game",
                    "sortIndex": "6",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 488,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067915",
                            "name": "Protein - Beef",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 289,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067916",
                            "name": "Protein - Pork",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 85,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067918",
                            "name": "Protein - Sausage",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 67,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067924",
                            "name": "Protein - Lamb",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 30,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067925",
                            "name": "Protein - Veal",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067914",
                            "name": "Protein - Exotic Meats",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 10,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068028",
                            "name": "Protein - Philly Sandwic",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 5,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068027",
                            "name": "Protein - Gyro",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067919",
                    "baseName": "poultry",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Poultry",
                    "sortIndex": "7",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 223,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067922",
                            "name": "Protein - Turkey",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 29,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067923",
                            "name": "Protein - Duck",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067920",
                            "name": "Protein - Chicken",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 182,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067921",
                            "name": "Protein - Game Hens",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 3,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067926",
                    "baseName": "bakery",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Bakery",
                    "sortIndex": "8",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 258,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067927",
                            "name": "Baked Goods",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 145,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067928",
                            "name": "Bread",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 113,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067937",
                    "baseName": "beverage",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Beverage",
                    "sortIndex": "9",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 396,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067955",
                            "name": "Beverages",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 290,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067953",
                            "name": "Coffee, Tea, And Cocoa",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 75,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067938",
                            "name": "Bar Supplies And Mixes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 31,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067942",
                    "baseName": "dairy + eggs",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Dairy + Eggs",
                    "sortIndex": "10",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 343,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067948",
                            "name": "Cheese",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 240,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067943",
                            "name": "Dairy",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 78,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067958",
                            "name": "Creamer",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067944",
                            "name": "Eggs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 16,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067951",
                    "baseName": "miscellaneous",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Miscellaneous",
                    "sortIndex": "11",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 2,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067952",
                            "name": "Non Commission",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068072",
                            "name": "Trackmax Test Pbh It",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067959",
                    "baseName": "frozen desserts",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Frozen Desserts",
                    "sortIndex": "12",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 85,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067969",
                            "name": "Toppings",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 15,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067960",
                            "name": "Desserts",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 70,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154068232",
                    "baseName": "equipment + furniture",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Equipment + Furniture",
                    "sortIndex": "13",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 1290,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "385187583",
                            "name": "Baskets",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 6,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187548",
                            "name": "Glassware",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 111,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187245",
                            "name": "Dining Room Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 79,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069020",
                            "name": "Pizza Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 12,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068261",
                            "name": "Pots And Pans",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 53,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068246",
                            "name": "Kitchen Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 248,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219489",
                            "name": "Brushes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187472",
                            "name": "Flatware",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 93,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187246",
                            "name": "China",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 30,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068233",
                            "name": "Equipment",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 42,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187763",
                            "name": "Vacuum Bags",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 11,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068254",
                            "name": "Storage",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 44,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069159",
                            "name": "Squeeze Bottles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 12,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069157",
                            "name": "Carts",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068251",
                            "name": "Bar Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 31,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068245",
                            "name": "Parts",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 16,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187907",
                            "name": "Pastry Cloth",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069158",
                            "name": "Warewashing",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 24,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069164",
                            "name": "Racks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385188009",
                            "name": "Bell",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069199",
                            "name": "Shakers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187695",
                            "name": "Textiles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 5,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068635",
                            "name": "Light Bulbs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069163",
                            "name": "Servers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069017",
                            "name": "Hoses",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 3,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069160",
                            "name": "Mandolines",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 3,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069165",
                            "name": "Valves",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "411509560",
                            "name": "Baking Supplies",
                            "sortIndex": 2,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 340,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "411516576",
                            "name": "Cutlery",
                            "sortIndex": 3,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 69,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "411516527",
                            "name": "Trays",
                            "sortIndex": 3,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 31,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154068234",
                    "baseName": "janitorial",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Janitorial",
                    "sortIndex": "14",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 267,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154068239",
                            "name": "Restroom Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 46,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068235",
                            "name": "Chemical-dispensed",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 53,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068236",
                            "name": "Chemical-green Dispense",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068237",
                            "name": "Chemical-nondispensed",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 80,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187873",
                            "name": "Waste Receptacles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187876",
                            "name": "Signs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069114",
                            "name": "Chemical-green Non-disp",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 6,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069130",
                            "name": "Brooms",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187742",
                            "name": "Can Liners",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 31,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069137",
                            "name": "Buckets",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069131",
                            "name": "Mops And Handles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069139",
                            "name": "Squeegees",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069134",
                            "name": "Dust Mops And Handles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187905",
                            "name": "Spray Bottle",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069133",
                            "name": "Dust Pans",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 3,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385188391",
                            "name": "Vacuums",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069138",
                            "name": "Plunger",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219331",
                            "name": "Distilled Water",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154068262",
                    "baseName": "operational supplies",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Operational Supplies",
                    "sortIndex": "15",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 765,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "385187909",
                            "name": "Wipes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 5,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187293",
                            "name": "Containers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 51,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187260",
                            "name": "Environmentally Friendly",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 167,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187290",
                            "name": "Cups",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 42,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187469",
                            "name": "Food Safety",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 41,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187892",
                            "name": "Dispensers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 23,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187289",
                            "name": "Boxes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 37,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187292",
                            "name": "Food Wraps",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 41,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187388",
                            "name": "Lids",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 34,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187291",
                            "name": "Bags",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 49,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187390",
                            "name": "Cutlery",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 69,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187908",
                            "name": "Filters",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187686",
                            "name": "Food Pans",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187547",
                            "name": "Napkins",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 35,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219491",
                            "name": "Scouring Pads",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 12,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187586",
                            "name": "Guest Checks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 10,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187904",
                            "name": "Doilies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187386",
                            "name": "Trays",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 31,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187389",
                            "name": "Straws",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 12,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187903",
                            "name": "Skewers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187910",
                            "name": "Twine",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187471",
                            "name": "Platters",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187911",
                            "name": "Tablecover",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187893",
                            "name": "Picks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 11,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187470",
                            "name": "Java Jackets",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187589",
                            "name": "Stir Sticks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069016",
                            "name": "Apparel",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187543",
                            "name": "Fuel",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 21,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187598",
                            "name": "Bowls",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187549",
                            "name": "Beverage Carriers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187392",
                            "name": "Pan Liners",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187585",
                            "name": "Corrugated Circles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187906",
                            "name": "Placemats",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385188349",
                            "name": "Grill Scrapers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187387",
                            "name": "Plates",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187874",
                            "name": "Grill Pads",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187950",
                            "name": "Masking Tape",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068263",
                            "name": "Back Office Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187550",
                            "name": "Towelettes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            }
        ]
    }
}
```
# Search

## Example URL
https://app.cutanddry.com/catalog/BiRite%20Foodservice%20Distributors/247696227?verifiedVendorId=120984264&categoryId=154067862&categoryName=Produce&subcategoryId=154067863&subcategoryName=Fresh+Produce&page=1
