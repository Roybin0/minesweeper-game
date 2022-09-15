# Minesweeper Game 

## Introduction

Minesweeper is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Players must choose locations to reveal on a gameboard while avoiding mines. 

![](https://lh3.googleusercontent.com/pw/AL9nZEXpFLU0Dw5LZAJUmmhPIK9LhjxXeypnRjaMs8DnhsmL3lXCTkEe2gVv0uB9IsvfSHCaktPCSSG77qIXs23SuvD5eViA5LqFPOBSKXSJ_YEN0nlpofP_FmdpuTrXlICjtZQIgOdYGnCRVxATkFuGVzJF=w1882-h1098-no?authuser=0) 

The link to the live game can be found here: [Minesweeper Game](https://roybin-minesweeper-game.herokuapp.com)


## Table of Contents

* [How to Play](#how-to-play)
* [Features](#features)
    * [Player Input](#player-input)
    * [Validation](#validation)
    * [Play Again](#play-again)
* [Testing](#testing)
* [Errors](#errors)
* [Future Features](#future-features)
* [Validator Testing](#validator-testing)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Other Code](#other-code)
    * [Acknowledgements](#acknowledgements)

## How to Play 

Minesweeper is a logic game where players must reveal spaces on a game board without landing on a mine. The number of mines on the board depends on the difficulty level. 

* E = Easy = 8 mines
* M = Medium = 20 mines
* H = Hard = 30 mines 

If a revealed space contains a number, this denotes how many mines are in the spaces immediately surrounding that space. 

If a revealed space contains 'X', the player has landed on a mine and the game is over. 

Read more about the origins of Minesweeper on Wikipedia [here](https://en.wikipedia.org/wiki/Minesweeper_(video_game)). 


## Features 

### Flow Chart

In order to build the game, a flow chart of required steps was created to highlight different features needed: 

![](https://lh3.googleusercontent.com/pw/AL9nZEWdCagh7eby3L992cMhus3znHzBVjOyLuKvTtSe9Ekn3Jh7dcjMUd_g-cqbJAZ6_hp3VI1Vz9rIaqdiX5rbMkaGGarPAACdUU2CQkoSBc0MAmDdIvHQUMwSjHAOVNOg5pB2mCtNtsdb3FD7l5-EoLDw=w1470-h1164-no?authuser=0)

### Player Input

This game requires multiple player inputs: 
* Difficulty level
![](https://lh3.googleusercontent.com/pw/AL9nZEX5UtmYBxlFKayICGxtqrM4hDqeUQmb4uJX3veKTtSuhxq7jNpmsi2KHTTtnPuProBQ_BPBzYzoG8ZF_JYLUMBNkERIaVbftlEzlz6dQIXpA-UcJp_euBYYSkump2rrHSAoDRn8uHzIm1apa1Yt__Jp=w1014-h408-no?authuser=0)
* Row and column to dig at
![](https://lh3.googleusercontent.com/pw/AL9nZEUSEPtPOLB4_i68BEGlCCs3h-zhjmOnCFO-abovPt5gS9SHjQjudcXcBDYMbkd2ncpblnKGdU5EgCoE_VBXTymZoCZZzIe_l8h2rbfriDnmMi2d-RIiNYm-DBNO-3z-j3UzYHGCca6sItThxePL1GRs=w1148-h820-no?authuser=0)
* Continue game Y or N 
![](https://lh3.googleusercontent.com/pw/AL9nZEWoUSe7MBj6dcXriwmneAxbzKQTx9KkI8FOwV15uXGiQyJg48FbXkjefijrKcOPz15v95fiQSDY-XbySvbrG-2Ytc-8xElOUZpX2NnwkNFBBDeIVldW_6sxbU3Axaai1Wry_QE3Iu54tapzNIBrNADY=w672-h302-no?authuser=0)

### Validation

For each input requested from the user, the data is validated to ensure that it is a correct input type and is within range of accepted answers. 

For example, when entering a row or column, the player will see an error if they try to enter a letter or word, or if the number they have entered is higher or lower than the board size: 

![](https://lh3.googleusercontent.com/pw/AL9nZEV2uTR2pUlTn5Ot8u51be4IZFJDe64oXDi_18iLOvj3KNzxKfgZjAm8NOd7PrcDlyHVaaQC5OtO4FFoHydplZWXHHDXl_KqwTdRa0SpymkiDPTjCu6ZxGDzmbXz3b6AfpgMGXWi9QaXGHKJIsZiIJfu=w1114-h142-no?authuser=0)
![](https://lh3.googleusercontent.com/pw/AL9nZEXoXVAqBLL16Ozcw-BTe7uWhHp9F7cPzuC1nk3b-KeOmj3tS_yKxXpDpoT8xliWoG97ZZJYTnHW5dipKcRm0DH5oJGGeSZqAv6XOxil-GbCpy2rG1Tu2C7dPavUFEPN23Q-v87dOYprzHILHKLyVaw9=w1204-h144-no?authuser=0)


### Play Again

The Minesweeper Game ends if: 

* The player reveals a mine OR
* The player reveals all spaces that are NOT mines 

Once the game has ended, players are given the option to play again

## Testing

### Desktop

Google Chrome, Mozilla Firefox & Microsoft Edge; game is running succesfully without any errors. Invalid entered data returns errors as expected. 

### Tablet & Mobile 

Huawei P20 Pro, Galaxy A40, Galaxy Tab; game is running succesfully without any errors. Invalid entered data returns errors as expected. UI issue for Galaxy Tab in landscape mode - The keyboard hides the updated game board from player view. 

## Errors

* A bug was found where the program repeatedly drew the updated game board on an endless loop. The underlying cause was determined to be a While statement in the wrong place and it was resolved once the While was placed correctly. 
* Similar bugs were found when raising Value Errors for invalid data - the errors repeatedly printed on an endless loop. Again the issue was determined to be the While statement in the wrong place and was resolved once moved. 
* Initial testing showed that revealed spaces were incorrect locations. This was resolved by allowing for 0-indexing (row/col - 1).

## Future Features

In a standard game of Minesweeper, if a player reveals a space that has 0 mines in the surrounding spaces, the board continues to reveal surrounding spaces until it finds a value. 

The current game can reveal the immediate surrounding spaces of a single space with a value of 0. If further spaces reveal 0, the spaces surrounding the new 0 are not revealed. This functionality should be added in the future. 

Creating the game board as an object may make this easier. 

## Validator Testing

### PEP8 Testing

No errors found on http://pep8online.com/ :
![](https://lh3.googleusercontent.com/pw/AL9nZEWpMqWoOmtLNaLOF5uaxAGJwEjKLEP-sP9gfnabeQaxVLrqKEFEvEm3HJIKNGxNvp4VaBNKCqJPJ74bwcVLXBar2309TdMkUmByg9Eb9sEPoEzrANp7KmqB5U42T7FfFJAf6Djfanl53Zb895imMv0a=w1062-h652-no?authuser=0)

## Deployment

This project was deployed to Heroku using Code Institute's mock terminal. 

Steps to deploy: 
1. Clone this repository.
2. Create a new Heroku app. 
3. Add buildpacks `Python` and `NodeJS` in that order.
4. Link the Heroku app to the repository. 
5. Click Deploy. 

## Credits

### Other Code

* Code for validation functions has been adapted from Code Institute's Love Sandwiches project which can be found [here](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode).
* Code for the deployment terminal has ben provided by Code Institute. 

### Acknowledgements 

* A huge thank you to Donny, Cara and Charlotte - your confidence and patience over the last couple of weeks is massively appreciated. 
* Further thanks to Carolann for all the testing.


