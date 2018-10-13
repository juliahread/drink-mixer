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
* DELETE delete
  * /api/ingredient/delete?id={String}

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
   title: {String}
   ingredients: {
       {ingredient.uuid}: {ingredient.amount}
       ...
       ...
       ...
       ...
       ...
   }
}
```
* PUT updateRecipe
  * Request JSON
```
{
   id: {uuid as String}
   title: {String}
   ingredients: {
       {ingredient.uuid}: {ingredient.amount}
       ...
       ...
       ...
       ...
       ...
   }
}
```
* GET getRecipe
  * /api/recipe/get?id={String}
  * Response JSON
```
    an ingredient
```
* GET getAll
  * /api/recipe/all
  * Response JSON
```
[
  ingredients...
]
```
* DELETE delete
  * /api/recipe/delete?id={String}

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
