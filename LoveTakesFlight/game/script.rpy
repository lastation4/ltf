#########################################################################################################################
#   Day 1 - Starting your new life at school                                                                            #
#########################################################################################################################

# Begin Day 1 Flags

define selected_boeing = False
define selected_airbus = False
define d1_played_mmo_with_zoomy = False
define with_777 = False

# End Day 1 Flags

label d1_gameStart:

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

label d1_driveToSchool:
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
        show a330 at left
    else:
        #show 757_phone_talk
        b757 "Obviously Boeing! You don't want to upset Dad after all the hard work he put in landing this job!"
        m "You're right, that's probably a good idea. Wouldn't want to make dad mad by picking Airbus..."
        #show 757_phone_laugh
        "You and 757 both laugh."
        m "Yeah imagine if I picked Airbus, what would you do Dad?"
        show 757 at left
    show father at right
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

label d1_arriveAtSchool:
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
            jump d1_b777_smalltalk
        "So 777, I see you're a third year, mind asking what team are you on?":
            jump d1_b777_classrank
        "...":
            jump d1_b777_noresponse

label d1_b777_classrank:
    $ affinity_777 -= 1

    #show 777_disappointed
    b777 "Oh...um...Boeing..."

    "She's a Boeing girl, I should have known that!"
    "Now I look like an idiot!"

    jump d1_walkToGym

label d1_b777_smalltalk:
    #no affinity gain for smalltalk
    #show 777_finger_poke_together
    b777 "..."
    jump d1_walkToGym

label d1_b777_noresponse:
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

label d1_walkToGym:
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
                jump d1_oc_777_sitwith

            "I'll see you later, I should sit with my classmates. ":
                $ affinity_777 -= .25
                jump d1_oc_777_bye
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
                jump d1_oc_777_sitwith
            "You're right, I'll see you around then.":
                $ affinity_777 -= .25
                jump d1_oc_777_bye

    else:
        m "I see a seat over there, I'll see you later, yeah 777?"
        #show 777_finger_poke_together
        b777 "Y-yeah...later..."
        #hide 777_finger_poke_together
        "You find a seat in the back row; there are not many open ones left."
        jump openingCeremony

label d1_oc_777_sitwith:
    #show 777_flustered
    $ with_777 = True
    b777 "O-okay, that works, let's grab them before anyone else does."
    hide 777_flustered with moveoutleft
    "The two of you hurry off to take your seats before the ceremony starts."
    jump d1_openingCeremony

label d1_oc_777_bye:
    $ with_777 = False
    #show 777_disappointed
    "777 makes it obvious that she wanted to sit with you..."
    b777 "O-okay...I'll go find my friends..."
    hide 777 with moveoutleft
    #hide 777_disappointed with moveoutleft
    "She hurries off."
    "Maybe you should have invited her to sit with you...there are two open seats next to each other over there..."
    m "She's an upperclassmen, she's obviously got more important things to do than to sit with the transfer student..."
    jump d1_openingCeremony

label d1_openingCeremony:
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

label d1_afterCeremony:
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
        "She spots you. She doesn't look too happy to see you..."
        a330 "..."
        a330 "Are you trying to humiliate me? It's hard enough to make friends without you repelling other people away."
        m "Sorry, I figured it would be best to stick together."
        a330 "Of course you would. Just try not to draw too much attention to yourself."
        a330 "It seems you have chased one person away already, as it is. I probably can't talk to that 777 girl anymore thanks to you."
        "..."
        a330 "Just get to your class already..."
        "She practically runs away from you."
        hide a330 with moveoutleft
        "You find your way to the classroom building, by following the crowd."

    else:
        "You see your sister, 757, in the crowd. Being the only familiar face you can see, you make your way towards her."
        show 757
        "She gives you a friendly wave,"
        b757 "Wasn't that a great speech by dad? Oh! How are you liking school so far?"
        m "Well, I-"
        "Before you can even get a word out, your sister's attention is stolen by another group of girls"
        b757 "Oh! Gotta go! Byyyeee! Let's talk more later!"
        hide 757 with moveoutright
        "She darts off, to join her new friends."
        "..."
        "You find your way to the classroom building, by following the crowd."

