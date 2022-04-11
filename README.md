# Game, review App

# Creator - Tony Zherka

* Objective
To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

* Project:

To create a working Web Application where users can access to leave reviews on the games of there choice.

The implicit CRUD functionality of this app will include:

* CREATE

  -Add Games

  -Add reviews

* READ

  -View all reviews

  -View all games to review

* UPDATE

  -Edit reviews of games

  -Update games

*DELETE

  -Delete games of there choice

  -Remove reviews of games

## Planning, Design and Project Tracking

## CI Pipeline

The pipeline image represents what services and tools that have been chosen for each stage of development. I used flask to quickly build the app including the database schema which conected to an external SQL instance as it is more secure.

![new pipeline](https://user-images.githubusercontent.com/101265381/162474402-1b394371-f31b-4c32-b60b-73b6d3a8b6dd.png)


## Trello Board

firstly i began making a trello board so i knew which was the route i was going to go down from deciding what to create first and what to move on to next, and see my overall progress here is a link to the trello board. ![TrelloBoard](![trello board1](https://user-images.githubusercontent.com/101265381/162193724-7fdce9b5-5484-4bee-8383-9cef30422263.png)

after coming near the end of the project a few things changed on the trello board.

* more user stories
* main requirement to be completed 90%+ for coverage with jenkins
* move all files to done that have been completed

![updated trello board](https://user-images.githubusercontent.com/101265381/162486540-6fb2b3bb-d695-44a1-9491-1b70a36cfd23.png)


## ERD

I made a basic relationship diagram around with the idea of the expected entities, the diagram might change further into the project but this was my initial design. 

![Erd](https://user-images.githubusercontent.com/101265381/162194438-e733ae8b-c548-4a3f-b8c2-7e5a24336906.png)

after some thought, i came to realise that i wouldnt need the date and time unless i was adding another diagram for users, if i had more time i would have implemented a user diagram and made many to many relationships.

![updated erd diagrams net](https://user-images.githubusercontent.com/101265381/162431085-3bd74534-9533-4a15-900b-e6da4b7465b4.png)


## Risk Assessment

My risk assessment, though basic, attempted to percieve possible threats to the project. The entries with proposed Control Measures as opposed to implemented were considered and noted later on towards the end of the project.

![Risk_Ass](https://user-images.githubusercontent.com/101265381/162195607-c3c0ead6-f251-43a9-8da6-ac520720160a.png)

## Front End Design

for the front end design the main goal was to have a simple but working navbar for people to use.
when users navigated to the URL, they would be greeted with this page.

![working nav bar](https://user-images.githubusercontent.com/101265381/162477252-99e137c7-43a8-4d7c-bc36-ed8db203064d.png)

once on this page they can navigate through the options.
if they wanted to add a game, they will be greeded with a page with 3 opens, the title of the game, the genre of the game and the developer of the game.

![add game](https://user-images.githubusercontent.com/101265381/162478057-501970b9-d871-464d-abb5-033a3f3fa68f.png)

after adding a game the user can click on see added games where they can update or delete the games of there choice.

![working gamelist with update and delete button](https://user-images.githubusercontent.com/101265381/162478769-db1263d8-7579-4823-bdb5-9bc93fecca37.png)

here they can see all added games, and decide if they want to update them or delete them, if the user wants to keep the game and add a review keep note of the number ie (destiny2 = number 11)they can navigate through to create review page, where the user can input there name the review they would like to add

![add review working](https://user-images.githubusercontent.com/101265381/162481038-787b8c17-6814-4076-a9d8-492f40a13d69.png)

after adding review, you can navigate to see all added reviews at the top, once you are in see all reviews you can update or delete exisiting reviews.

![working review list](https://user-images.githubusercontent.com/101265381/162481296-74ef61aa-6bb3-4a87-bd0d-2b250cfe1ce1.png)

from here people can delete or update existing reviews, users cant delete games that are connected to reviews the only way to delete a existing game they would have to remove all reviews with that game.

## Testing and issues

For testing i originally used pytest to run tests on all of my code to make sure i got above 90% coverage, but ended up running into issues. The main issues i was encountering was making tests work for my update and delete functions. the reason i was having issues is because you cant delete a game without having the review deleted so i had to have both delete functions in one, had to make sure the review function was going first so it deleted the review first before the game. after to make sure the test was working i had to assert something that was always in the webpage for games it was (Games list) and reviews it was (Review list) reason why was because when a game was deleted it would still be in the same web page, but after fixing these changes i was able to reach a coverage of 98%.

below you will have the code and the pytest coverage report.

![test code](https://user-images.githubusercontent.com/101265381/162483849-c2b172f3-5e09-4971-96ed-ce8aee25c286.png)


![pytest coverage](https://user-images.githubusercontent.com/101265381/162475058-0a0e45b5-ad60-4b67-92bd-108f53c045d2.png)

after tuning and fixing my code i ended up with a overall 98% achieved coverage on my tests i then implemented jenkins to automatically run these tests as seen below.

![working jenkins updated](https://user-images.githubusercontent.com/101265381/162475409-a96600fe-9760-4b0b-9a69-34b358936e6f.png)


## Future Improvements

there are a few improvements i would like to add if i had more time like:

* Adding users into the data base so people can log in and make accounts
* Adding times and dates of when reviews have been made
* Adding scroll menus for users to be able to select which games they would like to review
* Making the App more appealing and functional for users.

## Authors

Tony Zherka

## Acknowledgement

Many thanks to Earl Grey for the teaching to get me to this stage to be able to complete my own project and helping with any errors that have happened also want to say a thank you to Harry Volker, Leon Robinson and Wei Yao my fellow collegue.

Earl Grey, Harry Volker, Leon Roobinson, Wei Yao


