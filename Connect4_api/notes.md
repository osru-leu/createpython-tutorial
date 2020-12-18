# Day 30 Notes

## Connect 4 Pseudo code Game

Rough steps
MVP - Minimum Viable Product
- 2 player game
    - Assignment of Player to either player1 or player 2

- Need a board
    - Dimensions (7wide x 6high array)


- Moves
    - Input from player and place it on the board (what column you want to drop in)
        - Validate move
            - Valid Criteria:
                - Make sure the column is not full before dropping in (i.e. there is not already 6 items in column)
                    - isColumnFull attribute
                - Column selected must be within range (0-6 since it is 7 wide)
            - If Valid
                - Place the move
                    - determine the vertical position
                        - Keep going down the column till right before you hit a non-zero position or the beginning of column
                    - track which player took the position (i.e. fill th eposition with 1 or 2)
                - Win Check
                    - If Win then end of game and ask if they want to play again
                    - If no winner
                        - Check if there are any remaining possible moves
                            - If all columns isColumnFull=true
                                - Declare a tie and ask if they want to play again
                            - Else
                                - Ask next player to enter move (start over on the moves)
            - If Invalid
                - notify user that its invalid
                - prompt same user to retry

- Display the board
GET /board

- Alternate players


/move
    - the player
    - column

PUT /players/{playerId=1 or 2}/move/{columnId=0-6}

        2 0 0 0 0 0 0
        1 0 0 0 0 0 0
        2 0 0 0 0 0 0
        1 0 0 0 0 0 0
        2 0 0 0 0 0 0
[0,0]   1 0 0 0 0 0 0

sequence of plays
PUT /players/1/move/0
    - valid: 1 at [0,0]
    response:
        {
            "board": [
                2 0 0 0 0 0 0
                1 0 0 0 0 0 0
                2 0 0 0 0 0 0
                1 0 0 0 0 0 0
                2 0 0 0 0 0 0
                1 0 0 0 0 0 0
            ],
            "status": "WIN | TIE | IN_ACTION | INVALID_MOVE | INVALID_PLAYER",
            "message": "Some more details about the status",
            "playerUp": 1 or 2,
            "winner": None, 1, or 2,
            "playerRed": {playerId},
            "playerYellow": {playerId}
        }
PUT /players/1/move/0
    - invalid move
PUT /players/2/move/0
    - valid: 2 at [0,1]
PUT /players/3/move/0
    - invalid player
PUT /players/1/move/0
    - valid: 1 at [0,2]
PUT /players/2/move/0
    - valid: 2 at [0,3]
PUT /players/1/move/0
    - valid: 1 at [0,4]
PUT /players/2/move/0
    - valid: 2 at [0,5]
PUT /players/1/move/0
    - invalid move (column full)



- Ask if they want to play again at the end of the game
- Win / Draw / Abort

POST /players  <-- creates a player
    - playerId
    - displayName

POST /games  <-- creates a new game
    - Response
        {
            "id": 123, <-- autogenerate id (google it... mongo autoincrement id python)
            "board": [
                0 0 0 0 0 0 0
                0 0 0 0 0 0 0
                0 0 0 0 0 0 0
                0 0 0 0 0 0 0
                0 0 0 0 0 0 0
                0 0 0 0 0 0 0
            ],
            "status": "NOT_STARTED | WIN | TIE | IN_ACTION | INVALID_MOVE | INVALID_PLAYER",
            "message": "Some more details about the status",
            "playerUp": 1,
            "winner": None
            "playerRed": None,
            "playerYellow": None
        }
PUT /games/{gameId}/player-yellow/{playerId}
PUT /games/{gameId}/player-red/{playerId}

PUT /games/{gameId}/move/{playerId}/column/{columnId}

## Assignement for Thursday

* Create PUT /players endpoint
    - Attributes:
        - playerId <-- autogenerate or not...has to be unique
        - displayName
* Create GET /players
    - Returns a list of players in DB

* Create PUT /games endpoint
    - Attributes:
        - gameId <-- auto-generated
        - board
        - status
        - message
        - playerUp
        - winner
        - playerRed
        - playerYellow
* Create GET /games
    - Returns a list of games in DB


function for ai id
function getValueForNextSequence(sequenceOfName){
...
...   var sequenceDoc = db.sample.findAndModify({
...     query:{_id: sequenceOfName },
...      update: {$inc:{sequence_value:1}},
...      new:true
...    });
...
...     return sequenceDoc.sequence_value;
... }


Needed Changes

board --> array

playerRed--> fields.Integer
playerYellow --fields.Integer

ERRORS

    PUT_GAME
        XXX-throwing error
            XXX-game name is a required property error

TALKING POINTS
    -XXXXNaming conventions namespace fields to parameters
    -Entering a an id number when it is auto generated
        solution in progress:
            -removed gameId field(s) from namepace.
            -reroute displayName as game_id
            -create a separate post games schema.py? why? review video for possible answer


DEBUGS
    PUT
    - now not working due to changes in routing through gameId instead of displayName
    DELETE
        -Debug DELETE games via game_id
            fix find
        -Debug Players DELETE


WORKING
    -GAMES
       - GET ONE
        -GET ALL
        -PUT
        -POST

NEEDED 
    xxxa displayName check so 2 of the same names cannot exist


    