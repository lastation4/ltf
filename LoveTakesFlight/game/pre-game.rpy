# The script of the game goes in this file.

# disable the back button, cause you have to save scum
define config.rollback_enabled = True

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define some administrative characters
define v = Character("lastation4")
define nameunknown = Character("???")
define two = Character("The Two of You")

#define yourself...wow that's deep
define m = Character("You")

#define your family
define father = Character("Father")
define a330 = Character("Airbus A330-300")
define b757 = Character("Boeing 757-200")

#define side characters

define airbus_chair = Character("Airbus Chairman")
define boeing_chair = Character("Boeing Chairman")

#define some gorls
define b777 = Character("Boeing 777-300ER")
define a320 = Character("Airbus A320 neo")
define b737 = Character("Boeing 737-800")
define b747 = Character("Boeing 747-8")
define crj = Character("Bombardier CRJ-900")
define erj = Character("Embraer ERJ-190")
define a350 = Character("Airbus A350-900")
define a340 = Character("Airbus A340-600")

#begin to define stats here
#a330 doesn't like you that much, but you're still family, hence, set to -2
define affinity_a330 = -2
#757 loves her older sibling, so she's set to 2.
define affinity_757 = 2
define affinity_777 = 0
#a320 is set to 5 because she's your childhood friend
define affinity_a320 = 5
#737 is a tsundere, so -2 to you!
define affinity_737 = -2
define affinity_crj = 0
define affinity_erj = 0
define affinity_747 = 0
define affinity_a350 = 0
#a340 is set to -5 because she's supposed to be VERY HARD TO GET
define affinity_a340 = -5

#define and init character attributes
#INT shows how smart you are, you'll have an easier time impressing girls that like INT
define intel = 0
#confidence shows how ballsy you are.
define confidence = 0
#CHA shows how charming you are to others, like INT, this will make charming the panties off the girls easier
define cha = 0
#DEX defines how good you are at manual tasks, like jobs, example: helping A320 with her lawnmowing business
define dex = 0
#WIS is a special stat that will help you make the right decision for girls that you have over 5 affinity with.
define wis = 0

#general flags go here

define prealpha = False

# The game starts here.

label start:

    scene bg prealpha

    if prealpha == True:
        jump alphatest
    else:
        jump d1_gameStart

# This block is just a showcase of the girls if the Alpha Test flag is set. 

label alphatest:

    v "Hello, and welcome to the pre-alpha of Love Takes Flight!"

    v "If you're seeing this, everything is working well!"

    v "Here's a showcase of the sprites for now to make sure everything is loading right!"

    show 737

    v "This is 737, she's a tsundere."

    hide 737

    show 747

    v "This is 747, she's a himedere."

    hide 747

    show 777

    v "This is 777, she's total waifu material."

    hide 777

    show crj

    v "This is CRJ. She's based off of pre-transition Maxwell. Obviously the best plane."

    hide crj

    show erj

    v "This is ERJ. She's a homo."

    hide erj

    v "That's all for now. Enjoy the pre-alpha!"


    scene black with dissolve

    jump gameEnd