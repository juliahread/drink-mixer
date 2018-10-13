# Drink API

## Ingredients
### Interface
* String name
  * The name of the Ingredients
* double sugarContent
  * Sugar content per volume
* String type
  * Type of ingredient
  * Syrup or Mixer
* String uuid
  * Unique global identifier for ingredient

### API Endpoints
* POST createIngredient
  * Request JSON
```
{
    name: {String},
    type: {String},
    sugarContent: {double},
    type: {String}
}
```
* PUT updateIngredient
  * Request JSON
```
{
    uuid: {String},
    name: {String},
    type: {String},
    sugarContent: {double},
    type: {String}
}
```
* GET getAll
* GET get
  * Query params
  * {url}?uuid={String}

## Recipes
### Interface
* HashMap Ingredients
  * key: storing ids of Ingredients
  * value: dispense amount of Ingredients

### API Endpoints
* POST createRecipe
  * Request JSON
```
{
   {ingredient.uuid}: {ingredient.amount}
   ...
   ...
   ...
   ...
   ...
}
```
* PUT updateRecipe
  * Request JSON
```
{
   {ingredient.uuid}: {ingredient.amount}
   ...
   ...
   ...
   ...
   ...
}
```
* GET getRecipe
  * Response JSON
```
    an ingredient
```
* GET getAll
  * Response JSON
```
[
  ingredients...
]
```

## Display
### Interface
* uuid[6] Stuff
  * contains the ingredient ids
  * and the amount left

### API Endpoints
PUT methods for each slot

## General API Endpoints
API endpoints to dispense recipes.
API endpoints to add drinks to a queue.

Sugar rush warning!
