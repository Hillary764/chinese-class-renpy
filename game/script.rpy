# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


default pengyouEnd = 0
default leiEnd = 0
default jiarenEnd = 0
default haowanEnd = 0

default numberOfTurns = 5
default turnCount = 0

default lastAction = ""



# The game starts here.


label start:

    menu:
        "你想玩电子游戏玩得怎么样？"

        "玩电子游戏玩得很多":
            $ numberOfTurns = 15
        
        "玩电子游戏":
            $ numberOfTurns = 10
        
        "玩电子游戏玩得很少":
            $ numberOfTurns = 5

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room
    scene bg Untitled

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    L "我叫小猫。"
    L "我比别的猫很漂亮，很能干，很有灵气。"
    L "我想我是最好的猫。"

    jump houseOptions

    # This ends the game.

    return
