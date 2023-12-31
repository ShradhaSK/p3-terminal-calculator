 ![download](https://github.com/ShradhaSK/p3-terminal-calculator/assets/131806140/78e6ac5e-fb13-4faf-aef8-9fdee758c251)
 # Terminal Calculator 

Welcome,

This is a terminal arithmetic calculator to fulfill all your complex calculation needs, without having to open a separate app, amazing right? 🤯
It allows you to compute complex arithmetic calculations right from the comfort of your Terminal. Beware, it is not for the faint of hearts; this will prove to be a saviour for developers all around the world, who struggle with adding an extra app window to already piling tabs and terminal windows open on their system.

## Features

- Simple operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  
- A little complex operations too:
  - Square root
  - Exponent
  - Average
  - Percentage

- There is also the feature of memory, which stores the last TEN OPERATIONS! So now you would not have start over just because you forgot one of the answers in between!

## Deployment
The project was deployed as a Heroku app. The following steps were followed:

### Creating the Heroku app

While creating the app, two buildpacks were added from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

A _Config Var_ called `PORT` was created and the value for this was set as `8000`

Connected to my GitHub repository in the Deployment section.

The app was deployed manually.

## Testing
The project was tested for bugs both in the local environment and after deployment to Heroku.
The following cases were tested:

1. Enter valid values for both numbers and operator
2. Enter invalid operator
3. Enter invalid first value
4. Enter invalid second value
5. Enter one of the non-arithmetic valid operators (M, H)

All the tests passed, and no bug was detected in the deployed app.

## Credits
- Read a short article on [Stack Overflow]([url](https://stackoverflow.com/)) on how to add the memory feature for the calculator
- Watched a short video on python classes and and how to use them.

## Media
- Downloaded Calculator icon for the README.md file from [Icon Finder](https://www.iconfinder.com/icons/171352/calculator_icon)

