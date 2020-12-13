# The script of the game goes in this file.

# disable the back button, cause you have to save scum
define config.rollback_enabled = False

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

#flags go here
define with_777 = False
define prealpha = False
define selected_boeing = False
define selected_airbus = False

# The game starts here.

label start:

    scene bg prealpha

    if prealpha == True:
        jump alphatest
    else:
        jump gameStart

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

label gameStart:

    scene bg sky

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
        a330 "Well, maybe think next time! We're going to be late if we don't get going soon!"
        "You nod, and go downstairs with her and meet up with your father."
        hide a330 with moveoutleft
        #hide a330_scolding with moveoutleft
    else:
        show 757
        nameunknown "Waah! Watch out! We're going to crash! Nyeaowwwww!"
        hide 757 with moveoutleft
        "Your sister, 757, quickly darts to the left of you, and hops down the stairs."
        b757 "HEY! HURRY UP! YOU DON'T WANT TO BE LATE! DAD'S WAITING!"
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
        a330 "It doesn't really matter to me, but shouldn't you just go with the family team? Should be an easy choice."
        m "You're right, that's probably a good idea. Wouldn't want to make dad mad by picking Boeing..."
        "You laugh dryly to yourself, and try to change the subject."
        m "Yeah imagine if I picked Boeing, what would you do Dad?"
    else:
        #show 757_phone_talk
        b757 "Obviously Boeing! You don't want to upset Dad after all the hard work he put in landing this job!"
        m "You're right, that's probably a good idea. Wouldn't want to make dad mad by picking Airbus..."
        #show 757_phone_laugh
        "You and 757 both laugh."
        m "Yeah imagine if I picked Airbus, what would you do Dad?"
    show father
    father "I'd disown you."
    m "What...?"
    if father_is_airbus:
        #show a330_annoyed
        a330 "Dad, really? I mean...that's kind of awful to say."
    else:
        #show 757_shocked
        b757 "DAD! WHY WOULD YOU SAY SUCH A HORRIBLE THING!"
    "You gulp audibly."
    m "...you're serious?"
    show father
    if not father_is_airbus:
        father "Of course not. It's your choice, and I respect the competition and technological innovation that Airbus brings to the market. Without their advanced avionics, Boeing wouldn't have upgraded theirs. Competition is healthy."
        #show 757_scolding
        b757 "Dad! Don't play around like that!"
        #show 757_smile
    else:
        father "Of course not. It's your choice, and I respect the competition and legacy that Boeing has. They do have a way with making their planes look nice. Competition is healthy."
        #show a330_stoic
        "A330 continues to stare out the car window..."

    m "Okay, that's a relief. Thanks for supporting my decision. "
    "You wonder to yourself what that decision is going to be...Boeing or Airbus..."
    "..."
    father "We're about there, kiddos. "

    if father_is_airbus:
        #show a330_sarcasm
        a330 "Great, how exciting."
        #hide a330_sarcasm
        show father
        father "You could at least show some enthusiasm. Does anything excite you anymore?"
        hide father
        #show a330_angry
        a330 "Hmph."
        #hide a330_angry
        #show a330_cellphone_music
        "Your sister does what she always does when dad's being an asshole; pops in her earbuds and blasts music."
        "..."
        "You can cut the tension in the car with a knife."
        show father
        father "We're here. See you both later. I've got a job to do."
        "You both get out of the car and go your separate ways."
    else:
        #show 757_excited
        b757 "YAY SCHOOL! I CAN'T WAIT FOR FLYING CLASS!"
        b757 "Dad, I'm picking Boeing!"
        #hide 757_excited
        show father
        father "Good! You remember the mantra?"
        hide father
        b757 "Of course!"
        #show 757_yell
        b757 "If it isn't Boeing, I'm not going!"
        "The three of you laugh."
        show father
        father "We're here. Now both of you, remember to pick Boeing! Make me proud!"
        hide father
        #show 757_excited
        two "Alright!"

    scene black with dissolve

