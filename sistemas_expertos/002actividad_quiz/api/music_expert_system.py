import clips

env = clips.Environment()

moods = ["happy", "sad", "angry", "relaxed"]

genres = ["reggaeton", "electronic", "rock", "jazz", "classical", "pop", "metal", "hip-hop"]

def load_templates():
    try:
        env.build("""
        (deftemplate person (slot name) (slot prefered_genre) (slot mood))          
        """)
        env.build("""
        (deftemplate song (slot song_name) (slot genre) (slot artist) (slot mood))
        """)
    except clips.CLIPSError as e:
        print(f"Error al cargar templates: {e}")
        return False
    return True

def load_rules():
    try:
        RULE3 = """
            (defrule mood_sad_reggaeton 
                (person (name ?name) (prefered_genre "reggaeton") (mood "sad")) 
                => 
                (printout t "Rule mood_sad_reggaeton activated for " ?name crlf)
                (assert (song (song_name "Amorfoda") (genre "reggaeton") (artist "Bad Bunny") (mood "sad")))
            )
        """

        RULE4 = """
            (defrule mood_happy_electronic 
                (person (name ?name) (prefered_genre "electronic") (mood "happy")) 
                => 
                (printout t "Rule mood_happy_electronic activated for " ?name crlf)
                (assert (song (song_name "Titanium") (genre "electronic") (artist "David Guetta ft. Sia") (mood "happy")))
            )
        """

        RULE5 = """
            (defrule mood_angry_rock 
                (person (name ?name) (prefered_genre "rock") (mood "angry")) 
                => 
                (printout t "Rule mood_angry_rock activated for " ?name crlf)
                (assert (song (song_name "Killing In The Name") (genre "rock") (artist "Rage Against The Machine") (mood "angry")))
            )
        """

        RULE6 = """
            (defrule mood_relaxed_jazz 
                (person (name ?name) (prefered_genre "jazz") (mood "relaxed")) 
                => 
                (printout t "Rule mood_relaxed_jazz activated for " ?name crlf)
                (assert (song (song_name "So What") (genre "jazz") (artist "Miles Davis") (mood "relaxed")))
            )
        """

        RULE7 = """
            (defrule mood_sad_classical 
                (person (name ?name) (prefered_genre "classical") (mood "sad")) 
                => 
                (printout t "Rule mood_sad_classical activated for " ?name crlf)
                (assert (song (song_name "Moonlight Sonata") (genre "classical") (artist "Beethoven") (mood "sad")))
            )
        """
        RULE12 = """
            (defrule mood_happy_any_genre 
                (person (name ?name) (prefered_genre ?genre) (mood "happy")) 
                => 
                (printout t "Rule mood_happy_any_genre activated for " ?name crlf)
                (assert (song (song_name "Feel So Close") (genre ?genre) (artist "Calvin Harris") (mood "happy")))
            )
        """

        RULE13 = """
            (defrule mood_sad_any_genre 
                (person (name ?name) (prefered_genre ?genre) (mood "sad")) 
                => 
                (printout t "Rule mood_sad_any_genre activated for " ?name crlf)
                (assert (song (song_name "The Night We Met") (genre ?genre) (artist "Lord Huron") (mood "sad")))
            )
        """

        RULE14 = """
            (defrule mood_relaxed_any_genre 
                (person (name ?name) (prefered_genre ?genre) (mood "relaxed")) 
                => 
                (printout t "Rule mood_relaxed_any_genre activated for " ?name crlf)
                (assert (song (song_name "Ocean Eyes") (genre ?genre) (artist "Billie Eilish") (mood "relaxed")))
            )
        """

        RULE15 = """
            (defrule mood_angry_any_genre 
                (person (name ?name) (prefered_genre ?genre) (mood "angry")) 
                => 
                (printout t "Rule mood_angry_any_genre activated for " ?name crlf)
                (assert (song (song_name "Duality") (genre ?genre) (artist "Slipknot") (mood "angry")))
            )
        """
        RULE8 = """
            (defrule mood_happy_any 
                (person (name ?name) (mood "happy")) 
                => 
                (printout t "Rule mood_happy_any activated for " ?name crlf)
                (assert (song (song_name "Good Life") (genre "hip-hop") (artist "Kanye West ft. T-Pain") (mood "happy")))
            )
        """

        RULE9 = """
            (defrule mood_sad_any 
                (person (name ?name) (mood "sad")) 
                => 
                (printout t "Rule mood_sad_any activated for " ?name crlf)
                (assert (song (song_name "Someone Like You") (genre "pop") (artist "Adele") (mood "sad")))
            )
        """

        RULE10 = """
            (defrule mood_angry_any 
                (person (name ?name) (mood "angry")) 
                => 
                (printout t "Rule mood_angry_any activated for " ?name crlf)
                (assert (song (song_name "B.Y.O.B.") (genre "metal") (artist "System of a Down") (mood "angry")))
            )
        """

        RULE11 = """
            (defrule mood_relaxed_any 
                (person (name ?name) (mood "relaxed")) 
                => 
                (printout t "Rule mood_relaxed_any activated for " ?name crlf)
                (assert (song (song_name "Chill Bill") (genre "hip-hop") (artist "Rob $tone ft. J. Davi$ & Spooks") (mood "relaxed")))
            )
        """
        env.build(RULE15)
        env.build(RULE14)
        env.build(RULE13)
        env.build(RULE12)
        env.build(RULE11)
        env.build(RULE10)
        env.build(RULE9)
        env.build(RULE8)
        env.build(RULE7)
        env.build(RULE6)
        env.build(RULE5)
        env.build(RULE4)
        env.build(RULE3)
    except clips.CLIPSError as e:
        print(f"Error al cargar reglas: {e}")
        return False
    return True

def evaluacion(name: str, prefered_genre: str, mood: str):
    env.reset()
    preconditions()
    print("----- EVALUATION -----")
    factArray = []
    usuario = f"""
        (person (name \"{name}\") (prefered_genre \"{prefered_genre}\") (mood \"{mood}\"))
    """
    try:
        env.assert_string(usuario)
    except clips.CLIPSError as e:
        print(f"Error al asertar el hecho: {e}")
        return "Error"
    
    env.run()
    
    for fact in env.facts():
        fact_conditions = {slot.name: fact[slot.name] for slot in fact.template.slots}
        factArray.append({
            "fact_rule": fact.template.name,
            "fact_conditions": fact_conditions
        })
    factArray = factArray[1:]
    return factArray

def preconditions():
    print("----- PRINTING TEMPLATES -----")
    if load_templates():
        print("Templates loaded successfully.")
        for template in env.templates():
            print(f"Template: {template.name}")
            print(template)
    else:
        print("Failed to load templates.")
    
    print("----- PRINTING RULES -----")
    if load_rules():
        print("Rules loaded successfully.")
        for rule in env.rules():
            print(f"Rule: {rule.name}")
            print(rule)
    else:
        print("Failed to load rules.")

