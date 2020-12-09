# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Mysterious Voice")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    v "Hello, and welcome to the pre-alpha of Love Takes Flight!"

    v "If you're seeing this, everything is working well!"

    v "Here's a picture of the ultimate waifu of this game!"

    v "...well a concept at least"

    show 737

    v "Isn't she cute?"

    v "Well that's all for now! Thanks for testing."

    # This ends the game.

    return
