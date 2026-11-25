# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lauren")
define a = Character("Addy")
define ad = Character("Adrien")
define e = Character("Ellie")
define g = Character("Grace")
define m = Character("Moriah")
define o = Character("Oli")
define s = Character("Sandy")
define j = Character("Jasper")
define c = Character("Chiron")
define ma = Character("Manuela")

default know_jasper = False
default know_oli = False
default know_grace = False
default know_addy = False

transform fullscreen:
    xysize (config.screen_width, config.screen_height)
    fit "cover"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene front camp at fullscreen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Chiron

    # These display lines of dialogue.

    c "Hello! Welcome to Camp Halfblood."

    c "I'm sure your satyr has told you all about us. I recommend going to the Hermes cabin. Our Hermes head counselor can help you there."

    hide Chiron

    scene Hermes Beds

    m "Uh is there a head counselor here?"

    # Animation here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    a "Ow..."

    m "Hello?"

    a "Hey."

    menu welcome:
        "What to say?"
        "Are you the head counselor?":
            show Addy disheveled
            a "Yeah, sorry. Normally I'm a bit more... up. New camper?"
            menu:
                "What to say?"
                "Yeah? Chiron told me to come up.":
                    show Addy Excited
                    a "Oh okay cool. Well, welcome to Camp Halfblood!"
                "Yeah...":
                    show Addy Excited
                    a "Great! Welcome to Camp Halfblood. Your home for the summer... or... more."
                        
        "Am I in the wrong place?":
            show Addy disheveled
            a "Well if you're looking for Hermes Cabin, you're right."
            menu:
                "What to say?"
                "Oh then yeah... are you the head counselor?":
                    show Addy Excited
                    a "Indeed I am. Welcome to Camp Halfblood!"
                "Yes, sorry, I'm new here.":
                    show Addy Excited
                    a "Oh then welcome! I'm the head counselor for Hermes!"



    a "If Chiron sent you here, I'm probably your guide!"

    a "You're in luck. I'm the best one. Don't tell anyone I said that..."
    
    show Addy Neutral

    a "My name is Addy. A daughter of Hermes. I stay here all year."

    $ know_addy = True

    #Add new person notif

    m "I'm Moriah!"
    menu:
        "What to say?"
        "How do I know what child of a god I am?":
            a "Well, a symbol or some sign from your parent will appear eventually."
            a "The gods used to never claim us, but a kid named Percy Jackson changed all that. You'll probably hear about him."
            a "Well, which parent do you have?"
            m "I live with my mom?"
            a "Then you can limit your choices to the dads."
            a "Mostly.... It's rare but I've seen some with two biological dads. Mostly Apollo."
            a "Do you have any hints for your cabin? Like powers?"
            menu: 
                "What to say?"
                "Not as far as I can tell":
                    a "Then you'll find who later."
                "My like senses and abilities are better than most peoples?":
                    a "That's most gods. Don't worry, he'll claim you eventually."          
            a "I learned mine when I challenged the old head counselor to a race and won."

        "Do I have to stay all year?":
            a "No, it's your choice. Most kids stay for the summer, it really depends on how monsters are attracted to you, or if you actually just want to stay."

        "Where do I stay?":
            a "Until you find your cabin, all unclaimed campers stay in Hermes!"
            a "There's not many, Percy Jackson made a deal with the gods, so most kids get claimed pretty quick."

        "Nothing":
            a "Good to meet you."

    a "If you follow me along here, I can show you the camp."

    scene pavillion front

    show Addy Guide

    a "This is the dining pavillion, each cabin has their table."

    scene big house at fullscreen

    show Addy Guide
    
    a "This is where Chiron and our camp director lives, Dionysus."

    a "It's also the infirmary and war room."

    scene combat area at fullscreen

    show Addy Guide

    a "This is where our arena, climbing wall, and archery range are."

    scene forest at fullscreen

    show Addy Guide

    a "Of course, this is the forest. We have Canoe Lake and a beach a little past here."

    scene stables at fullscreen

    show Addy Guide

    a "And here's the stables."

    scene main camp

    show Addy Guide

    a "And that's the end of our tour."

    a "We also have a forge, volleyball courts, armory, showers, ampitheater, and strawberry fields. Pretty much everything you can think of."

    a "Any questions?"

    menu:
        "Any questions?"
        "None":
            a "Awesome! I'll see you later then, you can go do whatever. Maybe look through the cabins?"

            a "We have a schedule everyday depending on your cabin. You can find the Hermes one on the board in our cabin."

        "What do we do everyday?":
            a "We have a schedule everyday depending on your cabin. You can find the Hermes one on the board in our cabin."

        "How can I get claimed as soon as possible?":
            a "Eager, okay! You just have to wait, do some activities or something. Go talk to other cabins."
    
    a "Au revoir mon ami. I'll catch you for dinner tonight? I gotta head to the wall."

    #Add the these choices will have consequences

    menu:
        "Go with her to the wall?":
            m "Can I come with?"
            a "For sure!"
            scene Wall
            #Add minigame.


        "Go to Apollo Cabin?":
            hide Addy
            scene Apollo Cabin
            show Oli argue:
                xalign 0.8
            show Grace argue:
                xalign 0.2
            o "Dude, shut up. You don't even know what you're talking about."
            g "No, I'm completely right!"
            g "Oh! Girl over there! Chik fil a is better than In n Out right??"
            menu:
                "What to say?"
                "Chik fil a, for sure.":
                    show grace happy:
                        xalign 0.2
                    g "I WAS RIGHT!"
                    o "That's one opinion."
                "In n Out is better.":
                    show grace sad:
                        xalign 0.2
                    g "Fine. You win this time."
                    o "Knew it."

            show Oli Happy:
                xalign 0.8
            show grace happy:
                xalign 0.2
            
            $ know_grace = True

            $ know_oli = True

            g "Anyway, hello!!!! I haven't seen you around? I'm Grace!!"

            #NOTIFICATION and variable

            m "I'm Moriah!"

            o "I'm Oli, nice to meet you. I'm the head of Apollo cabin."

            #NOTIFICATION

            "{i} He doesn't look like who I would've thought an Apollo kid would look like. {/i}"

            g "I am the unofficial cohead of Apollo cabin! --" 
            o "-- No she's not."
            g "Have you got your godly parent yet?"

            m "Not yet, got here today."

            o "Well, you should hope to be Apollo's kid! If you are, I can show you around! Also our dad is the most... well fatherly."

            m "I'll keep that in mind. Thanks!"

            show grace wink

            g "You'll also find that he has the most kids.... Our dad is very active. Let's say."

            o "Ignore her. Anyway, we gotta get to training. We'll see you for dinner!!!"

        "Explore the camp?":
            hide Addy
            scene Main Camp
            show jasper sad
            j "AH!!!!!"
            m "Are you okay??"
            j "NO! I don't think I can finish my stupid poster today."
            m "What poster?"
            j "I'm supposed to make the poster for like motivation for my cabin, but Capture the Flag is tomorrow and I still haven't finished."
            menu:
                "What to say?"
                #This action will have consequences later in the game.
                "I can help you!":
                    show jasper happy
                    j "Really? Thanks!"
                    m "Of course! What can I do?"
                    j "Well, right now you can help me colour, and if you wanna come tomorrow, you could help me put it up? I really need someone to help me hang it."
                    m "Sure! I can help you with that."
                    j "Awesome!!! By the way, I'm Jasper. Son of Iris."
                    $ know_jasper = True
                    #NOTIFICATION and variable
                    m "Moriah! Unclaimed for now."
                    #White out and later
                    j "Well! That's all for now, but I really appreciate your help!"
                    j "I hope to see you tomorrow!"
                "Oh. Well I wish you luck!.":
                    show jasper sad
                    j "Thanks. I'll see you later then."

    scene Dinner
    show Addy food:
        xalign 0.2
    a "Heyyyyy! How was your day?"
    m "Pretty good!"
    a "Awesome! Well, welcome to the dining pavillion, you can grab your food over there."
    a "The rest of Hermes cabin will meet up with us soon."
    show Adrien food:
        xalign 0.8
    ad "Yello!"
    ad "Woah new kid. Didn't know we associated with that type."
    a "He's joking. This is Moriah."
    ad "Hi Moriah! I'm Adrien."
    m "Hello!"
    a "She's unclaimed so she'll be staying with us for a bit."
    ad "Dammit. I was loving not having any unclaimed kids with us."
    a "Dude, you can't say that."
    ad "Right, right. Oppressing the speech of the youth, I see how it is."
    m "Wowwwww, that's low."
    a "Oh whatever, I'm leaving. I'll see ya at the campfire."
    hide Addy food
    m "The campfire? What campfire?"
    ad "Oh, every day after dinner we do a campfire. To promote bonding or something."
    m "Good to know"
    # TIME SKIPPPPPPPPPPP
    scene campfire
    show Addy happy:
        xalign 0.2
    show Adrien happy:
        xalign 0.45
    m "So this is it?"
    ad "Yup!!!! We just like sing songs and talk and stuff."
    show Manuela camp:
        xalign 0.8
    ma "ADRIEN. I GOT TEA."
    ma "Woah new kid who dis?"
    ad "That's Moriah, not important, what tea???"
    ma "Okay okay. You know the kid from Hypnos. The hot one?"
    ad "Which one, they're all hot."
    ma "The one who gave me his hoodie."
    ad "OOOOOOOOOH YES. WHAT ABOUT HIM."
    ma "HE ASKED ME TO FIGHT WITH HIM FOR CAPTURE THE FLAG."
    ad "OH MY GOD I'M SO HAPPY FOR YOUUUUU!"
    menu:
        "What to say?"
        "Who?":
            ma "Nosy one, aren't you?"
            ma "His names Connorrrrr. He's really cute."
            a "No he's not."
            ma "Shut up Canadian."
            a "Oh my god, I hate my friends."
            m "Wait, point him out for me."
            ma "He's not here right now, Hypnos cabin typically likes to just chill instead of the campfire."
            m "We get a choice????"
            a "No they're just the exception."
        "Stay out of it.":
            a "He's not that cute."
            ma "Shut up Canadian."
            a "Yeah okay, whatever."
    ad "Anyway, onto other news. Moriah, this is Manuela."
    # NOTIFICATIONNNN
    m "Hello!"
    ma "Hi! IIIII can introduce myself, thank you. I'm Manuela."
    a "Shh guys, Grace is starting the song."
    g "Amazingggg Gra---"
    c 'NOT THE SONG, GRACE.'
    g "Right, sorry."
    g "{i}This land is Minos' land---{i}"
    # TIME SKIPPPPPP

    scene Hermes beds
    show Addy sleep
    a "Alright, you can sleep over there. Me and Adrien are up in the bunks if you need us."
    m "Got it! Goodnight!!!"
    
    # TIME SKIPPPPP

    scene Hermes beds
    "{i}Loud commotion and moving as everyone wakes up.{i}"
    m "urghhhhh."
    show Addy happy:
        xalign 0.2
    show Adrien happy:
        xalign 0.8
    a "Mornin' Sunshine. Rise and shine."
    ad "Addyyyyyyy. I'm hungryyyyyyy. Let's go."
    ad "Oh, Moriah, We'll see you at breakfast."
    a "Bye?"
    hide Addy happy
    hide Adrien happy
    m "{i}Guess it's time to get up then.{i}"


    scene Dining pavillion
        #Make IF MET BLANK
    menu:
        "Where to sit?"
        "Hermes Cabin?":
            show Addy food
            a "Hey nice to see you again!"
            a "You can grab food over there."
            #Whiteout
            m "What are we doing today?"
            a "Well, in a bit we'll be heading to the ampitheater for Ancient Greek."
            a "Oh! And tonight we have the camp capture the flag."
            a "It's gonna be so fun. Trust me, you'll love it."
            m "Oh, okay cool!"
            a "I gotta go start gathering kids for Greek. See ya there soon!"
            hide Addy food
        "Apollo Cabin?" if know_grace:
            show Oli food:
                xalign 0.2
            show grace food:
                xalign 0.8
            o "Woah, hey!"
            g "It's the newbie."
            o "Enjoying camp?"
            menu:
                "What to say?"
                "Haven't experienced much yet.":
                    o "Okay, okay. Mature answer. You'll grow to like it."
                "I love it, it's really amazing.":
                    show grace happy:
                        xalign 0.8
                    g "YES!!!!"
            show grace food:
                xalign 0.8
            show oli excited:
                xalign 0.2
            o "Oh wait, if you're here did you get your cabin?"
            m "No, not yet. Still unclaimed."
            show oli disapointed:
                xalign 0.2
            g "That's alright! You'll figure it out eventually."
            show oli food:
                xalign 0.2
            m "Yeahhhh, I guess so."
            o "What is Hermes cabin doing today?"
            m "I heard we were going to the ampitheater for Ancient Greek?"
            g "Oh, I hate that part of camp."
            o "Whaaaaat. It's really fun. I know how to say so many words in Greek..."
            m "No good ones I assume?"
            o "You'd assume right."
            g "Well, we gotta head off to chores, so have fun at the ampitheater!"
            hide grace food
            hide oli food

        "Iris Cabin?" if know_jasper:
            show jasper happy
            j "Hey there new friend!"
            m "Hey Jasper!!!"
            m "What's up?"
            j "Excited to finally hang up my poster. What about you?"
            m "I don't know. I'm not sure what I'm supposed to be doing today to be honest."
            j "Yeah you'll have to talk to your head for that."
            j "I'm excused for everything today. Poster privilege!"
            m "Is it that important????"
            j "No, but I'm friends with my head and they're the favourite."
            j "The Iris kids are Dionysus' second favourite, after his own kids, of course."
            j "He likes their ability to send messages and like the arts or something."
            m "Huh, nice!"
            j "Anyway, I gotta go. I'm pretty sure your next place to go is to the ampitheater for greek lessons."
            j "I think Iris and Hermes are there together right now."
            hide jasper happy
        "Skip breakfast?":
            scene ampitheater at fullscreen
    menu:
        "What to do?"
        "Go to the ampitheater for class?":
            scene ampitheater at fullscreen
    show Chiron
    c "Alright everyone!"
    c "I asked to take over class for today, I need to brush up on my Greek."
    c "Now, let's learn some basics."
    #TIME SKIPPPPP
    c "Test time!!!"
    c "How do you say 'How are you?'?"
    menu:
        "What to guess?"
        "Με λένε":
            c "Incorrect."
        "Χαίρω πολύ":
            c "Incorrect."
        "Τι κάνεις":
            c "Correct!"
        "Πόσο κάνει αυτό":
            c "Incorrect."
    c "What about asking if someone speaks English?"
    menu:
        "What to guess?"
        "Μιλάτε αγγλικά":
            c "Correct!"
        "Δεν καταλαβαίνω":
            c "Incorrect."
        "Μαθαίνω ελληνικά":
            c "Incorrect."
        "Μπορείτε να μιλήσετε":
            c "Incorrect."
    c "Okay, now what about, 'Good afternoon'?"
    menu:
        "What to guess?"
        "Καληνύχτα":
            c "That's goodnight, close."
        "Καλησπέρα":
            c "Correct!"
        "Ευχαριστώ":
            c "Incorrect."
        "Παρακαλώ":
            c "Incorrect."
    c "One last one, what is 'goodbye'?"
    menu:
        "What to guess?"
        "Τα λέμε":
            c "So close!"
        "Πώς λέμε":
            c "Incorrect."
        "Με λένε":
            c "Incorrect."
        "Γειά σου":
            c "Correct!"
    c "Now, I must go prepare for your guys' capture the flag. Bye!"
    hide Chiron
    show Addy Neutral
    a "Hey Riah!"
    a "You ready for capture the flag?"
    m "Not really..."
    a "Haha no worries, you'll get the hang of it."
    a "Follow me, we gotta go get prepared."
    scene forest
    show Sammy Games
    s "ALRIGHT GUYS."
    s "WE ARE GOING TO RULE THIS CAPTURE THE FLAG."
    s "EVERYONE KNOW WHAT TO DO?"
    s "New kid?"
    s "We have tons of people, wanna do defense, offense, or what?"
    menu:
        "What are you choosing?"
        "Defense":
            s "Alright, you stay back and protect the flag with the rest."
            s "Take a sword."
        "Offense":
            s "Eager, alright! Grab a bow and arrow, and head up with Addy."
            s "I'll be right behind you once the game starts."
        "Can I sit out?":
            s "Yeah... I guess.... You go sit with Zach then, up around Chiron. You can watch or whatever."
            scene sitout
            hide Sammy Games
            show Gus
            g "You sitting out too?"
            m "Yeah, I guess so."
            g "I get that. I hurt my leg so I'm out."
            g "Oh! The bands about to pass by, are you planning to join them?"
            menu:
                "Do you want to join the bands?"
                "Yes":
                    g "Woah, okay. HEY GUYS! NEW KID WANTS TO JOIN!"
                    show Sandy:
                        at xalign 0.2
                    s "OF COURSE! FOLLOW US!"
                    hide Gus
                    # WHITEOUT
                    scene forest
                    show Sandy
                    show Grace:
                        at xalign 0.8
                    g "Here to cheer us on?"
                    m "Yup!"
                    g "Moriah... there's a sign over your head?"
                    m "OH MY GOD, OH MY GOD, OH MY GOD."






    # This ends the game.

    return