label d1_classroom_morning:
    scene outside_classroom
    "I finally find my classroom. The desks are still for the most part empty."
    "There are desks over by the window. I decide to take the one that is second to back."
    "Maybe I can get a good view of the training port from here? I might even see one of the hikokiko in flight..."
    "The other students trickle in one by one. The boys in class all crowd towards the front seats."
    "Strange."
    "Back in my old school, students would try to sit in the back to avoid the teacher's attention."
    "Perhaps, that's the difference between an average and a prestigious school."
    "The students quiet down as the sensei walks in..."
    show a340
    a340 "Hello students!~ Welcome to DC Circuitry 101"
    a340 "Today, we'll be learning a bit about Ohms law. I'll be drafting some schematics here on the board and we'll work..."
    # If there is a face where it can be derived that she might be having ulterior thoughts, it ought to be here.
    a340 "together... on calculating the current"
    a340 "I'll also be your homeroom teacher, so we'll be seeing A LOT of each other. "
    "She gives an over-exaggerated wink."
    a340 "Before we get to that, of course, we'll need to introduce our new transfer students. Please stand up if you transferred this year."
    "Guess I should stand up..."
    "Both another girl and I stand up"
    a340 "Okay, okay, please introduce yourselves and, more importantly, pick your team."
    a340 "I'm not biased, but if you want to see more of dear ol' A340, then pick Airbus <3!"
    "She makes a heart motion with her hands like you'd expect from one of the girls, not a teacher..."

    "..."
    # the most important decision of the game
