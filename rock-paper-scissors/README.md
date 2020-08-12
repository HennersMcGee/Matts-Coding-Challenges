# Rock, Paper, Scissors
Write a program that can calculate the winner based on moves for [Rock, Paper, Scissors](https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors).

## Input 
The program should take a either a local filename or a remote URL as input, which contains JSON with the following format:

```
[
    {
        "Player1": "rock",
        "Player2": "paper"
    },
    {
        "Player1": "paper",
        "Player2": "scissors"
    }
]
```

For example, the program could be called like (ignoring language specific commands):

```
./my_program /path/to/local/file
```

Or

```
./my_program https://example.com/rock_paper_scissors.json
```

Each row in the JSON array represents a game round with each player's move.
NOTE: this is only a sample input.  When your program is evaluated, it will be tested with a more exhaustive input file.

## Expected Output
The final output should be a JSON file in the following format:

```
[
    {
        "Winner": "Player2",
        "Inputs": {
            "Player1": "rock",
            "Player2": "paper"
        }
    },
    {
        "Winner": null,
        "Inputs": {
            "Player1": "scissors",
            "Player2": "scissors"
        }
    }
]
```

Each row in the ouput also represents a game round, but in addition to each player's moves, it will contain a field that declares the winning player.  If it is a tie, then the `Winner` field should have `null` since there is no winner.

The output should be written to `stdout`.

## Implementation
It is up to you to implement the code that can take the input JSON and output the expected output JSON with correct winners chosen for each game round.  
It should be able to handle an input file up to 10 MB in size.

## Testing
Write an end-to-end test that verifies that the program behaves correctly.  
The test should exhaustively cover as many input and output combinations as possible.

## Documentation

There should be instructions on how to:

- Build/run the code with an arbitrary file or URL.
- Run the test suite.

## Objectives 

The purpose of this challenge:

- Write clean, robust, well factored, well named, easy to understand code.
- Write code that clearly informs the user of the program results.  For example if the user calls the program with an input argument that references a non-existent file or URL, it should tell them that directly so they will know to rerun it with a valid file or URL.
- Understand the requirements and produce a result that satisfies them.
- Write tests that demonstrate the program correctness in a compelling manner.
- Anticipate ways in which the app could fail and test to make sure those situations are accounted for, including invalid input.

What won't be specifically judged:
- Performance optimization.
- Writing everything from scratch, if it is already offered in an existing standard library then you should use it.

## Rules
- You may use any of the following programming languages: `Python`, `Java`, `Go`, `C/C++`, `C#`, `Node.js`.
- Feel free to use any built-in standard libraries for the programming language you intend to use.  You may also use a 3rd party library, but please justify its use and explain the reason for doing so.
- You may not ask specific questions on Stack Overflow or to anyone you know, you can ask clarifying questions to the person who set the challenge
