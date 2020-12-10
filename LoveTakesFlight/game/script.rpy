# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#define some administrative characters
define v = Character("lastation4")
define nameunknown = Character("???")

#define yourself
define m = Character("Me")


#define your family
define father = Character("Father")
define sister_airbus = Character("Airbus A330-300")
define sister_boeing = Character("Boeing 757-200")

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

#define character attributes
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



define prealpha = True


# The game starts here.

if prealpha == True:
    jump start
else:
    jump gameStart


label start:

    scene bg prealpha

    v "Hello, and welcome to the pre-alpha of Love Takes Flight!"

    v "If you're seeing this, everything is working well!"

    v "Here's a showcase of the sprites for now to make sure everything is loading right!"

    show 737

    v "This is 737, she's a tsundere."

    hide 737

    show 747

    v "This is 747, she's a himedere."

    hide 747

    show 777chan

    v "This is 777, she's total waifu material."

    hide 777chan

    show crj

    v "This is CRJ. She's based off of pre-transition Maxwell. Obviously the best plane."

    hide crj

    show erj

    v "This is ERJ. She's a homo."

    hide erj

    v "That's all for now. Enjoy the pre-alpha!"


    scene black with dissolve

label gameStart:

    scene bg room

    "The sun is shining bright through your window; Today is the first day at your new school."

    "You toss and turn a little bit, not wanting to leave the warmth of your bed"

    "You hear a knock at your door and a familiar voice."

    father "Wake up, you'll be late for the entrance ceremony if you don't leave now!"

    "You roll out of bed slowly and begin to gather your things."

    "Shirt: check."
    "Pants: check."
    "Schoolbag: check."

    father "Forget walking, we're out of time. I'll drop you by school on my way to work."

    "That's right, your father is one of the two chairmen at your new school."
    "The school you will attend is quite different from that of other schools, in that after the entrance ceremony, you must pick a \"team\" that you must join."

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
        #show a330_scolding
        show a330
        nameunknown "Hey. Maybe watch where you're going, idiot."
        "Your sister, A330 looks at you, expecting an apology."
        m "S-sorry sis, I'm just really excited and wasn't really thinking..."
        sister_airbus "Well, maybe think next time! We're going to be late if we don't get going soon!"
        "You nod, and go downstairs with her and meet up with your father."
        hide a330 with moveoutleft
        #hide a330_scolding with moveoutleft
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
        #show a330_stoic
        show a330
        "A330 stares out the window."

    else:
        "You and 757 get into the car with your father"
        show 757
        #show 757_cellphone
        "757 sits on her legs and pulls out her phone, playing some random anime game."

    m "Hey sis, I was wondering...what team should I pick? They both have their advantages, but I'm kinda stuck..."

    if father_is_airbus:
        #show a330_shrug
        sister_airbus "It doesn't really matter to me, but shouldn't you just go with the family team? Should be an easy choice."
        m "You're right, that's probably a good idea. Wouldn't want to make dad mad by picking Boeing..."
        "You laugh dryly to yourself, and try to change the subject."
        m "Yeah imagine if I picked Boeing, what would you do Dad?"
    else:
        #show 757_phone_talk
        sister_boeing "Obviously Boeing! You don't want to upset Dad after all the hard work he put in landing this job!"
        m "You're right, that's probably a good idea. Wouldn't want to make dad mad by picking Airbus..."
        #show 757_phone_laugh
        "You and 757 both laugh."
        m "Yeah imagine if I picked Airbus, what would you do Dad?"
    show father
    father "I'd disown you."
    m "What...?"
    if father_is_airbus:
        #show a330_annoyed
        sister_airbus "Dad, really? I mean...that's kind of awful to say."
    else:
        #show 757_shocked
        sister_boeing "DAD! WHY WOULD YOU SAY SUCH A HORRIBLE THING!"
    "You gulp audibly."
    m "...you're serious?"
    show father
    if not father_is_airbus:
        father "Of course not. It's your choice, and I respect the competition and technological innovation that Airbus brings to the market. Without their advanced avionics, Boeing wouldn't have upgraded theirs. Competition is healthy."
        #show 757_scolding
        sister_boeing "Dad! Don't play around like that!"
        #show 757_smile
    else:
        father "Of course not. It's your choice, and I respect the competition and legacy that Boeing has. They do have a way with making their planes look nice. Competition is healthy."
        #show a330_stoic
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
    hide father
    scene bg school_outside_main_campus

    "You get out of the car and rush off to the school gym."

    "...at least you would if you knew where it was..."

    "..."

    "You decide to ask someone where the gym is."

    "...you look around trying to get someone's attention..."

    show 777chan

    "You spot a Senior that looks like she's either lost, or confused..."

    m "Excuse me, do you know where the gym is? I don't want to be late for the ceremony."

    nameunknown "Ah! U-u-um...were y-you talking to...m-me?"

    m "Yeah, are you alright?"

    #show 777chan_point_right

    nameunknown "Y-yeah...I guess. The gym is that large building over there..."

    #show 777chan_shy

    "She points to a large building that has a banner on it, which reads \"Welcome New Cadets\""

    m "How could I miss that. Wow. You probably think I'm an idiot."

    nameunknown "W-what! No! I don't think that at all!"

    m "Well since we're headed the same way, how about we go together?"

    #show 777chan_blush

    nameunknown "A...ah! Yes, that's a good idea, wouldn't want either of us getting lost..."

    #show 777chan

    nameunknown "B...by the way I'm 777, b-but my friends call me \"Triple Seven\"."

    "You tell 777 what your name is."

    "..."

    b777 "L-lovely weather we've been having..."

    menu:
        "She's trying to make small talk with you...better change the subject..."
        "Y...yeah...weather's been nice...":
            jump b777_smalltalk
        "So 777, I see you're a third year, mind asking what team are you on?":
            jump b777_classrank
        "...":
            jump b777_noresponse

