# Drink API

## Ingredients
### Interface
* String name
  * The name of the Ingredients
* Integer sugarContent
  * Volume per standard sugar drink
* Integer type
  * Type of ingredient
  * Syrup (0) or Mixer (1)
* String uuid
  * Unique global identifier for ingredient

### API Endpoints
* POST createIngredient
  * /api/ingredient/new
  * Request JSON
```
{
    name: {String},
    sugarContent: {Integer},
    type: {Integer}
}
```
* PUT updateIngredient
  * /api/ingredient/new
  * Request JSON
```
{
    uuid: {String},
    name: {String},
    type: {Integer},
    sugarContent: {Integer}
}
```
* GET getAll
  * /api/ingredient/all
* GET get
  * /api/ingredient/get?id={String}

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