label arriveAtSchool:
    scene bg car

    "A bell chimes in the distance...You'd better hurry off to the opening ceremony!"

    m "See ya Dad! Gotta go!"
    hide father
    scene bg school_outside_main_campus

    "You get out of the car and rush off to the school gym."
    "...at least you would if you knew where it was..."
    "..."
    "You decide to ask someone where the gym is."
    "...you look around trying to get someone's attention..."

    show 777

    "You spot a third year that looks like she's either lost, or confused..."

    m "Excuse me, do you know where the gym is? I don't want to be late for the ceremony."

    nameunknown "Ah! U-u-um...were y-you talking to...m-me?"

    m "Yeah, are you alright?"

    #show 777_point_right

    nameunknown "Y-yeah...I guess. The gym is that large building over there..."

    #show 777_shy

    "She points to a large building that has a banner on it, reading \"Welcome New Cadets\""

    m "How could I miss that. Wow. You probably think I'm an idiot."

    nameunknown "W-what! No! I don't think that at all!"

    m "Well since we're headed the same way, how about we go together?"

    #show 777_blush

    nameunknown "A...ah! Yes, that's a good idea, wouldn't want either of us getting lost..."

    #show 777

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

    #show 777_disappointed
    b777 "Oh...um...Boeing..."

    "She's a Boeing girl, I should have known that!"
    "Now I look like an idiot!"

    jump walkToGym

label b777_smalltalk:
    #no affinity gain for smalltalk
    #show 777_finger_poke_together
    b777 "..."
    jump walkToGym

label b777_noresponse:
    $ affinity_777 += 1
    #show 777_finger_poke_together
    b777 "Y-you're a transfer student, right?"
    m "Yeah, how'd you know? Is it that obvious?"
    #show 777_glasses_push
    b777 "Y-yeah, I mean, you have two bars on your uniform, so that means you're...second year."
    b777 "That must mean transfer! R-right?"
    m "Ding ding ding, you're right!"
    #show 777_flustered
    b777 "W-what?"
    if not father_is_airbus:
        m "Guess my little sister's demeanor is rubbing off on me..."
    else:
        m "Guess I've been watching too many gameshows. Sorry."

label walkToGym:
    scene bg gym_outside

    m "Looks like we made it on time!"
    b777 "Y-yeah!"

    scene bg gym
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
        #show 777_surprised
        b777 "Y-yeah, but I should sit with my class..."
        menu:
            "..."
            "Don't worry about that, they'll see you later in class. Besides I enjoy your company!":
                #show 777_embarassed
                b777 "Y-you do?"
                m "You're the first person I meet at my new school and you're super friendly, of course I do!"
                #show 777_poke_finger_together
                $ confidence +=.5
                $ affinity_777 += .25
                jump oc_777_sitwith
            "You're right, I'll see you around then.":
                $ affinity_777 -= .25
                jump oc_777_bye

    else:
        m "I see a seat over there, I'll see you later, yeah 777?"
        #show 777_finger_poke_together
        b777 "Y-yeah...later..."
        #hide 777_finger_poke_together
        "You find a seat in the back row; there are not many open ones left."
        jump openingCeremony

label oc_777_sitwith:
    #show 777_flustered
    $ with_777 = True
    b777 "O-okay, that works, let's grab them before anyone else does."
    hide 777_flustered with moveoutleft
    "The two of you hurry off to take your seats before the ceremony starts."
    jump openingCeremony

label oc_777_bye:
    $ with_777 = False
    #show 777_disappointed
    "777 makes it obvious that she wanted to sit with you..."
    b777 "O-okay...I'll go find my friends..."
    hide 777 with moveoutleft
    #hide 777_disappointed with moveoutleft
    "She hurries off."
    "Maybe you should have invited her to sit with you...there are two open seats next to each other over there..."
    m "She's an upperclassmen, she's obviously got more important things to do than to sit with the transfer student..."
    jump openingCeremony