label d1_the_selection:
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

    if selected_airbus and father_is_airbus:
        "I decide to go with my family team, Airbus."
    elif selected_airbus and not father_is_airbus:
        "I've decided to go with the technologically advanced Airbus over my family team of Boeing. Wonder what Dad'll think of that..."
    elif selected_boeing and not father_is_airbus:
        "I decide to go with my family team, Boeing. "
    elif selected_boeing and father_is_airbus:
        "I've decided to go with the tenacious Boeing over my family team of Airbus. Wonder what Dad'll think of that..."
    else:
        v "How the fuck did you get here?"
        v "he does not foksmash my code"
        $ renpy.quit()
    if selected_boeing:
        a340 "Boeing, is it? Such a shame, but I suppose we have chase our own ambitions."
    else:
        a340 "Another one for Airbus, is it? How exciting!"

    a340 "Well, why don't you both tell us a little bit more about yourselves?"

    show a340 at right
    show a350 at left
    a350 "Hullo. I'm A350, but some of my friends call me Trash Panda."
    a350 "I, um, like anime, manga, anime music and I like to collect figurines."
    a350 "..."
    a350 "From anime."
    a350 "... That's all"
    hide a350
    show a340 at center
    a340 "...Rivoting."
    a340 "Alright, How about you tell us a little bit about yourself?"

    "..."

    if father_is_airbus:
        m "Well my father is the chair of the Airbus team..."
    else:
        m "Well my father is the chair of the Boeing team..."

    m "I like anime and manga as well, so I guess we share something in common A350. I hope we get along."

    show a350 at left

    a350 "!!!"

    a350 "Cool. Another degenerate like me!"

    a340 "Take your seats everyone."

    hide a340
    hide a350

    "We take our seats and A340-sensei begans teaching the class about currents."

    "She does a few demonstrations on the board and then gives us all a problem to work on"


    if selected_airbus:
        "You hear the clicking of a fallen pencil. You look down to your right and see it. Instinctively, you lean over to pick it up."
        nameunknown "Hey!"
        "You look up and see the angry face of the girl sitting next to you"

        show 737 center

        nameunknown "That's mine!"

        menu:
            "I'm sorry. I was just trying to pick it up for you":
                nameunknown "Ah!"
                nameunknown "Well, I didn't ask you to!"
                nameunknown "B-but thanks, anyways, I guess"
                $ affinity_737 += 1
            "Mine now.":
                nameunknown "Ex-CUSE me?"
                nameunknown "Where do you get off stealing other people's property?"
                m "I'm just kidding! Why would anyone want to steal a pencil? They're like fifty cents! Here you go."
                nameunknown "R-right. Of course, that would be silly."
            "...":
                nameunknown "What, do I got something on my face? Give that back already!"
                "She snatches the pencil from your hand"
                nameunknown "The nerve of some people!"
                $ affinity_737 -= .25
                hide 737
        "We proceed with our assignment with the awkward silence between the two of us."
        "I sorta want to try to strike up conversation with her... Considering she sits next to me, it would suck for class to be tense like this everyday"
        m "So, my name is ~~~... What is yours?"
        show 737 at right
        "The girl looks up from her desk, seemingly unsure if I was speaking with her"
        nameunknown "I am 737, I suppose. What's it to you?"
        m "Not anything. I just figured that, since we are sitting near each other, it's worth at least knowing each others names."
        "She goes back to looking at her assignment."
        737 "I guess that's true. But, that doesn't mean we are friends or anything!"
        "... That's an odd thing to clarify, but I'll take it."
        hide 737

    else:
        m "I..."
        m "... do not get this!"
        "In spite of the fact she had just demonstrated all of this, my attempts to replicate what was on the board falls short of getting an answer."
        "I look up to see if I could get some help... It seems that A340-sensei is currently occupied with helping some of the students in the front"
        "It makes me feel better seeing that a lot of them were not getting it either. But, I don't want to fall behind any of them!"
        "I try to raise my hand up to try to get her attention"
        nameunknown "You having trouble?"
        show a320
        nameunknown "It's not all that hard. I can help you if you are struggling"
        "Wait a minute..."
        m "A320?"
        #a320 smiles
        a320 "...Took you long enough to notice me."
        m "I'm sorry, I was just really focused on class."
        "a320 looks towards the sensei as she helps someone with their coursework."
        a320 "...Sure you were."
        m "Your offer to help still stands, right?"
        a320 "I don't know, you've completely forgotten about me, in spite of us being friends since grade school."
        a320 "... but, I guess I'll be nice this time."

        #Oh, we might actually need practice problems for ohms law.
        #This is basic math; We could probably have the protag be cofused about where things fall in the equation and a320 break it down to the mathmatical stuff

        "..."

        a320 "So it's pretty simple, draw a triangle with a \"T\" inside of it. Write V in the top slot, I in the left slot, and R in the right slot."
        m "I think I understand, let's see..."

        "You do what A320 suggests..."

        a320 "So if you have V, the formula is I*R. If you have I, the formula is V/R, and finally...."
        "A320 looks at you expectantally..."

        menu:
            "A320 looks at you expectantally..."
            "If I've got R, I/V?":
                a320 "Nope, division is not communicative. You've got it backwards. It's V/I."
                $ affinity_a320 -= .25
                $ intel -= .25
            "If I've got R, V*I?":
                a320 "Nope, you only multiply I and R since they are next to each other in the triangle. It's V/I."
                $ affinity_a320 -= .25
                $ intel -= .25
            "If I've got R, V/I?":
                a320 "See, you're getting the hang of it now."
                $ affinity_a320 += .25
                $ intel += .25
        m "Thanks, A320! I think I understand now"
        #Smug look for a320?
        a320 "You'd better! I'm not just here to look pretty, now!"

        if confidence >= 1:
            m "I mean, you are quite pretty..."
            # show a320_blush
            a320 "A...anyway! We need to move on to the next formula!"
            $ affinity_a320 += 1

    "Class goes on without any further events."
    "The rest of the day, the students spend doing practice problems with sensei periodically helping the ones struggling."

    if selected_boeing:
        jump d1_lunchtime
    else:
        jump d1_classroom_afternoon

label d1_lunchtime:
    "After class, you find a spot in the cafeteria."
    "Everyone else is clustered among their own friends. Naturally, being the fresh transfer student leaves you to eat alone."
    "You see 737 sitting by herself."
    "She isn't eating."
    "Did she forget her food? It's entirely possible she's the sort to not bother with lunch."
    "You start eating your food."
    "She seems to be staring at other people's trays."

    "..."

    "You notice her eyes wander over to you."

    menu:
        "Go sit with 737.":
            "You decide to go sit with 737."
        "Eat alone.":
            "You decide it is better that you don't bother 737 anymore for the day. "

    v "DEVNOTE: You spend lunchtime alone on day 1, and depending on affinity, may notice that 737 does not have a lunch. Since she was so abrasive earlier, you don't question her motives, but make a mental note of it. "
    v "DEVNOTE: 737 is actually quite poor and sometimes cannot afford a lunch, due to restrictions that have left her family quite broke. (737 MAX fiasco) [august edit: maybe if affinity is high enough shell talk briefly about it; only to then
    shut down; or not want to talk about it any more. It could be timed out nicely with lunch bell ringing, and her quickly saying 'i have to go.. sorry...' if you develope more with 737 later on, you can get all of this story at a later date?]"
