define me = Character("Me")
define a = Character("Atlas")
define l = Character("Luna")
define nani = Character("???")
label start:
    stop music fadeout 1.0
    scene black
    with Dissolve(1.0)
    play music "waves.mp3" fadeout 1.0 fadein 1.0
    "The soft sound of ocean waves gently lulling back and forth is the first thing I remember."
    "The next thing I remembered was the soft, warm, and bright rays of sunshine on my face, waking me from my gentle sleep."
    "That's about all I could remember. Besides that, my mind was clear, I couldn't recall my age, name, or anything like that."
    me"Where am I? What is this place?"
    "My eyes slowly opened and greeted the bedroom I was in."
    scene bedroom
    with Dissolve(3.0)
    "Oh, this is..."
    "Not a place I was familiar with."
    "Everything here was foreign to me... but I was overcome with a strange feeling of Deja Vu, like I've been here before."
    "Who am I?"
    "I pointed at the window in front of me."
    me"That's a window, and those are curtains over the edges."
    "Next, I pointed at the wall."
    me"That's a poster for some kind of rock band."
    "How come I know everything about this room, yet nothing about myself?"
    "I know what these things are, but I still can't remember where they come from..."
    "I couldn't put this feeling into words."
    "I didn't even know what I looked like. Maybe I had dark hair, maybe it was light."
    "Or maybe it was the shock of waking up in this place that confused me."
    "Think... who am I?"
    pause 0.5
    "Nope. I can't even remember what I look like."
    "I slowly lifted myself out of bed, my muscles stiff like I just woke up from a deep sleep."
    "I noticed a mirror accross from my bed, and I came towards it."
    scene mirror
    with Dissolve(3.0)
    "I was greeted by my face, foreign to myself."
    "Emerald eyes, brown hair..."
    "My face was seriously plain, I looked like anybody you could run into on the street."
    "This face I saw was undoubtedly my own."
    "I didn't know why, but it was clear to me that this was my face."
    "Yet, for some reason..."
    "I still didn't recognize who it was I was looking at."
    "This whole situation I'm in feels really weird."
    "I woke up in a foreign land, with no knowledge or resources..."
    "And to top it off, I didn't know anything about myself, not even my name."
    "This is just like something that would be inside of an anime, isn't it?"
    "An isekai, a story where the protagonist wakes up in another world."
    "But honestly, nothing amazing has happened to me yet, I felt more like an NPC or a side character. "
    "The confusion only grew at this point."
    "Was I an important person?"
    "Where was everyone else?"
    "I walked away from the mirror and just stood in the middle of the room."
    scene bedroom
    with Dissolve(3.0)
    "You know..."
    "This place has a seriously bad musty smell."
    "It's getting hard to breathe in here."
    "I don't want to stay around here for so long."
    "Should I leave this place?"
    jump leave
label leave:
    menu:
        "Should I leave this place?"
        "Yes.":
            stop music fadeout 1.0
            play music "Happy.wav" fadeout 1.0 fadein 1.0
            scene town
            with Dissolve(3.0)
            "I walked outside the room, to find myself in the middle of a town square."
            "The gentle sound of the waves and the gentle wind blowing onto my face was certainly relaxing, yet I was still overcome by a feeling of confusion and being lost."
            "Though it was a town square, and quite a nice one too, not a single person was in sight. Where had everyone gone?"
            "A quick thought brushed my mind, one that said the worst of the worst. I tried to shut it out, but it rang loud and clear inside of my head."
            "\"What if I was the only person left on this island... what if everyone else was dead?\""
            "Suddenly, the serenity and peace of the gentle waves and wind became a deathly silence, I wished for something... anything... to break this silence."
            "I didn't want to be alone."
            me"Hello? Is anyone here?"
            pause 1.0
            "I was greeted by silence again."
            "Determined to find anyone on this island, I pressured on. Maybe it was just so I could prove myself wrong, or maybe I was just lying to myself."
            "Either way, the thought subsided, and I was filled with a determination to find any sign of life here."
            jump townsquare
        "No.":
            "This place is seriously getting on my nerves."
            "It smells terrible!"
            "I can't breathe!"
            "I really want to leave!"
            jump leave
