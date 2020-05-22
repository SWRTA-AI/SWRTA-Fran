# SW - RTA

## Predict picks

<details>

### Request

POST `http://localhost:5000/api/predictor/pick/`

```JSON
{
    "type": "id",
    "input": [22213, 15713, 19114, 16615, 21112]
}
```

```JSON
{
    "type": "name",
    "input": ["Vanessa", "Giana", "Seara", "Fran", "Hathor", "Verdehile", "Barbara"]
}
```

### Response 200

```JSON
{
    "result": [
        {
            "archetype": "Support",
            "base_stars": 5,
            "com2us_id": 21413,
            "element": "Wind",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0043_2_2.png",
            "name": "Triana",
            "pk": 1030,
            "score": 0.23579524457454681,
            "url": "https://swarfarm.com/api/bestiary/1030?format=json"
        },
        {
            "archetype": "Support",
            "base_stars": 6,
            "com2us_id": 17014,
            "element": "Light",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0019_3_2.png",
            "name": "Artamiel",
            "pk": 695,
            "score": 0.07925765216350555,
            "url": "https://swarfarm.com/api/bestiary/695?format=json"
        },
        {
            "archetype": "Support",
            "base_stars": 6,
            "com2us_id": 20513,
            "element": "Wind",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0039_2_2.png",
            "name": "Hathor",
            "pk": 942,
            "score": 0.06436343491077423,
            "url": "https://swarfarm.com/api/bestiary/942?format=json"
        },
        {
            "archetype": "Attack",
            "base_stars": 6,
            "com2us_id": 23511,
            "element": "Water",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0054_0_0.png",
            "name": "Barbara",
            "natural_stars": 5,
            "pk": 1339,
            "score": 0.06321056932210922,
            "url": "https://swarfarm.com/api/bestiary/1339?format=json"
        },
        {
            "archetype": "Support",
            "atbBoost": 30,
            "base_stars": 6,
            "com2us_id": 17012,
            "element": "Fire",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0019_1_2.png",
            "name": "Velajuel",
            "pk": 268,
            "score": 0.05273795127868652,
            "url": "https://swarfarm.com/api/bestiary/268?format=json"
        }
    ]
}
```

</details>

## Predict ban 01 & 02

<details>

### Request

POST `http://localhost:5000/api/predictor/pick/`

```JSON
{
    "type":"id",
    "team": [22213, 15713, 19114, 16615, 21112],
    "opponent": [22212, 15712, 16614, 16611, 21113]
}
```

```JSON
{
    "type": "name",
    "opponent": ["Vanessa", "Hathor", "Ragdoll", "Artamiel", "Fran"],
    "team": ["Ganymede", "Daphnis", "Masha", "Barbara", "Verdehile"]
}
```

### Response 200

```JSON
{
    "result": [
        {
            "archetype": "Support",
            "base_stars": 5,
            "com2us_id": 21413,
            "element": "Wind",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0043_2_2.png",
            "name": "Triana",
            "pk": 1030,
            "score": 0.23579524457454681,
            "url": "https://swarfarm.com/api/bestiary/1030?format=json"
        },
        {
            "archetype": "Support",
            "base_stars": 6,
            "com2us_id": 17014,
            "element": "Light",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0019_3_2.png",
            "name": "Artamiel",
            "pk": 695,
            "score": 0.07925765216350555,
            "url": "https://swarfarm.com/api/bestiary/695?format=json"
        },
        {
            "archetype": "Support",
            "base_stars": 6,
            "com2us_id": 20513,
            "element": "Wind",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0039_2_2.png",
            "name": "Hathor",
            "pk": 942,
            "score": 0.06436343491077423,
            "url": "https://swarfarm.com/api/bestiary/942?format=json"
        },
        {
            "archetype": "Attack",
            "base_stars": 6,
            "com2us_id": 23511,
            "element": "Water",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0054_0_0.png",
            "name": "Barbara",
            "natural_stars": 5,
            "pk": 1339,
            "score": 0.06321056932210922,
            "url": "https://swarfarm.com/api/bestiary/1339?format=json"
        },
        {
            "archetype": "Support",
            "atbBoost": 30,
            "base_stars": 6,
            "com2us_id": 17012,
            "element": "Fire",
            "fusion_food": false,
            "image_filename": "https://swarfarm.com/static/herders/images/monsters/unit_icon_0019_1_2.png",
            "name": "Velajuel",
            "pk": 268,
            "score": 0.05273795127868652,
            "url": "https://swarfarm.com/api/bestiary/268?format=json"
        }
    ]
}
```

</details>
