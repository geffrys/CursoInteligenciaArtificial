import random 
import numpy as np

def get_genres():
    return genre_db

def get_moods():
    return mood_db

# Definimos la base de datos de canciones
songs_db = [
    {"id": 1, "genre": "rock", "mood": "melancholic", "name": "Bohemian Rhapsody", "artist": "Queen"},
    {"id": 2, "genre": "rock", "mood": "energetic", "name": "Highway to Hell", "artist": "AC/DC"},
    {"id": 3, "genre": "rock", "mood": "angry", "name": "Killing in the Name", "artist": "Rage Against the Machine"},
    {"id": 4, "genre": "rock", "mood": "party", "name": "Don't Stop Believin'", "artist": "Journey"},
    {"id": 5, "genre": "rock", "mood": "happy", "name": "Here Comes the Sun", "artist": "The Beatles"},
    {"id": 6, "genre": "rock", "mood": "relaxed", "name": "Wish You Were Here", "artist": "Pink Floyd"},
    {"id": 7, "genre": "rock", "mood": "romantic", "name": "Sweet Child O' Mine", "artist": "Guns N' Roses"},
    {"id": 8, "genre": "rock", "mood": "chill", "name": "Hotel California", "artist": "Eagles"},
    {"id": 9, "genre": "pop", "mood": "happy", "name": "Dancing Queen", "artist": "ABBA"},
    {"id": 10, "genre": "pop", "mood": "sad", "name": "Someone Like You", "artist": "Adele"},
    {"id": 11, "genre": "pop", "mood": "melancholic", "name": "Yesterday", "artist": "The Beatles"},
    {"id": 12, "genre": "pop", "mood": "angry", "name": "Bad Guy", "artist": "Billie Eilish"},
    {"id": 13, "genre": "pop", "mood": "relaxed", "name": "Someone You Loved", "artist": "Lewis Capaldi"},
    {"id": 14, "genre": "pop", "mood": "energetic", "name": "Blinding Lights", "artist": "The Weeknd"},
    {"id": 15, "genre": "pop", "mood": "romantic", "name": "Love Story", "artist": "Taylor Swift"},
    {"id": 16, "genre": "pop", "mood": "chill", "name": "Watermelon Sugar", "artist": "Harry Styles"},
    {"id": 17, "genre": "reggaeton", "mood": "happy", "name": "Dákiti", "artist": "Bad Bunny, Jhay Cortez"},
    {"id": 18, "genre": "reggaeton", "mood": "sad", "name": "Hasta Que Dios Diga", "artist": "Anuel AA, Bad Bunny"},
    {"id": 19, "genre": "reggaeton", "mood": "melancholic", "name": "La Noche de Anoche", "artist": "Bad Bunny, Rosalía"},
    {"id": 20, "genre": "reggaeton", "mood": "angry", "name": "Yo Perreo Sola", "artist": "Bad Bunny"},
    {"id": 21, "genre": "reggaeton", "mood": "relaxed", "name": "Relación - Remix", "artist": "Sech, Daddy Yankee, J Balvin, Rosalía, Farruko"},
    {"id": 22, "genre": "reggaeton", "mood": "energetic", "name": "Safaera", "artist": "Bad Bunny, Jowell & Randy, Ñengo Flow"},
    {"id": 23, "genre": "reggaeton", "mood": "romantic", "name": "La Modelo", "artist": "Ozuna, Cardi B"},
    {"id": 24, "genre": "reggaeton", "mood": "chill", "name": "Soy Peor", "artist": "Bad Bunny"},
    {"id": 25, "genre": "rap", "mood": "happy", "name": "Good Life", "artist": "Kanye West, T-Pain"},
    {"id": 26, "genre": "rap", "mood": "sad", "name": "Lucid Dreams", "artist": "Juice WRLD"},
    {"id": 27, "genre": "rap", "mood": "melancholic", "name": "Changes", "artist": "2Pac"},
    {"id": 28, "genre": "rap", "mood": "angry", "name": "m.A.A.d city", "artist": "Kendrick Lamar"},
    {"id": 29, "genre": "rap", "mood": "relaxed", "name": "Gin and Juice", "artist": "Snoop Dogg"},
    {"id": 30, "genre": "rap", "mood": "energetic", "name": "SICKO MODE", "artist": "Travis Scott"},
    {"id": 31, "genre": "rap", "mood": "romantic", "name": "Love The Way You Lie", "artist": "Eminem, Rihanna"},
    {"id": 32, "genre": "rap", "mood": "chill", "name": "SAD!", "artist": "XXXTENTACION"},
    {"id": 65, "genre": "rock", "mood": "happy", "name": "Livin' on a Prayer", "artist": "Bon Jovi"},
    {"id": 66, "genre": "rock", "mood": "sad", "name": "Nothing Else Matters", "artist": "Metallica"},
    {"id": 67, "genre": "pop", "mood": "party", "name": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars"},
    {"id": 68, "genre": "pop", "mood": "chill", "name": "Shape of You", "artist": "Ed Sheeran"},
    {"id": 69, "genre": "reggaeton", "mood": "party", "name": "Tusa", "artist": "KAROL G, Nicki Minaj"},
    {"id": 70, "genre": "reggaeton", "mood": "relaxed", "name": "Caramelo", "artist": "Ozuna"},
    {"id": 71, "genre": "rap", "mood": "energetic", "name": "Lose Yourself", "artist": "Eminem"},
    {"id": 72, "genre": "rap", "mood": "chill", "name": "God's Plan", "artist": "Drake"},
    {"id": 73, "genre": "rock", "mood": "romantic", "name": "I Don't Want to Miss a Thing", "artist": "Aerosmith"},
    {"id": 74, "genre": "pop", "mood": "romantic", "name": "Perfect", "artist": "Ed Sheeran"},
    {"id": 75, "genre": "reggaeton", "mood": "happy", "name": "Baila Baila Baila", "artist": "Ozuna"},
    {"id": 76, "genre": "rap", "mood": "melancholic", "name": "Mockingbird", "artist": "Eminem"},
    {"id": 77, "genre": "rock", "mood": "angry", "name": "Smells Like Teen Spirit", "artist": "Nirvana"},
    {"id": 78, "genre": "pop", "mood": "sad", "name": "Stay", "artist": "Rihanna ft. Mikky Ekko"},
    {"id": 79, "genre": "reggaeton", "mood": "angry", "name": "Te Boté", "artist": "Nio Garcia, Casper Magico, Bad Bunny, Nicky Jam, Ozuna"},
    {"id": 80, "genre": "rap", "mood": "happy", "name": "Hotline Bling", "artist": "Drake"}
]
# Definimos la base de datos de los mood
mood_db = [
    {"id": 1, "name": "happy"},
    {"id": 2, "name": "sad"},
    {"id": 3, "name": "melancholic"},
    {"id": 4, "name": "angry"},
    {"id": 5, "name": "relaxed"},
    {"id": 6, "name": "energetic"},
    {"id": 7, "name": "romantic"},
    {"id": 8, "name": "chill"},
    {"id": 9, "name": "party"}
]

genre_db = [
    {"id": 1, "name": "rock"},
    {"id": 2, "name": "pop"},
    {"id": 3, "name": "reggaeton"},
    {"id": 4, "name": "rap"}
]

# Función para generar una población inicial
def generate_population(pop_size: int):
    population = []
    for _ in range(pop_size):
        playlist = random.sample(songs_db, 3)  # Cada individuo es una lista de 3 canciones
        population.append(playlist)
    return population

# Función de evaluación (fitness function)
def evaluate_playlist(playlist, prefered_genre: str, mood: str):
    score = 0
    for song in playlist:
        if song["genre"] == prefered_genre:
            score += 1  # menor peso para el género preferido
        if song["mood"] == mood:
            score += 2  # mayor peso para el estado de ánimo
    print(f"EVALUACION: Playlist: {playlist}, Score: {score}")
    return score

# Selección de las mejores playlists
def select_best_playlists(population, prefered_genre, mood, num_best=2):
    # Evaluar cada playlist
    scored_population = [(evaluate_playlist(p, prefered_genre, mood), p) for p in population]
    # Ordenar según el puntaje
    scored_population.sort(key=lambda x: x[0], reverse=True)
    # Retornar las mejores playlists
    return [p for _, p in scored_population[:num_best]]

# Cruce de playlists (crossover)
def crossover(playlist1, playlist2):
    crossover_point = len(playlist1) // 2
    child_playlist = playlist1[:crossover_point] + playlist2[crossover_point:]
    print(f"CRUZE: Playlist 1: {playlist1}, Playlist 2: {playlist2}, Child: {child_playlist}")
    return child_playlist

# Mutación de playlists
def mutate(playlist):
    if random.random() < 0.2:  # Probabilidad de mutación del 20%
        random_song = random.choice(songs_db)
        playlist[random.randint(0, len(playlist) - 1)] = random_song
    return playlist

# Función principal del algoritmo genético
def genetic_algorithm(prefered_genre: str, mood: str, generations=5, population_size=8):
    # Generar la población inicial
    population = generate_population(population_size)
    
    for generation in range(generations):
        # Seleccionar las mejores playlists
        best_playlists = select_best_playlists(population, prefered_genre, mood)
        
        # Crear nueva población a partir de crossover y mutación
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(best_playlists, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population  # Actualizar la población con la nueva generación
    print(f'LA POBLACION RESULTANTE DEL CROSSOVER Y LA MUTACION: {population}')
    # Retornar la mejor playlist después de todas las generaciones
    best_playlist = select_best_playlists(population, prefered_genre, mood, num_best=1)[0]
    return best_playlist