label openingCeremony:
    scene bg gym_stage

    nameunknown "Ahem. Quiet please, quiet. "
    "The clamour of the gym quiets down to a whisper. "

    if father_is_airbus:
        #show boeing_chair
        nameunknown "I am the chairman of the Boeing Racing Team, and it is my pleasure to welcome you to this new year at our academy!"
        boeing_chair "I'd like you all to consider flying or engineering for our team for this year's competition. As you know, we've won the last 4 years straight and would love to have you help us continue that legacy. Our competition may have better technology, but as the record shows..."
        #show boeing_chair_fist
        boeing_chair "Technology doesn't stand a chance against Tenacity!"
        boeing_chair "That's all I have to say on that matter. Now I'll introduce the underdogs, the Airbus Racing Team."
        #hide boeing_chair
        #show father
        father "Ahem, I'm the chair of the the Airbus Racing Team this year, and although I am new, my ideas will lead us to unseating Boeing as the de facto leaders in Planegirl Racing. I'm sure of it!"
        #hide father
        "Small giggles erupt in the audience"
        nameunknown "Nobody can beat Boeing!"
        nameunknown "If it's not Boeing, I'm not going!"
        nameunknown "The underdogs think they have a chance! How cute!"
        #show father_flustered
        father "Quiet! Quiet please, I'm not finished! I'm sure that our newest technologies that we will deploy at Race #1 will ensure a new day rises for Airbus!"
        father "That's all I have, now let me introduce the Student Council President, 747!"
        #hide father_flustered
        show 747
        b747 "Thank you \"esteemed\" Airbus Chairman."
        #show 747_giggle
        "She giggles to herself, and it is picked up on the microphone."
        b747 "Ara, ara. Excuse me. I just found your little speech...cute is all. Thinking you could defeat the great Boeing. It's hilarious."
        b747 "Anyway, if you want power and glory, join Boeing. If you want to strive hard toward nothing, choose Airbus, as they'll do what they do every year: bluster about new technology but not actually deliver at any races."
    else:
        nameunknown "I am the chairman of the Airbus Racing Team, and it is my pleasure to welcome you to this new year at our academy!"
        airbus_chair "I'd like you all to consider flying or engineering for our team for this year's competition. As you know, we've won the last 4 years straight and would love to have you help us continue that legacy. Our competition may be tenacious, but as the record shows..."
        #show airbus_chair_
        airbus_chair "Tenacity doesn't hold a flame to Progress and Technology!"
        airbus_chair "That's all I have to say on that matter. Now I'll introduce the underdogs, the Boeing Racing Team."
        #show father
        father "Ahem, I'm the chair of the the Boeing Racing Team this year, and although I am new, my ideas will lead us to unseating Airbus as the de facto leaders in Planegirl Racing. I'm sure of it!"
        #hide father
        "Small giggles erupt in the audience"
        nameunknown "Nobody can beat Airbus!"
        nameunknown "If it's Boeing, I'm not going!"
        nameunknown "The underdogs think they have a chance! How cute!"
        #show father_flustered
        father "Quiet! Quiet please, I'm not finished! I'm sure that our newest technologies that we will deploy at Race #1 will ensure a new day rises for Boeing! We'll show them that we can do technology too!"
        father "That's all I have, now let me introduce the Student Council President, 747!"
        #hide father_flustered
        show 747
        b747 "Thank you \"esteemed\" Boeing Chairman."
        #show 747_giggle
        "747 giglges to herself..."
        b747 "While I may be a Boeing girl, it's obvious to see the awesome tech that Airbus cranks out every year in the name of the saftey of our sport. They are the true leaders, and don't let Boeing convince you otherwise!"
        b747 "If you want a safer sport, come engineer or fly for Airbus. If you want nosedives and firey crashes, go with Boeing. They're good at that here lately."
        jump d1_challenge_747

label d1_challenge_747:
    menu:
        "You can feel your blood beginning to boil..."
        "We'll show you, you bloated gas-guzzler!":
            $ confidence += .5
            if with_777:
                hide 747
                #show 777_shocked
                show 777
                b777 "..."
                m "I'm not going to let her say those things about my father!"
                if father_is_airbus:
                    b777 "...Airbus-sensei is your father?"
                else:
                    b777 "...Boeing-sensei is your father?"
                m "That's right. And I'm not going to let some bitch talk like that!"
                b777 "...you're not wrong..."
                m "Thanks for your support Triple Seven."
                $ affinity_777 +=.25
                hide 777
        "...":
            $ confidence -= .5
            if with_777:
                b777 "...she sure has a way of really riling up the students..."
                hide 777
    show 747
    b747 "This concludes our ceremony. Please make your way back to your homerooms. Transfer students: you will be making your team selection upon arrival, so please be prepared with your decision. "
    b747 "I'm sure you'll make the right one."
    b747 "If you don't...well then that sucks for you."
    hide 747
    scene black with dissolve