label d1_classroom_afternoon:
    v "DEVNOTE: You have a pop quiz on Flight Dynamics and are called to answer a question a la Persona style. Gain .25 affinity if you get the question right, lose .5 affinity if you get it wrong..."

label d1_classroom_afterschool:
    if affinity_777 >= 1:
        "As I walk out of class, I see 777 far ahead of me in the hallway."
        "I rush past other students to try to catch up with her"
        m "Triple Seven! Triple Seven!"
        show 777 at center
        777 "H-huh? Who is..."
        777 "!"
        m "It's me, ~~~!"
        777 "Ah, I remember you from this morning! How was your first day?"
        m "It was great!"
        "It was, at best, okay. But, upon seeing 777 again, I felt like it was different at that moment"
        777 "T-that's great!"

        if selected_boeing:
            m "I picked Boeing... The same team as you!"
            777 "!"
            777 "That's exciting!"
            $ affinity_777 += 1
        else:
            m "I'm part of Airbus!"
            777 "R-really! That's great!"
        777 "Are you going to become a hikokiko or an engineer?"
        m "I'm going to be an engineer! I, ah, don't quite qualify to fly myself."
        777 "So, I won't be seeing you in the air..."

        if selected_boeing:
            777 "But, we might be working together later! What's a Hikokiko without her engineer?"
        else:
            777 "Still, we can be friends, even if we are on opposing teams"

        m "That's true! Well, I'm sure my sister is waiting on me, I best be going. I hope to see you tomorrow!"
        "Triple Seven almost seems to blush at my hopes to see her again. She gives a timid wave."

    else:
        jump d1_walkhome
    v "DEVNOTE: You catch up with 777 on her way out of the school building (if your affinity is 1) and tell her about what team you chose. +1 affinity if you chose Boeing. +0 if you chose Airbus. You say goodbye to 777 and wish her a good night."

label d1_walkhome:
    if father_is_boeing:
        "I find my sister outside of the school talking with her friends."
        "A320 stands among them. They both wave goodbye to their friends and we head off towards home"
        show 757 at right
        show a320 at left
        757 "So, what did you end up picking?"

        if selected_boeing:
            m "I picked Boeing! Just like you and dad!"
            757 "Yippe! I can't wait to tell him!"
            757 "I was a little worried you were going to pick airbus."
            757 "I know he said he would respect you regardless of your decision, but I feel like it would've made him a little sad, you know?"
            a320 "Ha, could you imagine the chairman's kid being in a completely different team?"
            757 "So scandalous~"
            $ affinity_757 += 1
        else:
            a320 "Airbus is what they picked!"
            757 "Woah, really!?"
            a320 "Yep! Announced it in front of the whole class!"
            757 "Wowzers! I didn't actually think you would go for them."
            757 "I know dad will support your decision, regardless of the jokes he makes!"
            a320 "I'd imagine your dad would get some heat from his colleges for your decision, though!"
            757 "Do you think so?"
            a320 "Oh, I'm sure it'll be fine."
            a320 "It's your life, I wouldn't worry too much about that stuff"
    else
        "Crowds of students cluster in various places in front of the school, all possibly squeezing in whatever conversations they can before the teachers usher them away."
        "There's really no need for me to loiter here. I'll make friends in due time"
        "I head out the school's gates when someone puts a hand on my shoulder"
        m "What the-"
        "I turn and see A320."
        a320 "Forgetting someone?"
        m "N-no, of course I wouldn't forget you."
        "I did forget."
        "It's been so long since we lasted walked together that I didn't even consider the fact we could now."
        a320 "Hey, where's your sister?"
        m "Oh, she's probably back at school, talking with some of her friends."
        m "Even then, I don't think she really wants to be seen with me."
        a320 "Are you serious? What, she think she's too good for you?"
        a320 "Psh, I remember back when she used to wet the bed."
        a320 "Whatever, she can do whatever she wants, I guess, it's not like we want her around or anything."
        m "Haha, the way you said that makes it sound like you are tsun for her or something."
        a320 "What does that mean?"
        m "It's a romance cliche in anime where... well... uh... nevermind. I guess I might just watch too much tv"
        # A320 gives a mischivious grin
        a320 "Oh, romance? I never took you to be the sort to be into that stuff."
        "She puts her arm up to her head and speaks in a facetious tone"
        a320 "Little ~~~, is all grown up! I'm guessing this means you got your eye on some hotties in your class, huh?"
        "She nudges me"

        if renpy.random.randint(1,20) == 20:
            m "Yeah. You."
            # a320 blushes
            a320 "W-what?"
            "I laugh at her"
            a320 "Y-you idiot! Don't tease me that way!"
            m "Haha, sorry, but it was you who started it!"
            $ affinity_320 += 1
        else:
            m "Well, I did meet this girl..."
            # a320's face goes neutral again
            a320 "Oh. Did you get her name?"
            m "Triple Seven"
            a320 "Oh! I know her!"
            a320 "What, are you into older women now?"
            m "..."
            a320 "I'm just teasing!"
            $ affinity_320 -= 25
    a320 "Oh, by the way..."
    a320 "Do you got any plans for tonight?"

    menu:
        "I've got to study tonight. I could really use your help.":
            a320 "Oh, is that so?~"
            a320 "Well, you were getting pretty behind in class. If you want to pass, I think we should not waste any time and get to it."
            if father_is_boeing:
                "A320 grabs me by the hand and we both begin to run. 757 sees what is going on and rushes to keep up."
                757 "Hey, wait up, guys! We're not that far off from the house, there's no need to ruuunnnn-!"
            else:
                "A320 grabs me by the hand and we both run the rest of the way home."
            jump d1_study
        "I was thinking of going to the arcade. Care to join me?":
            a320 "Yeah! Let's meet up in a little bit! I got a few things I'd like to pick up! See you, then!"
            jump d1_arcade
        "I was going to play Land of the Last Fantasy III. How about we meet up online?":
            a320 "Sounds like a plan to me. See you online!"
            jump d1_mmo


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
        "I should be getting some sleep...its getting late. School was a lot today.":
            jump d1_morgana