label townsquare:
    "My legs pushed me forward, even though I had no idea where I was going. Eventually, I arrived at what appeared to be an street connected to the town square."
    scene road
    with Dissolve(1.5)
    "Instinctively, I called out to the silence that greeted me when I arrived."
    me"I-i-is anyone here? I'm lost and I need some help!"
    pause 1.0
    "Once again, I was only answered by more silence."
    "The road itself wasn't very fancy, it would just have been like any old street you'd see on the street."
    "Still, with no one here... it raises a pretty big red flag."
    "If no one was here, who was keeping it in this good condition?"
    "Puzzled, I went to look for more answers, moving on further away from the town square."
    scene garden
    "I arrived at a garden. Just looking at it made me puzzled me further."
    "It was beautifully kept. A ring of blooming roses and daisies adorned a tall oak tree, and an adorned gazebo lay at the middle of the garden."
    "Understanding that there was probably no one here, I looked around the garden just to see if I could at least find a sign of life on this island."
    pause 1.0
    "Nope. Not a single person was in sight here."
    "I sighed, and I put my hands to my face..."
    me"What kind of place is this?"
    me"I just want to find someone, anyone!"
    me"Not only is there no one here, even I'm not here!"
    me"Who the hell am I?!"
    "I shouted that question to the skies, who just as before, answered me with apathy."
    "Frustrated, I headed back to the town square, tired and confused by the situation I was in."
    "Maybe I took a wrong turn, but it wasn't the town square that I ended up."
    jump shore
label shore:
    scene shore
    with Dissolve(3.0)
    stop music fadeout 1.0
    play music "waves.mp3" fadeout 1.0 fadein 1.0
    "This is... a shoreline?"
    "Is this town... actually an island?"
    "I gazed upon the waters, to see if there was any kind of land I could spot."
    "All that greeted me was the line that the sky touched the water, no land in sight."
    "Still confused by how I ended up on the shore instead of the town square, I was about to turn back so I could head to back, until I saw what appeared to be a silhouette of someone on the sand."
    "There appears to be someone here."
    "A girl, I think."
    "Should I approach her?"
    menu:
        "Should I approach her?"
        "Approach the girl.":
            jump shorelinewalk
        "Keep my distance.":
            jump undesirableending