label b777_classrank:
    $ affinity_777 -= 1

    #show 777chan_disappointed
    b777 "Oh...um...Boeing..."

    "She's a Boeing girl, I should have known that!"
    "Now I look like an idiot!"

    jump walkToGym

label b777_smalltalk:
    #no affinity gain for smalltalk
    #show 777chan_finger_poke_together
    b777 "..."
    jump walkToGym


label b777_noresponse:
    $ affinity_777 += 1
    #show 777chan_finger_poke_together
    b777 "Y-you're a transfer student, right?"
    m "Yeah, how'd you know? Is it that obvious?"
    #show 777chan_glasses_push
    b777 "Y-yeah, I mean, you have two bars on your uniform, so that means you're...second year."
    b777 "That must mean transfer! R-right?"
    m "Ding ding ding, you're right!"
    #show 777chan_flustered
    b777 "W-what?"
    if not father_is_airbus:
        m "Guess my little sister's demeanor is rubbing off on me..."
    else:
        m "Guess I've been watching too many gameshows. Sorry."


label walkToGym:
    scene bg inside_gym

    m "Looks like we made it on time!"
    b777 "Y-yeah!"
    "She looks around looking for a seat to take."

    if affinity_777 >= 1:
        menu:
            "..."
            "There are two seats over there! Let's grab them!":
                $ confidence += 1
                $ affinity_777 += .25
                jump oc_777_sitwith

            "I'll see you later, I should sit with my classmates. ":
                $ affinity_777 -= .25
                jump oc_777_bye
    elif affinity_777 == 0:
        m "Hey, I see two seats over there, we should get them!"
        #show 777chan_surprised
        b777 "Y-yeah, but I should sit with my class..."
        menu:
            "..."
            "Don't worry about that, they'll see you later in class. Besides I enjoy your company!":
                #show 777chan_embarassed
                b777 "Y-you do?"
                m "You're the first person I meet at my new school and you're super friendly, of course I do!"
                #show 777chan_poke_finger_together
                $ confidence +=.5
                $ affinity_777 += .25
                jump oc_777_sitwith
            "You're right, I'll see you around then.":
                $ affinity_777 -= .25
                jump oc_777_bye

    else:
        m "I see a seat over there, I'll see you later, yeah 777?"
        #show 777chan_finger_poke_together
        b777 "Y-yeah...later..."
        #hide 777chan_finger_poke_together
        "You find a seat in the back row; there are not many open ones left."
        jump openingCeremony

label oc_777_sitwith:
    #show 777chan_flustered
    b777 "O-okay, that works, let's grab them before anyone else does."
    hide 777chan_flustered with moveoutleft
    "The two of you hurry off to take your seats before the ceremony starts."
    jump openingCeremony

label oc_777_bye:
    #show 777chan_disappointed
    "777 makes it obvious that she wanted to sit with you..."
    b777 "O-okay...I'll go find my friends..."
    hide 777chan with moveoutleft
    #hide 777chan_disappointed with moveoutleft
    "She hurries off."
    "Maybe you should have invited her to sit with you...there are two open seats next to each other over there..."
    m "She's an upperclassmen, she's obviously got more important things to do than to sit with the transfer student..."
    jump openingCeremony



label openingCeremony:
    scene bg gym_stage

    nameunknown "Ahem. Quiet please, quiet. "
    "The clamour of the gym quiets down to a whisper. "

    v "DEVNOTE: The StuCo president makes a speech after the two team chairmen make their opening speeches, trying to sell their teams to the students. "