label d1_arcade:
    "After I stop by my house to drop my school stuff off, I meet up with A320 at the arcade"
    "There are so many games to choose from. As we walk around, A320 latches onto a machine"
    a320 "Let's do this one!"
    "We both share a machine and take turns against an opponent on the other side of the machine."
    "Neither of us win. This guy is really good!"
    "As A320 gets cornered and has her health chipped away, I peek around the machine to see who our opponent is."
    show a350
    "Hey, it's-"
    "She glances at me for a moment and suddenly her face is struck with recognition and she tears her eyes away from the game."
    a350 "Oh hey, it's you. I didn't expect to see people from the school here"
    "A320 notices that her opponent was no longer fighting and peeks over as well"
    A320 "Do you know her?"
    m "A320, this is our classmate, Trash Panda"
    a320 "Right, the other transfer student. Sorry I didn't recognize you from before."
    a350 "It's okay. I generally try to keep a low profile. Can't have people interrupting my gaming sessions to talk about the weather."
    a320 "Speaking of which, shall we all resume our gaming?"
    "Trash Panda joins us on our outing. We all play the 'Ninja Frogs' game together and do a few songs on 'Dance Heros'"
    "As we wind down, I use up the last of my tokens on a claw machine."
    "On my very last token, I get ahold of a stuffed cat toy"
    "The claw wobbles clumsily"
    "The cat slips."
    "... but it narrowly makes out into the drop box"
    "The girls both take notice of this"
    a320 "I can't believe you actually pulled that off!"
    a350 "Nice. What are you gonna do with it?"

    menu:
        "What will I do with it?"
        "Give it to A320":
            a320 "What!? Really?"
            m "Well, you love cats, don't you?"
            a320 "You know it! I think I'll call her Masha."
            m "Masha?"
            a320 "What? Is there a problem with Masha?"
            m "N-no! It's a good name!"
            a320 "Damn right, it is..."
            a320 "...Thanks again."
        "Give it to Trash Panda":
            a350 "For me...?"
            a320 "What are you going to name them?"
            a350 "..."
            a350 "Tama"
            m "Tama?"
            a350 "Yeah. Tama. Like the train cat."
            "Trash Panda cradles the cat in her arms"
            a350 "Thanks."
        "Save for sister":
            a320 "Aw, aren't you a thoughtful brother?"
            m "I guess? I just figured it might be her kind of thing."
            if father_is_airbus:
                a320 "Would she really appreciate the gesture, though...?"
                m "I hope so."
                a350 "Not a fan of plushes?"
                m "Not really a fan of me. I don't know why, either."
                m "It seems ever since she started High School, she's been really distant and, honestly, cruel."
                a320 "It's not just you. She's been about the same to me, to be honest."
                a350 "Wow, um, I'm sorry. Her loss, I guess?"
            else
                a320 "It would suit her, I think."
                m "I hope she likes it"
                a320 "If she doesn't, I can always take it off her hands"
        if affinity_777 > 1.5:
            "Give it to 777.":
                a320 "Triple Seven? Didn't you two just meet?"
                m "Yeah, but, she seems pretty cool. I figured it might be something she would like."
                a320 "Haha. Or, perhaps, there might be more to it...?"
                a350 "...?"

    "Trash Panda glances up to the clock."
    a350 "Oh, the time is getting late. I best be getting home before my mom decides to unplug my 'computer' again."
    a350 "She might realize this time that she's only been taking my monitor, but I don't want to give her too many chances to figure that out."
    a320 "Well, we best be heading on home ourselves."
    "I walk A320 home. I head off to sleep as soon as I get back to my room."
    "Today has been a good one."


    v "DEVNOTE: +2 affinity with A320 if you give it to her (she loves cats), +1 affinity with A350 if you give it to her. +1 affinity with 757/A330 if you decide to give it to your sister. You also get the option to give it to 777 if your affinity with her is above 1.5 "
    jump gameEnd

