# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Images
image back = "back.png"
image fam_happy = im.FactorScale("fam_happy2.png", 0.5)
image sun = im.FactorScale("sun.png", 0.5)
image fam_mutate = im.FactorScale("fam_mutate.png", 0.5)
image cells_mutate = im.FactorScale("cells_mutating.png", 0.4)
image gfr = im.FactorScale("gfr.png", 0.5)
image star = im.FactorScale("star.png", 0.1)
image ras = im.FactorScale("ras.png", 0.5)
image her2 = im.FactorScale("her2_label.png", 0.4)
image points_text = ParameterizedText(xalign=0.98, yalign=0.02, line_spacing=1)

#Characters
define g = Character("GF Receptors", who_color="#874caa")



# The game starts here.



label start:
    $ points = 0
    $ totalqs = 6

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene back

    show star:
        xalign 0.83
        yalign 0.0
    show points_text "Points: [points] / [totalqs]"
    jump scene3
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

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
    jump scene2

label incorrect_q1:

    "Incorrect. Try again."
    jump q1menu

label scene2:
    $ q2_tries = 0
    hide fam_happy
    show fam_mutate:
        yalign 0.4
        xalign 0.5

    "However, proto-oncogenes were very prone to falling ill to The Mutation, in which they would become:"

label q2:
    $ q2answer = renpy.input("What are mutated proto-oncogenes called?")
    $ q2answer = q2answer.strip()

    if q2answer == "oncogene" or q2answer == "oncogenes" or q2answer == "Oncogene" or q2answer == "Oncogenes":
        if q2_tries == 0:
            $ points += 1
            show points_text "Points: [points] / [totalqs]"
        jump correct_q2
    else:
        if q2_tries > 2:
            jump scene3
        $ q2_tries += 1
        jump incorrect_q2


label correct_q2:
    "Correct!"
    jump scene3

label incorrect_q2:
    "Incorrect. Try again."
    jump q2


#SCENE 3
label scene3:
    hide fam_mutate
    show cells_mutate:
        yalign 0.15
        xalign 0.5
    "You felt a wave of sadness rush over you as you realised that one of them had succumb to 'The Mutation': a horrible infliction."
    "It caused those affected unable to perform their jobs, essentially turning them into traitors against their own!"

    "This was a terrible occurrence. But first, you needed to figure out who it was that had fallen to the Mutation."
    "Based on what your vast knowledge of past afflictions and the information from your sensors, you narrow it down to three suspects."

    hide cells_mutate

label scene3menu:
    menu:
        "Click on each of the suspects to find out more about their function."
        "Ras gene":
            jump ras
        "HER2":
            jump her2
        "Myc gene":
            jump myc
        "I'm done!":
            jump scene4

label ras:
    show ras:
        xalign 0.5
        yalign 0.2
    "Ras is a family of GTP-binding proteins involved in signal transduction."
    "Ras responds to signals from cell surface receptors, and acts as a switch between two states."
    "In its GDP-bound state, is when it is held inactive."
    "However, when bound to GTP, it is switched ‘on’, which activates a signal cascade of protein kinases to stimulate cellular cell growth."
    hide ras
    jump scene3menu

label myc:


label her2:
    show her2:
        xalign 0.5
        yalign 0.2
    "HER2 is a proto-oncogene that has a structure similar to human epidermal growth factor receptor (HER1), thus earning its name."
    "It is a transmembrane protein, responsible for activating signal pathways by phosphorylating tyrosine within its cytoplasmic domains."
    "This is done through a process called dimerization. Ultimately, these signals result in cell proliferation."
    hide her2
    jump scene3menu

label scene4:
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

label q4_correct:
    "Correct! Growth factor receptors are the first step of the signalling cascade."
    "They are transmembrane proteins which are activated when a growth factor binds."
    "When activated, they convey signals to the intracellular space to stimulate the cell to grow or divide."

    "What kind of binding is it that signals this signalling pathway?"
    $q5_tries = 0

label q5:
    $ answer2 = renpy.input("Type of binding that causes growth factor receptors to come together:")
    $ answer2 = answer2.strip()
    if answer2 == "ligand":
        jump q5_correct
    else:
        if q5_tries > 2:
            jump q5_answer
        $ q5_tries += 1
        jump q5_incorrect

label q5_correct:
    "Correct!"
    jump scene6

label q5_incorrect:
    "Incorrect. Hint: starts with 'L'"
    jump q5

label q5_answer:
    "Answer is 'ligand binding'."

label scene6:
    g "Something strange has been going on."


    return
