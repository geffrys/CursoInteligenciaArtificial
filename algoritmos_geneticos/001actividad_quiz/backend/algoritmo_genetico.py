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
    {"id": 33, "genre": "rock", "mood": "melancholic", "name": "Bohemian Rhapsody", "artist": "Queen"},
    {"id": 34, "genre": "rock", "mood": "energetic", "name": "Highway to Hell", "artist": "AC/DC"},
    {"id": 35, "genre": "rock", "mood": "angry", "name": "Killing in the Name", "artist": "Rage Against the Machine"},
    {"id": 36, "genre": "rock", "mood": "party", "name": "Don't Stop Believin'", "artist": "Journey"},
    {"id": 37, "genre": "rock", "mood": "happy", "name": "Here Comes the Sun", "artist": "The Beatles"},
    {"id": 38, "genre": "rock", "mood": "relaxed", "name": "Wish You Were Here", "artist": "Pink Floyd"},
    {"id": 39, "genre": "rock", "mood": "romantic", "name": "Sweet Child O' Mine", "artist": "Guns N' Roses"},
    {"id": 40, "genre": "rock", "mood": "chill", "name": "Hotel California", "artist": "Eagles"},
    {"id": 41, "genre": "pop", "mood": "happy", "name": "Dancing Queen", "artist": "ABBA"},
    {"id": 42, "genre": "pop", "mood": "sad", "name": "Someone Like You", "artist": "Adele"},
    {"id": 43, "genre": "pop", "mood": "melancholic", "name": "Yesterday", "artist": "The Beatles"},
    {"id": 44, "genre": "pop", "mood": "angry", "name": "Bad Guy", "artist": "Billie Eilish"},
    {"id": 45, "genre": "pop", "mood": "relaxed", "name": "Someone You Loved", "artist": "Lewis Capaldi"},
    {"id": 46, "genre": "pop", "mood": "energetic", "name": "Blinding Lights", "artist": "The Weeknd"},
    {"id": 47, "genre": "pop", "mood": "romantic", "name": "Love Story", "artist": "Taylor Swift"},
    {"id": 48, "genre": "pop", "mood": "chill", "name": "Watermelon Sugar", "artist": "Harry Styles"},
    {"id": 49, "genre": "reggaeton", "mood": "happy", "name": "Dákiti", "artist": "Bad Bunny, Jhay Cortez"},
    {"id": 50, "genre": "reggaeton", "mood": "sad", "name": "Hasta Que Dios Diga", "artist": "Anuel AA, Bad Bunny"},
    {"id": 51, "genre": "reggaeton", "mood": "melancholic", "name": "La Noche de Anoche", "artist": "Bad Bunny, Rosalía"},
    {"id": 52, "genre": "reggaeton", "mood": "angry", "name": "Yo Perreo Sola", "artist": "Bad Bunny"},
    {"id": 53, "genre": "reggaeton", "mood": "relaxed", "name": "Relación - Remix", "artist": "Sech, Daddy Yankee, J Balvin, Rosalía, Farruko"},
    {"id": 54, "genre": "reggaeton", "mood": "energetic", "name": "Safaera", "artist": "Bad Bunny, Jowell & Randy, Ñengo Flow"},
    {"id": 55, "genre": "reggaeton", "mood": "romantic", "name": "La Modelo", "artist": "Ozuna, Cardi B"},
    {"id": 56, "genre": "reggaeton", "mood": "chill", "name": "Soy Peor", "artist": "Bad Bunny"},
    {"id": 57, "genre": "rap", "mood": "happy", "name": "Good Life", "artist": "Kanye West, T-Pain"},
    {"id": 58, "genre": "rap", "mood": "sad", "name": "Lucid Dreams", "artist": "Juice WRLD"},
    {"id": 59, "genre": "rap", "mood": "melancholic", "name": "Changes", "artist": "2Pac"},
    {"id": 60, "genre": "rap", "mood": "angry", "name": "m.A.A.d city", "artist": "Kendrick Lamar"},
    {"id": 61, "genre": "rap", "mood": "relaxed", "name": "Gin and Juice", "artist": "Snoop Dogg"},
    {"id": 62, "genre": "rap", "mood": "energetic", "name": "SICKO MODE", "artist": "Travis Scott"},
    {"id": 63, "genre": "rap", "mood": "romantic", "name": "Love The Way You Lie", "artist": "Eminem, Rihanna"},
    {"id": 64, "genre": "rap", "mood": "chill", "name": "SAD!", "artist": "XXXTENTACION"}
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
            score += 1  # Prioridad alta para el género preferido
        if song["mood"] == mood:
            score += 2  # Menor peso para el estado de ánimo
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
    if random.random() < 0.1:  # Probabilidad de mutación del 10%
        random_song = random.choice(songs_db)
        playlist[random.randint(0, len(playlist) - 1)] = random_song
    return playlist

# Función principal del algoritmo genético
def genetic_algorithm(prefered_genre: str, mood: str, generations=5, population_size=6):
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