label afterCeremony:
    v "DEVNOTE: Depending on your affinity with 777 you either walk to class with her or your sister. A330 is not too happy about having to be seen with you."

label d1_classroom_morning:
    v "DEVNOTE: You sit in the row closest to the window, second from the back obviously. A340-sensei is introduced and wow she's a whore. Like she seriously needs to just get laid, but you're not the one to do that!"
    v "DEVNOTE: This is where you make your team choice. "
    v "DEVNOTE: You'll be introduced as a transfer student with A350. You learn about what she likes. "
    v "DEVNOTE: Your seat neighbor will be A320 or 737 depending on your team choice. "
    v "DEVNOTE: If you pick Boeing, 737 will drop her pencil during class notes time and you'll get it for her, sparking a small conversation where you can gain 1 affinity if done right. Not like she wants you to help her or anything...b-baka..."
    v "DEVNOTE: If you pick Airbus, A320 will end up helping you with your math classwork, as you end up getting confused. You can gain 1 affinity with her depending on your answer to the quiz question, after she helps you. "

label d1_lunchtime:
    v "DEVNOTE: You spend lunchtime alone on day 1, and depending on affinity, may notice that 737 does not have a lunch. Since she was so abrasive earlier, you don't question her motives, but make a mental note of it. "
    v "DEVNOTE: 737 is actually quite poor and sometimes cannot afford a lunch, due to restrictions that have left her family quite broke. (737 MAX fiasco)"

label d1_classrom_afternoon:
    v "DEVNOTE: You have a pop quiz on Flight Dynamics and are called to answer a question a la Persona style. Gain .25 affinity if you get the question right, lose .5 affinity if you get it wrong..."

label d1_classroom_afterschool:
    v "DEVNOTE: You catch up with 777 on her way out of the school building (if your affinity is 1) and tell her about what team you chose. +1 affinity if you chose Boeing. +0 if you chose Airbus. You say goodbye to 777 and wish her a good night."
label d1_walkhome:
    v "DEVNOTE: You walk home with your sister (if Boeing) and your childhood friend A320. You make smalltalk about the day, and +1 affinity with A320 if you picked Airbus team. +1 with sister if you picked Boeing. No minuses. "
    v "DEVNOTE: A320 teases you about if there are any hot girls in your class. Random event here to see if you have the confidence to call her hot to her face. Very low chance, but +1 affinity with A320 if you pull it off."
    v "DEVNOTE: If you fail, you mention 777, and she teases you about being into older women (and you lose .25 affinity with A320). It's not like that...yet. "
    v "DEVNOTE: BRANCH POINT: Do you study, go to the arcade, or play MMO games at home all night? "
label d1_study:
    v "DEVNOTE: You decide to study Flight Dynamics with A320. She quizzes you three times, allowing you to build up your brains score, (total of 1 point if you get all right) and gain .25 affinity with A320 for being a responsible student. "
    v "DEVNOTE: You finish studying early and both decide that you can either go to the arcade, or play Land of Last Fantasy III together. "
    v "You can also decline this and go to bed like a limp dick. "
    menu:
        "What should A320 and I do now that we're done studying?"
        "We should go to the arcade!":
            jump d1_arcade
        "We should play Land of Last Fantasy III!":
            jump d1_mmo
        "I should be getting some sleep...":
            jump d1_morgana


label d1_arcade:
    v "DEVNOTE: You meet up with A320 and both get beaten at a fighting game by a familiar face. A350, the girl that was introduced with you this morning to your class. You three go play a crane game and you win a stuffed cat. You are given a choice of who to give it to."
    v "DEVNOTE: +2 affinity with A320 if you give it to her (she loves cats), +1 affinity with A350 if you give it to her. +1 affinity with 757/A330 if you decide to give it to your sister. You also get the option to give it to 777 if your affinity with her is above 1.5 "
    jump gameEnd
label d1_mmo:
    v "DEVNOTE: You decide to play Land of Last Fantasy III with A320, when you receive a whisper from a mysterious character calling themselves only Zoomy McFrickHands (this is CRJ-chan)"
    v "DEVNOTE: You get the option to run rifts with A320 (+.25 affinity) or abandon her to play with Zoomy McFrickHands (she's better geared, +1 affinity with CRJ, -.5 with A320)  "
    v "DEVNOTE: If CRJ, you play late into the night with her, killing evil spirits and demons. If A320, she scolds you into going to bed because of school. "
    jump gameEnd
label d1_morgana:
    v "You walk A320 back to her house and bid her goodnight."
    v "DEVNOTE: You limp dick, go to the shame bed."
    jump gameEnd
label gameEnd:
    # This ends the game.
    v "This is the end of this pre-alpha test of Day 1"
    return
