# Blackjack 
Write a program that allows a user to play against a computer 'dealer'. 

## Rules

The rules for this game of blackjack are covered below and should be used to create the program in addition to the requirements.
Note that these may not be standard rules or the ones that you are used to, so pay careful attention to these.

- A single deck of standard (52) playing cards is used
- Cards are worth the value of the number on the card (e.g. 2 of Clubs is worth 2), all 'Face Cards' (e.g. King, Queen) are worth 10.
- An ace is worth 11, unless the player has more than 2 cards, in which case it is worth 1.
- During a turn, the player can either choose to 'hit' or 'stick':
    - If the player 'hits' then they draw a card from the deck, which is drawn at random. The dealer must hit until their hand is above the value of 17. 
    - If the player 'sticks' then they will not draw a card and they will be unable to take any further turns in the game. The dealer must stick if the value of their hand is above the value of 17.
- The player plays until they have chosen to 'stick' or have gone bust, then the dealer will play their turn. 
- The following are the winning conditions:
    - If the player is dealt an Ace and a ten-value card, and the dealer does not, the player wins.
    - If the player exceeds a sum of 21 ("busts"); the player loses, even if the dealer also exceeds 21.
    - If the dealer exceeds 21 ("busts") and the player does not; the player wins.
    - If the player attains a final sum higher than the dealer and does not bust; the player wins.
    - If both dealer and player receive a blackjack or any other hands with the same sum called a "push", no one wins.

For any situation not covered by the rules above, you should use your best judgement (perhaps with a comment justifying why you took the approach you did).

## Additional Requirements

The following requirements are mandatory for your solution:

- The program must tell the user which cards they have been dealt (e.g. 9 of Hearts)
- The program must have an interface the user can use to play, this can be via a CLI REPL or you can create a GUI for this
- The program must prompt the user for their decisions and compute the result accordingly
- The program must display the total value of the hand at any given time
- The program must show the user whether they won or lost a round
- The program must allow the user to gracefully exit at the end of each round 

You must select at least one of the following requirements to implement, you are welcome to do more than one, but will not penalised if you do not:

- The program should keep track of 'wins' by both the dealer and the player within a session and display this when prompted 
- The program should provide some statistical guidance about whether the user should 'hit' or 'stick', e.g. recommend hitting at 12, recommend sticking at 20
- The program should allow for multiple human players (using the same screen, no need for networking etc), these players must be named and are only competing against the dealer, not each other
- The program should allow users to associate bets with each round and maintain a total 'pot' for the user
- The program should allow users to specify how many decks they want to play with (e.g. 1 deck, 2 decks, 4 decks), rather than just using the single deck

## Objectives 

The purpose of this challenge:

- Write clean, robust, well factored, well named, easy to understand code.
- Understand the requirements and produce a result that satisfies them, your solution will be measured directly against the requirements, particularly as there are specific game rules in place.
- Create an easy-to-use interface for the application, whether that's graphical or textual, ease-of-use will be scored highly.
- Anticipate ways in which the app could fail and test to make sure those situations are accounted for, including invalid input.

What won't be specifically judged:
- Performance optimization.
- Writing everything from scratch, if it is already offered in an existing standard library then you should use it.

## Documentation
There should be instructions on how to run the program, including installing any dependencies. 
If the interface needs explaining (e.g. command examples) then please also provide this detail.

## Rules
- You may use any of the following programming languages: `Python`, `Java`, `Go`, `C/C++`, `C#`, `Node.js`.
- Feel free to use any built-in standard libraries for the programming language you intend to use.  You may also use a 3rd party library, but please justify its use and explain the reason for doing so.
- You may not ask specific questions on Stack Overflow or to anyone you know, you can ask clarifying questions to the person who set the challenge.

