# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("LTFdev")
define m = Character("Me")
define father = Character("Father")
define sister_airbus = Character("A330-chan")
define sister_boeing = Character("757-chan")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg prealpha

    v "Hello, and welcome to the pre-alpha of Love Takes Flight!"

    v "If you're seeing this, everything is working well!"

    v "Here's a picture of the ultimate waifu of this game!"

    v "...well a concept at least"

    show 737 with moveinright

    v "Isn't she cute?"

    hide 737 with moveoutleft

    v "Here's another girl!"

    show crj with moveinright

    v "Well let's get started."

    scene black with dissolve

label gameStart:

    scene bg room

    "The sun is shining bright through your window; Today is the first day at your new school."

    "You toss and turn a little bit, not wanting to leave the warmth of your bed"

    "You hear a knock at your door and a familiar voice."

    father "Wake up, you'll be late for the entrance ceremony if you don't catch the train soon!"

    "You roll out of bed slowly and begin to gather your things."

    "Shirt: check."
    "Pants: check."
    "Schoolbag: check."

    father "Forget the train, I'll drop you by school on my way to work."

    "That's right, your father is one of the two chairmen at your new school."
    "The school you will attend is quite different from that of other schools, in that during the entrance ceremony, you must pick a \"team\" that you must join."

    m "I wonder what team I will join... Probably should pick the one that Dad is the chairman of."


    ##randomly pick which "team" your father is chairing

    $ chairman_airbus_number = 1

    if renpy.random.randint(1,2) == chairman_airbus_number:

        "You recall that he heads up the technologically advanced Airbus team."
        "You should probably pick Airbus at your entrance ceremony."
        $ father_is_airbus = True
    else:
        "You recall that he heads up the tried and true Boeing team."
        "You should probably pick Boeing at your entrance ceremony."
        $ father_is_airbus = False

    m "Time to get going, don't want to be late on the first day of school!"

    scene black with dissolve

    scene bg hallway with dissolve

    "You rush out of your bedroom, and run head-first into your sister."

    if father_is_airbus:
        show a330
        sister_airbus "Hey. Maybe watch where you're going next time, idiot."
        "You look down at your shoes and apologize."
        m "S-sorry sis, I'm just really excited and wasn't really thinking..."
        sister_airbus "Well, maybe think next time! We're going to be late if we don't get going soon!"
        "You nod, and go downstairs with her and meet up with your father."
    else:
        show 757
        sister_boeing "Waah! Watch out! We're going to crash! Nyeaowwwww!"
        hide 757 with moveoutleft
        "Your sister quickly darts to the left of you, and hops down the stairs."
        sister_boeing "HEY! HURRY UP! YOU DON'T WANT TO BE LATE! DAD'S WAITING!"
        "You sigh. She's always been this hyper. You decide to head downstairs and meet up with your father."
    scene black with dissolve

label driveToSchool:

    if father_is_airbus:
        "You and A330 get into the car with your father."
        scene intro_a330_carwindow
        "A330 stares out the window."

    else:
        "You and 757 get into the car with your father"
        scene intro_757_car
        "757 sits on her legs and pulls out her phone, playing some random anime game."

    m "Hey sis, I was wondering...what team should I pick? They both have their advantages, but I'm kinda stuck..."

    if father_is_airbus:
        sister_airbus "It doesn't really matter to me, but shouldn't you just go with the family team? Should be an easy choice."
        m "You're right, that's probably a good idea. Wouldn't want to make dad mad by picking Boeing..."
        "You laugh dryly to yourself, and try to change the subject."
        m "Yeah imagine if I picked Boeing, what would you do Dad?"
    else:
        sister_boeing "Obviously Boeing! You don't want to upset Dad after all the hard work he put in landing this job!"
        m "You're right, that's probably a good idea. Wouldn't want to make dad mad by picking Airbus..."
        "You and 757 both laugh."
        m "Yeah imagine if I picked Airbus, what would you do Dad?"
    father "I'd disown you."
    m "What...?"
    if father_is_airbus:
        sister_airbus "Dad, really? I mean...that's kind of awful to say."
    else:
        sister_boeing "DAD! WHY WOULD YOU SAY SUCH A HORRIBLE THING!"
    "You gulp audibly."
    m "...you're serious?"
    if not father_is_airbus:
        father "Of course not. It's your choice, and I respect the competition and technological innovation that Airbus brings to the market. Without their advanced avionics, Boeing wouldn't have upgraded theirs. Competition is healthy."
    else:
        father "Of course not. It's your choice, and I respect the competition and legacy that Boeing has. They do have a way with making their planes look nice. Competition is healthy."

    v "This is the end of this pre-alpha test."

    # This ends the game.

    return