label afterCeremony:
    scene outside_gym
    if with_777:
        show 777
        b777 "..."
        m "H...hey, since I'm new here can you help show me to my classroom? I'm in class...um 2-D."
        b777 "Oh! Of course! All second years are on the second floor of the main school building."
        "Triple Seven thinks for a bit..."
        b777 "L...let me show you where that building is..."
        "You walk with 777 to the school building."
        scene inside_school

        b777 "You just take these stairs to the second floor...I'm in class 3-A...if you want to...h-hang out again..."
        $ affinity_777 += .5
        m "Of course I do. I need to get to class now. I'll definitely see you around, Triple Seven."
        hide 777
        show 777_blush
        "She blushes, but you can see a small smile across her face, as she nods and hurries off to her classroom."
        hide 777_blush with moveoutleft
    elif father_is_airbus:
        show a330
        "You see your sister, A330, in the crowd. Being the only familiar face you can see you make your way towards her."
        "She spots you. She doesn't look too happy to see you"
        a330 "..."
        a330 "Are you trying to humiliate me? It's hard enough to make friends without you repelling other people away"
        m "Sorry, I figured it would be best to stick together."
        a330 "Of course you would. Just try not to draw too much attention to yourself."
        a330 "It seems you have chased one person away already, as it is. I probably can't talk to that 777 girl anymore thanks to you."
        "..."
        a330 "Just get to your class already"
    else:
        "You see your sister, 757, in the crowd. Being the only familiar face you can see, you make your way towards her."
        show 757
        "She gives you a friendly wave"
        b757 "Wasn't that a great speech by dad? Oh! How are you liking school so far?"
        m "Well, I-"
        "Before you can even get a word out, your sister's attention is stolen by another group of girls"
        b757 "Oh! Gotta go! Byyyeee! Let's talk more later!"
        hide 757
        "You find yourself standing alone in the crowded hallway"
    v "DEVNOTE: Depending on your affinity with 777 you either walk to class with her or your sister. A330 is not too happy about having to be seen with you."

label d1_classroom_morning:
    "You finally find your classroom. The desks are still for the most part empty."
    "There are desks over by the window. You take the one that is second to back."
    "Perhaps you would get a good view of the training port from there? You might even see one of the hikokiko in flight..."
    "The other students trickle in one by one. You notice that the boys in class all crowd towards the front seats."
    "Strange."
    "Normally, kids in your old school would try to sit in the back to avoid the teacher's attention."
    "Perhaps, that's the difference between an average and a prestigious school."
    "The students quiet down as the sensei walks in..."
    show a340
    a340 "Hello students!~ Welcome back to DC Circuitry 101"
    a340 "Today, we'll be learning a bit about Ohms law. I'll be drafting some schematics here on the board and we'll work..."
    # If there is a face where it can be derived that she might be having ulterior thoughts, it ought to be here.
    a340 "together... on calculating the current"
    a340 "I'll also be your homeroom teacher, so we'll be seeing A LOT of each other. "
    "She gives an over-exaggerated wink."
    a340 "Before we get to that, of course, we'll need to introduce our new transfer students. Please stand up if you transferred this year."
    "Guess I should stand up..."
    "You stand, and notice another girl stand as well."
    a340 "Okay, okay, please introduce yourselves and, more importantly, pick your team."
    a340 "I'm not biased, but if you want to see more of dear ol' A340, then pick Airbus <3!"
    "She makes a heart motion with her hands like you'd expect from one of the girls, not a teacher..."

    "..."
    # the most important decision of the game
label the_selection:
    menu:
        "...which team will I select?"
        "Boeing":
            menu:
                "Did you want to select Boeing?"
                "Yes":
                    $ selected_boeing = True
                    $ selected_airbus = False
                "No":
                    jump the_selection

        "Airbus":
            menu:
                "Did you want to select Airbus?"
                "Yes":
                    $ selected_boeing = False
                    $ selected_airbus = True
                "No":
                    jump the_selection

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
