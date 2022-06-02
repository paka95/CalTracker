# CalTracker

app that helps you track your calories intake

If you would like to keep an eye on what you eat and how many specific nutrients you take, this simple app is for you. In it, you can report your daily calories intake and keep track of everything you eat.

## Technologies used in this project:
- Backend - Python 3.10/Flask 2.0.3, PostgreSQL
- Frontend - HTML5/CSS, a little bit of JavaScript

## Setup
In order to run this project, simply clone the repository, setup the database (in file /website/__ init __.py) then in console run:
```
$ pip install -r requirements.txt
$ python app.py
```
After installation you will be able to use it at localhost:5000 or 127.0.0.1:5000

## Features
* Registering new users and logging in/out users
* Adding new products to the database
* Adding meals that include added products
* Specifying weight, proteins, carbohydrates, fats and type of each meal
* Updating and deleting each meal
* Grouping and displaying meals based on meal type (breakfast, dinner, snack etc.)

## Project overview

Register view, logging in/out (with error handling):

https://user-images.githubusercontent.com/94203043/171611791-023d8616-8c95-46ba-990b-255cd09ee5e6.mp4


Dashboard preview:

https://user-images.githubusercontent.com/94203043/171612411-09c47773-d375-4077-acac-d4aca57441ad.mp4


Adding new product:

https://user-images.githubusercontent.com/94203043/171613189-9e798226-82b6-4686-8c3e-2f58f97861c1.mp4

Adding new meal:

https://user-images.githubusercontent.com/94203043/171614833-90542e13-6461-48a0-83a8-b4e439ea3d65.mp4


Updating, removing meal:

https://user-images.githubusercontent.com/94203043/171615602-acf9b9ce-f807-4985-9a1e-ac7e04952d80.mp4

## Exemplary code snippets - backwards querying database:
![product table](https://user-images.githubusercontent.com/94203043/171624258-7c558dda-547d-4043-a2a9-959a26736171.png)
![meal table](https://user-images.githubusercontent.com/94203043/171624284-5a41d2f6-91d6-42ab-85c4-212d664dd830.png)
![snip meal](https://user-images.githubusercontent.com/94203043/171624295-a92c3c25-50e9-49af-9406-7020cb2bfe05.png)
![snip 2](https://user-images.githubusercontent.com/94203043/171624302-d7dea241-2261-4c07-a930-65bd0d6ee5e7.png)



## Plan for development
In the near future I plan on adding:
* a feature to track average calories intake throughout a month, 
* a monthly summary of consumed nutrients,
* a shopping list of consumed products,
* a feature to add repeating meals as a list
