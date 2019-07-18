# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Images
image back = "back.png"
image fam_happy = im.FactorScale("fam_happy2.png", 0.5)
image sun = im.FactorScale("sun.png", 0.05)
image fam_mutate = im.FactorScale("fam_mutate.png", 0.5)
image cells_mutate = im.FactorScale("cells_mutating.png", 0.4)
image gfr = im.FactorScale("gfr.png", 0.5)
image star = im.FactorScale("star.png", 0.1)
image ras = im.FactorScale("ras.png", 0.5)
image her2 = im.FactorScale("her2_label.png", 0.4)
image myc = im.FactorScale("myc.png", 0.5)
image points_text = ParameterizedText(xalign=0.98, yalign=0.02, line_spacing=1)
image chapter_text = ParameterizedText(xalign=0.06, yalign=0.02)
image pencil = im.FactorScale("pencil2.png", 0.45)
image eraser = im.FactorScale("eraser.png", 0.6)
image ruler = im.FactorScale("ruler.png", 0.45)
image paperclip = im.FactorScale("paperclip.png", 0.5)
#Characters
define g = Character("GF Receptors", who_color="#874caa")


# The game starts here.


label start:

label ch1screen:
    scene back
    show text "{size=+10} Chapter 1: The Mutation {/size}" at truecenter with dissolve
    pause 2
    hide text with dissolve
    hide fam_mutate with dissolve

    $ points = 0
    $ totalqs = 5

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show pencil:
        rotate 5
        xalign 1.1
        yalign 0.2
    show eraser:
        rotate 15
        xalign 1.0
        yalign 0.8
    show ruler:
        rotate -7
        xalign -0.25
        yalign 0.4
    show paperclip:
        xalign 0.1
        yalign 0.3
    show sun:
        xalign 0.01
        yalign 0.01
    show chapter_text "Chapter 1"
    show star:
        xalign 0.83
        yalign 0.0
    show points_text "Points: [points] / [totalqs]"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

#scene 1: Protooncogenes
label scene1:
    "You awake with a feeling of uneasiness. Your intuition tells you that something is wrong."
    "You check the sensors and with a jolt of panic you realise what you had been dreading had come true..."
    "No... it couldn’t be..."


    show fam_happy with moveinbottom:
        yalign 0.4
        xalign 0.5

    "It had happened to one of your most loyal communities: the proto-oncogenes."
    "They were essential to the  body’s function and survival, after all, they were performed the following important tasks:"

    jump q1


label q1:
    $ q1_tried = False

label q1menu:
    menu:
        "What are proto-oncogenes' function?"

        "Stimulate proliferation":
            $ q1_tried = True
            jump incorrect_q1

        "Inhibit Apoptosis":
            $ q1_tried = True
            jump incorrect_q1

        "Both of the above.":
            if not q1_tried:
                $ points += 1
                show points_text "Points: [points] / [totalqs]"
            jump correct_q1

label correct_q1:

    "Correct! Protooncogenes are normal genes responsible for cell growth through altering the processes of proliferation and apoptosis."
    jump q2

label incorrect_q1:

    "Incorrect. Try again."
    jump q1menu



label q2:
    $ q2_tries = 0
    hide fam_happy
    show fam_mutate:
        yalign 0.4
        xalign 0.5
    "However, proto-oncogenes were very prone to falling ill to The Mutation, in which they would become:"

label q2menu:
    $ q2answer = renpy.input("What are mutated proto-oncogenes called?")
    $ q2answer = q2answer.strip()

    if q2answer == "oncogene" or q2answer == "oncogenes" or q2answer == "Oncogene" or q2answer == "Oncogenes":
        if q2_tries == 0:
            $ points += 1
            show points_text "Points: [points] / [totalqs]"
        jump correct_q2
    else:
        if q2_tries > 2:
            jump q2_answer
        $ q2_tries += 1
        jump incorrect_q2


label correct_q2:
    "Correct!"
    jump scene2

label incorrect_q2:
    "Incorrect. Try again."
    jump q2menu

label q2_answer:
    "Incorrect. Answer is 'oncogene'."
    jump scene2


#SCENE 2: Oncogene suspects
label scene2:
    hide fam_mutate
    show cells_mutate:
        yalign 0.15
        xalign 0.5
    "You felt a wave of sadness rush over you as you realised that one of them had succumb to 'The Mutation': a horrible infliction."
    "It caused those affected unable to perform their jobs, essentially turning them into traitors against their own!"

    "This was a terrible occurrence. But first, you needed to figure out who it was that had fallen to the Mutation."
    "Based on what your vast knowledge of past afflictions and the information from your sensors, you narrow it down to three suspects."

    hide cells_mutate

label scene2menu:
    menu:
        "Click on each of the suspects to find out more about their function."
        "Ras gene":
            jump ras
        "HER2":
            jump her2
        "Myc gene":
            jump myc
        "I'm done!":
            jump scene3