label d1_mmo:
    "After dinner, I boot up my desktop and load up 'Land of the Last Fantasy'."
    "I grind at a nearby zone while I wait for A320"
    "*Bling!*"
    "... What's this? Someone whispered me on the game. I don't see anyone around. Who is this?"
    "...'Zoomy McFrickHands'"
    "'HEY. YOU ALSO DOING THE MAGUS QUEST FOR THE SLIME DROPS? JOIN MY PARTY?'"
    "I'm not doing this quest, but I could go fetch it. It could be a good way to kill time until A320 logs in."
    "I respond:"
    "'SURE. SEND INVITE. WHERE YOU AT?'"
    "'SAME AREA AS YOU. DON'T SEE ME?'"
    "Sure enough, they walk over the hill and-"
    "Holy shit! They are fully decked out! This person must either be on the game all day or knows some people!"
    "'... CAN SHARE THE QUEST IF YOU DON'T HAVE IT.'"
    "'YES PLS'"
    "Right as the party notification pops up on my screen, I get a notification that A320 is online."

    menu:
        "Uh-oh. I just agreed to join this person's party. What should I do?"
        "Play with A320.":
            jump d1_mmo_a320
        "Play with Zoomy McFrickHands":
            jump d1_mmo_zoomy


label d1_mmo_zoomy:
    "I accept the invite"
    "A320 pings me 'HEY, SO, WHAT ARE WE DOING TONIGHT? I GOT A FEW QUESTS'"
    "I respond:"
    "'ACTUALLY, I'M ALREADY PART OF A GROUP. WE CAN STILL CHAT, THOUGH'"
    "It takes her a little bit to respond."
    "'OK. GOT MY OWN QUESTS TO COMPLETE'"
    "Zoomy and I complete several quests and join a few of their friends to do a raid on Whalebone Castle."
    "We stay up to about 3 in the morning, killing off evil spirits and demons. "
    $ affinity_crj += 1
    $ affinity_a320 -= 1

label d1_mmo_a320:
    "'ACTUALLY', I start off with"
    "'MY FRIEND JUST CAME ONLINE. SORRY ABOUT THAT'"
    "I decline the invite"
    "Zoomy responds, 'NO WORRIES. HAVE A GOOD ONE.'"
    "A320 and do a few quests, but overall goof off in a town and talk about school and an anime we both watch."
    "10:00 rolls around and A320 calls it a night."
    "I was going to continue playing, but A320 chastizes me for not minding my health."
    "I exit the game and doze off to sleep."
    $ affinity_a320 += .25

label d1_morgana:
    v "You walk A320 back to her house and bid her goodnight."
    v "DEVNOTE: You limp dick, go to the shame bed."
    jump gameEnd


