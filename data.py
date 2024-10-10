
product_to_category = {
    'Apple': 'Fruits',
    'Orange': 'Fruits',
    'Banana': 'Fruits',
    'Mango': 'Fruits'
    
}


owners = [
    {
        "id": 101,
        "preference": {
            "products": [
                {"product_name": "Apple", "preferred_cost": {"min": 500, "max": 1000}},
                {"product_name": "Orange", "preferred_cost": {"min": 500, "max": 1000}}
            ],
            "marketing": [
                {"marketing_type": "instagram", "preferred_cost": {"min": 1000, "max": 3000}},
                {"marketing_type": "youtube", "preferred_cost": {"min": 1000, "max": 3000}}
            ]
        }
    },
    {
        "id": 102,
        "preference": {
            "categories": [
                {"category_name": "Fruits", "preferred_cost": {"min": 500, "max": 1000}}
            ],
            "marketing": [
                {"marketing_type": "instagram", "preferred_cost": {"min": 1000, "max": 3000}}
            ]
        }
    }
]

influencers = [
    {
        "id": 201,
        "preference": {
            "products": [
                {"product_name": "Orange", "preferred_cost": {"min": 500, "max": 1000}}
            ],
            "marketing": [
                {"marketing_type": "instagram", "preferred_cost": {"min": 1000, "max": 3000}},
                {"marketing_type": "youtube", "preferred_cost": {"min": 1000, "max": 3000}}
            ]
        }
    },
    {
        "id": 202,
        "preference": {
            "categories": [
                {"category_name": "Fruits", "preferred_cost": {"min": 500, "max": 1000}}
            ],
            "marketing": [
                {"marketing_type": "instagram", "preferred_cost": {"min": 1000, "max": 3000}}
            ]
        }
    },
    {
        "id": 203,
        "preference": {
            "products": [
                {"product_name": "Banana", "preferred_cost": {"min": 500, "max": 1000}},
                {"product_name": "Orange", "preferred_cost": {"min": 500, "max": 1000}}
            ]
        }
    }
]