label ras:
    show ras:
        xalign 0.5
        yalign 0.2
    "Ras is a family of GTP-binding proteins involved in signal transduction."
    "Ras responds to signals from cell surface receptors, and acts as a switch between two states."
    "In its GDP-bound state, is when it is held inactive."
    "However, when bound to GTP, it is switched ‘on’, which activates a signal cascade of protein kinases to stimulate cellular cell growth."
    hide ras
    jump scene2menu

label myc:
    show myc:
        xalign 0.5
        yalign 0.2
    "The Myc gene is a family of proto-oncogenes. Myc serves as the master transcription factor to promote entry into the S phase of the cell cycle."
    "Ways they do this is by activating cyclin D, a cyclin that binds to CDK4/6 involved in the G1 to S phase transition."
    "Myc also degrades p27, an inhibitor of S-phase cyclin/CDK complexes."
    hide myc
    jump scene2menu

label her2:
    show her2:
        xalign 0.5
        yalign 0.2
    "HER2 is a proto-oncogene that has a structure similar to human epidermal growth factor receptor (HER1), thus earning its name."
    "It is a transmembrane protein, responsible for activating signal pathways by phosphorylating tyrosine within its cytoplasmic domains."
    "This is done through a process called dimerization. Ultimately, these signals result in cell proliferation."
    hide her2
    jump scene2menu


#Scene 3: Growth factors
label scene3:
    hide cells_mutate
    "You come across a pair that signals you over for help."
    show gfr:
        xalign 0.5
        yalign 0.3
    # This ends the game.
    g "Hey you!"

    "The two speak in unison, their voices melding together melodically."
    "However, they look as terrified as you feel inside."
    "Their job here was highly important. After all, they:"
    $ q3_tried = False

label q3:
    menu:
        "Which of the following is true? Growth factor receptors..."
        "Are a transcription factor for S phase genes":
            $ q3_tried = True
            jump q3_incorrect


        "Begin a signal cascade":
            if not q3_tried:
                $ points += 1
                show points_text "Points: [points] / [totalqs]"

            jump q3_correct

        "Bind with CDK complexes":
            $ q3_tried = True
            jump q3_incorrect


label q3_correct:
    "Correct! Growth factor receptors are the first step of the signalling cascade."
    "They are transmembrane proteins which are activated when a growth factor binds."
    "When activated, they convey signals to the intracellular space to stimulate the cell to grow or divide."
    jump q4

label q3_incorrect:
    "Incorrect. Try again."
    jump q3

label q4:
    $ q4_tries = 0
    "What kind of binding is it that signals this signalling pathway?"

label q4menu:
    $ answer2 = renpy.input("Type of binding that causes growth factor receptors to come together:")
    $ answer2 = answer2.strip()
    if answer2 == "ligand" or answer2 == "Ligand":
        if q4_tries == 0:
            $ points += 1
            show points_text "Points: [points] / [totalqs]"
        jump q4_correct
    else:
        if q4_tries > 2:
            jump q4_answer
        $ q4_tries += 1
        jump q4_incorrect

label q4_correct:
    "Correct!"
    jump gfr

label q4_incorrect:
    "Incorrect. Hint: starts with 'L'"
    jump q4menu

label q4_answer:
    "Answer is 'ligand binding'."
    jump gfr

label gfr:
    g "Something strange has been going on. It's one of our colleagues we work closely with."
    g "Usually he's just sitting around not doing much, until we send him the signal when we receive our growth factor and send some signals into the cell."
    g "This eventually switches him on, and starts sending the signals himself. It's like that GTP drives him crazy or something."
    g "But recently, he's just always activated! Even when we don't have our growth factor with us. He never even takes a break anymore!"


label q5:
    "That was a strange occurrence indeed. Based off what you have learnt, which proto-oncogene do you think has mutated?"
    $ q5_tried = False

label q5menu:
    hide gfr
    show ras:
        xalign 0.2
        yalign 0.2

    show her2:
        xalign 0.5
        yalign 0.2

    show myc:
        xalign 0.85
        yalign 0.2

    menu:
        "Which proto-oncogene has mutated?"

        "Ras":
            if not q5_tried:
                $ points += 1
                show points_text "Points: [points] / [totalqs]"
            jump q5_correct
        "HER2":
            $ q5_tried = True
            jump q5_incorrect
        "Myc":
            $ q5_tried = True
            jump q5_incorrect

label q5_correct:
    "Correct! Ras gene has mutated...  "
    jump scene4

label q5_incorrect:
    "Incorrect. Try again."
    jump q5menu

label scene4:
    hide ras
    hide her2
    hide myc
    "This was terrible. What could you do to fight back?"

    if points >= 3:
        "You have enough points. Proceed to chapter 2?"
        menu:
            "Go to chapter 2":
                jump chapter2
            "I want to replay chapter 1":
                jump start
    else:
        "You need at least 3 points to progress the story. Retry chapter?"

        menu:
            "Get at least 3 points to progress!"
            "Retry":
                jump start

label chapter2:
    "sigh I have not done chapter 2 yet"
    ":("

    return
