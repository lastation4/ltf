# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("LTFdev")
define m = Character("Me")
define father = Character("Father")
define sister_airbus = Character("A330-chan")
define sister_boeing = Character("757-chan")
define nameunknown = Character("???")
define tripleseven = Character("777-chan")

define affinity_a330 = 0
define affinity_757 = 0
define affinity_777 = 0

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
        show a330_scolding
        nameunknown "Hey. Maybe watch where you're going, idiot."
        "Your sister, A330 looks at you, expecting an apology."
        m "S-sorry sis, I'm just really excited and wasn't really thinking..."
        sister_airbus "Well, maybe think next time! We're going to be late if we don't get going soon!"
        "You nod, and go downstairs with her and meet up with your father."
    else:
        show 757
        nameunknown "Waah! Watch out! We're going to crash! Nyeaowwwww!"
        hide 757 with moveoutleft
        "Your sister, 757, quickly darts to the left of you, and hops down the stairs."
        sister_boeing "HEY! HURRY UP! YOU DON'T WANT TO BE LATE! DAD'S WAITING!"
        "You sigh. She's always been this hyper. You decide to head downstairs and meet up with your father."
    scene black with dissolve

label driveToSchool:
    scene bg car
    if father_is_airbus:
        "You and A330 get into the car with your father."
        show a330_stoic
        "A330 stares out the window."

    else:
        "You and 757 get into the car with your father"
        show 757_cellphone
        "757 sits on her legs and pulls out her phone, playing some random anime game."

    m "Hey sis, I was wondering...what team should I pick? They both have their advantages, but I'm kinda stuck..."

    if father_is_airbus:
        show a330_shrug
        sister_airbus "It doesn't really matter to me, but shouldn't you just go with the family team? Should be an easy choice."
        m "You're right, that's probably a good idea. Wouldn't want to make dad mad by picking Boeing..."
        "You laugh dryly to yourself, and try to change the subject."
        m "Yeah imagine if I picked Boeing, what would you do Dad?"
    else:
        show 757_phone_talk
        sister_boeing "Obviously Boeing! You don't want to upset Dad after all the hard work he put in landing this job!"
        m "You're right, that's probably a good idea. Wouldn't want to make dad mad by picking Airbus..."
        show 757_phone_laugh
        "You and 757 both laugh."
        m "Yeah imagine if I picked Airbus, what would you do Dad?"
    show father
    father "I'd disown you."
    m "What...?"
    if father_is_airbus:
        show a330_annoyed
        sister_airbus "Dad, really? I mean...that's kind of awful to say."
    else:
        show 757_shocked
        sister_boeing "DAD! WHY WOULD YOU SAY SUCH A HORRIBLE THING!"
    "You gulp audibly."
    m "...you're serious?"
    show father
    if not father_is_airbus:
        father "Of course not. It's your choice, and I respect the competition and technological innovation that Airbus brings to the market. Without their advanced avionics, Boeing wouldn't have upgraded theirs. Competition is healthy."
        show 757_scolding
        sister_boeing "Dad! Don't play around like that!"
        show 757_smile
    else:
        father "Of course not. It's your choice, and I respect the competition and legacy that Boeing has. They do have a way with making their planes look nice. Competition is healthy."
        show a330_stoic
        "A330 continues to stare out the car window..."

    m "Okay, that's a relief. Thanks for supporting my decision. "
    "You wonder to yourself what that decision is going to be...Boeing or Airbus..."
    "..."

    v "DEV NOTES: Filler Conversation with your sister on the way to school."

    scene black with dissolve

label arriveAtSchool:
    scene bg car
    show father
    father "At last, after all that awful traffic we're here!"

    "A bell chimes in the distance...You'd better hurry off to the opening ceremony!"

    m "See ya Dad! Gotta go!"
    hide father with moveoutleft
    scene bg school_outside_main_campus

    "You get out of the car and rush off to the school gym."

    "...at least you would if you knew where it was..."

    "..."

    "You decide to ask someone where the gym is."

    "...you look around trying to get someone's attention..."

    show 777chan_flustered

    "You spot a Senior that looks like she's either lost, or confused..."

    m "Excuse me, do you know where the gym is? I don't want to be late for the ceremony."

    nameunknown "Ah! U-u-um...were y-you talking to...m-me?"

    m "Yeah, are you alright?"

    show 777chan_point_right

    nameunknown "Y-yeah...I guess. The gym is that large building over there..."

    show 777chan_shy

    "She points to a large building that has a banner on it, which reads \"Welcome New Cadets\""

    m "How could I miss that. Wow. You probably think I'm an idiot."

    nameunknown "W-what! No! I don't think that at all!"

    m "Well since we're headed the same way, how about we go together?"

    show 777chan_blush

    nameunknown "A...ah! Yes, that's a good idea, wouldn't want either of us getting lost..."

    show 777chan

    nameunknown "B...by the way I'm 777, b-but my friends call me \"Triple Seven\"."

    "You tell 777 what your name is."

    "..."

    tripleseven "L-lovely weather we've been having..."



    menu:
        "She's trying to make small talk with you...better change the subject..."
        "Y...yeah...weather's been nice...":
            jump tripleseven_smalltalk
        "So 777, I see you're a third year, mind asking what team are you on?":
            jump tripleseven_classrank
        "...":
            jump tripleseven_noresponse




label tripleseven_classrank:
    $ affinity_777 -= 1

    show 777chan_disappointed
    tripleseven "Oh...um...Boeing..."

    "She's a Boeing girl, I should have known that!"

    jump walkToGym

label tripleseven_smalltalk:
    #no affinity gain for smalltalk
    show 777chan_finger_poke_together
    tripleseven "..."
    jump walkToGym


label tripleseven_noresponse:
    $ affinity_777 += 1
    show 777chan_finger_poke_together
    tripleseven "Y-you're a transfer student, right?"
    m "Yeah, how'd you know? Is it that obvious?"
    show 777chan_glasses_push
    tripleseven "Y-yeah, I mean, you have two bars on your uniform, so that means you're...second year."
    tripleseven "That must mean transfer! R-right?"
    m "Ding ding ding, you're right!"
    show 777chan_flustered
    tripleseven "W-what?"
    if not father_is_airbus:
        m "Guess my little sister's demeanor is rubbing off on me..."
    else:
        m "Guess I've been watching too many gameshows. Sorry."


label walkToGym:
    v "DEVNOTE: Continue the conversation depending on affinity with 777, affinity 1, she'll sit with you, affinity 0, you have to convince her, affinity -1, she's sitting with her \"friends\""

label openingCeremony:
    v "DEVNOTE: The StuCo president makes a speech after the two team chairmen make their opening speeches, trying to sell their teams to the students. "


    # This ends the game.
    v "This is the end of this pre-alpha test."
    return
