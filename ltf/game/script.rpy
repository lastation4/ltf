# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    "Looking out to the birds flying up high, I sometimes wish I could do the same"

    "The only people who can do so are the Hikokito..."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.


    e "Hey, ___, have they responded to your application, yet?"

    "N-No, not yet"

    e "Don't worry, they'll get back with you on it, I'm sure! See you!"

    hide eileen

    "Each time I'm asked that question, my mind plays out the words of the inevitable rejection letter."

    "No doubt about it... I've been color-blind my whole life... And color-blindedness is an automatic disqualifier."

    "So, why did I even bother in the first place..?"

    # This ends the game.

    jump act1

    return


label act1:
    scene bg room

    show eileen happy

    e "This is to test some of the functionality of RenPy."

    e "We don't got a story, yet... Stay tuned for that!"

    return
