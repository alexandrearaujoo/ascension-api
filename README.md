# ascension-api

## Character

# fazer mission

POST - api/characters/missions/mission_id/

# RESPONSE

```json
{
  "username": "teste",
  "missions": [
    {
      "name": "shushushush",
      "description": "hsuhsuhsuhus",
      "level": 5,
      "gold": 500,
      "xp": 150
    }
  ]
}
```

# adicionar item no inventario

POST - api/characters/items/item_id/

# RESPONSE

```json
{
  "username": "teste",
  "inventory": [
    {
      "name": "shushushush",
      "type": "hsuhsuhsuhus",
      "artizan_id": "uuid"
    }
  ]
}
```

# deletar item do inventario

DELETE - api/characters/items/item_id/

## Artisan

POST - api/artisan/artisan_id/items/


# BODY 

```json
    {
        "name": "",
        "type": "",
        "price":"",
        "level_requires": "",
    }

```

# RESPONSE

```json
{
    "id": "",
    "name": "",
    "type": "",
    "price":"",
    "level_requires": "",
    "artisan":"artisan_id",
    "owner": null
}
```