label shorelinewalk:
    show luna
    nani"..."
    me"Hi. What's your name?"
    "I couldn't tell her age."
    "She could've been anywhere from 14 to 25."
    "She had a look of both maturity and youth to herself."
    nani"..."
    "Maybe she didn't hear me."
    "I asked her once again."
    me"Hi, what's your name?"
    nani"Were you never taught proper manners?"
    me"I'm sorry?"
    nani"Why are you repeating what you just said?"
    nani"If I didn't answer you the first time, what made you think the second one would yield anything different?"
    "She sighed."
    nani"It doesn't matter."
    "She turned and walked off."
    hide luna
    with Dissolve(2.0)
    "She took a few steps before she turned around towards me."
    nani"Come."
    "Honestly, her attitude kind of bugged me, and came off as bratty, but seeing as she was the only other person I could find on this island, I obeyed her."
    "I followed her as she walked on the shoreline, her feet making small footprints in the sand."
    "I attempted to make small talk with the girl."
    me"Hey, it's nice to meet you, I'm uh..."
    "Remembering that I didn't know my name, I realised the mistake I made."
    me"I'm err, pleased to meet you."
    nani"..."
    "The silence from her told me that she didn't want to make any conversation with me."
    "So, instead of trying to engage with her, I just kept following her around the shore."
    scene beach2
    with Dissolve(0.5)
    "As we walked on the shore line, I began to notice more about this place I was in."
    "It looks like I was right earlier, it really is an island."
    "The island wasn't particulary big, but was able to accomodate a town."
    "Besides my room, the town square, and the garden, there was quite a bit more on the town i didn't pass through."
    "There was what looked like a library, a forest, and more. I tried to identify them, but the girl walked at a pretty fast pace, and I only got small glimpses of everything else."
    scene shore
    with Dissolve(0.5)
    show luna
    "Once we made on full circle around the island, I decided to ask her another question."
    me"Say, have you seen anyone else on this island?"
    "I expected her to answer with silence, but I was wrong."
    "Instead, she asked her own question."
    nani"What do {i}you{/i} think about this island?"
    "I was confused, and didn't quite know how to answer her, maybe it was a response to the question I asked earlier, but I wasn't really sure."
    "I didn't quite know how to respond, but I guessed that she wouldn't like me to question her motives."
    "But this could be my only chance to get anything from her, so I decided to answer her."
    me"You know... this island... I'm completely clueless about it."
    me"Matter of fact, I guess you could say I'm on my own island, one inside of my head."
    "I didn't know where this weird poetic talk came from, but I just went with it."
    me"I'm trapped inside of my head, clueless about myself. My name... my age... everything... it's on the mainland, but all I can see from where I am is the empty horizon."
    me"As you can probably tell, I'm just as lost on this island as I am inside of my own head."
    nani"..."
    "She didn't even grace me with a response or a follow-up question."
    scene ocean
    with Dissolve(1.0)
    "Instead, she looked out into the ocean, and gazed, looking like she was lost in thought."
    "I decided to do as she did, but unlike her, I didn't seem to understand what was so special about it."
    "The ocean wind blew onto my body, and the waves came back and forth."
    "It was such a plain scene, but we stood like that for minutes, maybe hours, I lost track of time."
    "Suddenly, she turned and continued walking, and I followed."
    scene beach2
    with Dissolve(0.5)
    "I made small comments, and occasionally asked questions. Normally, she would just ignore them, but rarely she'd answer them, or maker her own small comment."
    "Usually they were also not much, and I didn't learn much about her."
    "For example, when I asked, \"Small island, huh?\" she just said, \"Yeah.\" and continued walking, like she was completely uninterested."
    scene nightshore
    with Dissolve(3.0)
    "By the time we had made our second walk around the shore, it had become night time."
    show luna
    nani"This walk was..."
    nani"Unproductive. I'm going to take my part now."
    nani"Farewell."
    "She was about to turn away and head towards the town square."
    me"Wait, before you go..."
    me"I'd like to ask one more question."
    nani"..."
    "Silence."
    "Regardless, I asked her the question."
    me"What's your name?"
    "She turned towards the night sky, and stared."
    "I looked up as well."
    scene nightsky
    with Dissolve(3.0)
    stop music fadeout 1.0
    play music "piano.wav" fadeout 1.0 fadein 1.0
    "The full moon glistened in the night sky."
    "The stars were little specks of light in the sky, ready to guide anyone lost to a new path."
    "It was breathtaking, and beautiful."
    nani"My name is..."
    l"Luna. Call me Luna. I think it's... fitting. Anything you want me to call you, nameless?"
    "At this moment I realised..."
    "On this deserted island, it was likely just the two of us, on this island."
    "There was no one else."
    "No one for me to depend on."
    "And no one for Luna to depend on."
    "Except for each other."
    "Because if either of us were going to survive here, we were going to need each other."
    "I don't want to be alone here."
    scene nightshore
    with Dissolve(3.0)
    "I want to hold her up."
    "So I answered her:"
    a"Atlas. My name is Atlas."
    show lunanight
    "It was a hamfisted response."
    "It was clear that neither of us were telling each other our real name."
    "She seemed to understand what I meant with my name, but she showed no sign of it."
    "Save for what looked like a small glimpse of a smile on her face. I blinked, and it was gone."
    "She asked another question."
    l"When can I see you again?"
    a"Anytime. I probably can't leave this island… so I’ll be at the shore tomorrow, as early as possible."
    hide lunanight
    with Dissolve(3.0)
    "She simply nodded, turned, and leaved. Honestly, I wanted to ask another question, but when I turned around, all I saw were light footprints in the sand."
    "And with a blink they’re blown away by the gentle night wind, and the beach turned pristine once again."
    "Like she'd never been there."
    scene black
    with Dissolve(1.0)
    "Skrrt Skrrt! This is the ending of the demo!"
    "Tell me what you thought!"
    return
label undesirableending:
    scene black
    with Dissolve(1.5)
    "This was supposed to lead into another ending, but in all honesty, I haven't fleshed this out much, so nyeh, you're gonna have to take it."
    "Thanks, gamers! Love you all!"
    return
