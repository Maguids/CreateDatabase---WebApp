import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from flask import render_template, Flask
import logging
import db

APP = Flask(__name__)

# Start page
@APP.route('/')
def index():
    stats = {}
    stats = db.execute('''
    SELECT * FROM
    (SELECT COUNT(*) n_movies FROM MOVIE)
    JOIN 
    (SELECT COUNT(*) n_characters FROM Character)
    JOIN
    (SELECT COUNT(*) n_actors FROM ACTOR)
    JOIN 
    (SELECT COUNT(*) n_directors FROM Director)
    JOIN
    (SELECT COUNT(*) n_genres FROM GENRE)
    ''').fetchone()
    logging.info(stats)
    return render_template('index.html',stats=stats)

# ----------------------------------------SEARCH PAGE----------------------------------------

@APP.route('/search/')
def search():
    return render_template('search_list.html')


# ----------------------------------------MOVIES----------------------------------------

# MOVIES TABLE
# function that lists all movies with all its attributes from its table
@APP.route('/movies/')
def list_movies():
    movies = db.execute(
        '''
        SELECT IdMovie, Name, "Date of Release" as ReleaseDate, Gross, IdDirector 
        FROM Movie
        ORDER BY Name
        ''').fetchall()
    
    # in order to not have problems with the overlap
    search_movie = None
    search = {'expr' : None}

    return render_template('movie_list.html', movies=movies, search=search, search_movie=search_movie)

# MOVIE - SEARCH NAME
# function that allows to search for movies by its NAME within the 'movie_list.html'
@APP.route('/movies/name/<expr>/')
def name_get_movie(expr):
    search = { 'expr': expr, 'type': 'name' }
    expr = '%' + expr + '%'

    search_movie = db.execute(
        ''' 
        SELECT IdMovie, Name,"Date of Release" as ReleaseDate
        FROM MOVIE 
        WHERE Name LIKE ?
        ''', [expr]).fetchall()
    
    movies = db.execute(
        '''
        SELECT IdMovie, Name, "Date of Release" as ReleaseDate, Gross, IdDirector 
        FROM Movie
        ORDER BY Name
        ''').fetchall()
    
    return render_template('movie_list.html', search=search, search_movie=search_movie, movies=movies)

# MOVIE - SEARCH YEAR
# function that allows to search for movies by its RELEASE YEAR within the 'movie_list.html'
@APP.route('/movies/year/<expr>/') 
def year_get_movie(expr):
    if (len(expr) == 4):
        search = { 'expr': expr, 'type': 'year' }
        expr = '%' + expr

        search_movie = db.execute(
            ''' 
            SELECT IdMovie, Name, "Date of Release" as ReleaseDate
            FROM MOVIE 
            WHERE ReleaseDate LIKE ?
            ''', [expr]).fetchall()
    else:
        search = { 'expr': expr, 'type': 'year' }
        search_movie = ""
        
    movies = db.execute(
        '''
        SELECT IdMovie, Name, "Date of Release" as ReleaseDate, Gross, IdDirector 
        FROM Movie
        ORDER BY Name
        ''').fetchall()
    
    return render_template('movie_list.html', search=search, search_movie=search_movie, movies=movies)

# MOVIE - SEARCH ID
# function that allows to search for movies by its ID within the 'movie_list.html'
@APP.route('/movies/id/<int:expr>/')
def id_get_movie(expr):
    search = { 'expr': expr, 'type': 'id' }

    search_movie = db.execute(
        ''' 
        SELECT IdMovie, Name, "Date of Release" as ReleaseDate
        FROM MOVIE 
        WHERE IdMovie == ?
        ''', [expr]).fetchall()
    
    movies = db.execute(
        '''
        SELECT IdMovie, Name, "Date of Release" as ReleaseDate, Gross, IdDirector 
        FROM Movie
        ORDER BY IdMovie
        ''').fetchall()
    
    return render_template('movie_list.html', search=search, search_movie=search_movie, movies=movies)

# MOVIE INFO
# function that allows to search for a movie from its Id and show all its info
@APP.route('/movies/info/<int:id>/')
def info_movie(id):
    movie = db.execute(
        '''
        SELECT IdMovie, Name, "Date of Release" as ReleaseDate, Gross,IdDirector 
        FROM Movie
        WHERE IdMovie = ?
        ''', [id]).fetchone()

    directors = db.execute(
        '''
        SELECT d.IdDirector, d.Name as n_d, d.Gender
        FROM MOVIE m
            JOIN DIRECTOR d ON m.IdDirector = d.IdDirector
        WHERE m.IdMovie = ? 
        ORDER BY d.Name;
        ''', [id]).fetchall()

    character_actor = db.execute(
        '''
        SELECT a.Name AS n_A, a.IdActor AS id_A, c.Name AS n_C, c.IdCharacter AS id_C
        FROM Actor a 
            JOIN Character c ON a.IdActor=c.IdActor
            JOIN Movie m on c.IdMovie=m.IdMovie
        WHERE m.IdMovie = ?
        ''', [id]).fetchall()
  
    genres = db.execute(
        '''
        SELECT g.IdGenre, g.Name
        FROM Movie m
            JOIN GenresOfMovies gm ON m.IdMovie = gm.IdMovie
            JOIN Genre g ON gm.IdGenre = g.IdGenre
        WHERE m.IdMovie = ?
        ''', [id]).fetchall()

    return render_template('movie.html', movie=movie, directors=directors, character_actor=character_actor, genres = genres)


# ----------------------------------------CHARACTERS----------------------------------------

# CHARACTERES TABLE
# function that lists all characters with all its attributes from its table
@APP.route('/characters/')
def list_characters():
    characters = db.execute(
        '''
        SELECT IdCharacter, Name, Species, Role, IdMovie, IdActor
        FROM Character
        ORDER BY IdCharacter
        ''').fetchall()

    # in order to not have problems with the overlap
    search_characters = None
    search = {'expr' : None}

    return render_template('character_list.html', characters = characters, search_characters = search_characters, search = search)

# CHARACTERS - SEARCH NAME
# function that allows to search for characters by its NAME within the 'character_list.html'
@APP.route('/characters/name/<expr>/')
def name_get_character(expr):
    search = {'expr' : expr, 'type': 'name'}
    expr = '%' + expr + '%'

    search_characters = db.execute(
        '''
        SELECT IdCharacter, Name
        FROM Character
        WHERE Name LIKE ?
        ''', [expr]).fetchall()
    
    # in order to not have problems with the overlap
    characters = db.execute(
        '''
        SELECT IdCharacter, Name, Species, Role, IdMovie, IdActor
        FROM Character
        ORDER BY IdCharacter
        ''').fetchall()

    return render_template('character_list.html', search_characters = search_characters, search = search, characters = characters)

# CHARACTERS - SEARCH ID 
# function that allows to search for characters by its ID within the 'character_list.html'
@APP.route('/characters/id/<int:expr>/')
def id_get_character(expr):
    search = {'expr' : expr, 'type': 'id'}

    search_characters = db.execute(
        '''
        SELECT IdCharacter, Name
        FROM Character
        WHERE IdCharacter == ?
        ''', [expr]).fetchall()
    
    # in order to not have problems with the overlap
    characters = db.execute(
        '''
        SELECT IdCharacter, Name, Species, Role, IdMovie, IdActor
        FROM Character
        ORDER BY IdCharacter
        ''').fetchall()

    return render_template('character_list.html', search_characters = search_characters, search = search, characters = characters)

# CHARACTERS INFO
# function that allows to search for a character from its Id and show all its info
@APP.route('/characters/info/<int:id>/')
def info_character(id):
    # get charcater's specific atributes (Id, Name, Species and Role)
    character = db.execute(
        '''
        SELECT IdCharacter, Name, Species, Role
        FROM Character
        WHERE IdCharacter = ?
        ''', [id]).fetchone()

    # get the Id and Name of the actor that makes the voice of the character
    actor = db.execute(
        '''
        SELECT a.IdActor, a.Name
        FROM Character c
            JOIN Actor a ON c.IdActor = a.IdActor
        WHERE c.IdCharacter = ?
        ''', [id]).fetchone()
    
    # get the name of the movie where the character belongs to
    movie = db.execute(
        '''
        SELECT m.Name, m.IdMovie
        FROM Character c
            JOIN Movie m ON c.IdMovie = m.IdMovie
        WHERE IdCharacter = ?
        ''', [id]).fetchone()
    
    return render_template('character.html', character = character, actor = actor, movie = movie)


# ----------------------------------------ACTORS----------------------------------------

# ACTORS TABLE
# function that lists all actors with all its attributes from its table
@APP.route('/actors/')
def list_actors():
    actors = db.execute(
        '''
        SELECT IdActor, Name, Gender
        FROM Actor
        ORDER BY IdActor
        ''').fetchall()

    search_actors = None
    search = {'expr' : None}

    return render_template('actor_list.html', actors = actors, search_actors = search_actors, search = search)

# ACTORS - SEARCH NAME
# function that allows to search for actors by its NAME within the 'actor_list.html'
@APP.route('/actors/name/<expr>/')
def name_get_actor(expr):
    search = {'expr' : expr, 'type': 'name'}
    expr = '%' + expr + '%'

    search_actors = db.execute(
        '''
        SELECT IdActor, Name
        FROM Actor
        WHERE Name LIKE ?
        ''', [expr]).fetchall()
    
    # in order to not have problems with the overlap
    actors = db.execute(
        '''
        SELECT IdActor, Name, Gender
        FROM Actor
        ORDER BY IdActor
        ''').fetchall()

    return render_template('actor_list.html', search_actors = search_actors, search = search, actors = actors)

# ACTORS - SEARCH ID
# function that allows to search for actors by its ID within the 'actor_list.html'
@APP.route('/actors/id/<int:expr>/')
def id_get_actor(expr):
    search = {'expr' : expr, 'type': 'id'}

    search_actors = db.execute(
        '''
        SELECT IdActor, Name
        FROM Actor
        WHERE IdActor == ?
        ''', [expr]).fetchall()
    
    # in order to not have problems with the overlap
    actors = db.execute(
        '''
        SELECT IdActor, Name, Gender
        FROM Actor
        ORDER BY IdActor
        ''').fetchall()

    return render_template('actor_list.html', search_actors = search_actors, search = search, actors = actors)

# ACTORS INFO
# function that allows to search for a actor from its Id and show all its info
@APP.route('/actors/info/<int:id>/')
def info_actor(id):
    # get actor's specific atributes (Id, Name and Gender)
    actor = db.execute(
        '''
        SELECT IdActor, Name, Gender
        FROM Actor
        WHERE IdActor = ?
        ''', [id]).fetchone()
    
    # get the name of the movie/movies where the actor belongs to and the character/characters 
    character_movie = db.execute(
        '''
        SELECT m.Name AS n_m, m.IdMovie AS id_m, c.Name AS n_c, c.IdCharacter AS id_c
        FROM Actor a
            JOIN Character c ON a.IdActor = c.IdActor
            JOIN Movie m ON c.IdMovie = m.IdMovie
        WHERE a.IdActor = ?
        ''', [id]).fetchall()
    
    return render_template('actor.html', actor = actor, character_movie = character_movie)


# ----------------------------------------DIRECTORS----------------------------------------

# DIRECTORS TABLE
# function that lists all directors with all its attributes from its table
@APP.route('/directors/')
def list_directors():
    directors = db.execute(
        '''
        SELECT IdDirector, Name, Gender 
        FROM Director
        ORDER BY Name
        ''').fetchall()
    
    # in order to not have problems with the overlap
    search_director = None
    search = {'expr' : None}

    return render_template('director_list.html', directors=directors, search_director=search_director, search=search)


# DIRECTORES - SEARCH NAME
# function that allows to search for directors by its NAME within the 'director_list.html'
@APP.route('/directors/name/<expr>/')
def name_get_director(expr):
    search = { 'expr': expr, 'type': 'name'}
    expr = '%' + expr + '%'

    search_director = db.execute(
        ''' 
        SELECT IdDirector, Name
        FROM director 
        WHERE Name LIKE ?
        ''', [expr]).fetchall()
  
    # in order to not have problems with the overlap
    directors = db.execute(
        '''
        SELECT IdDirector, Name, Gender
        FROM Director
        ORDER BY IdDirector
        ''').fetchall()
  
    return render_template('director_list.html', search=search, search_director=search_director, directors=directors)


# DIRECTORES - SEARCH ID
# function that allows to search for directors by its ID within the 'director_list.html'
@APP.route('/directors/id/<expr>/')
def id_get_director(expr):
    search = { 'expr': expr, 'type': 'id'}

    search_director = db.execute(
        ''' 
        SELECT IdDirector, Name
        FROM director 
        WHERE IdDirector == ?
        ''', [expr]).fetchall()
    
    # in order to not have problems with the overlap
    directors = db.execute(
        '''
        SELECT IdDirector, Name, Gender
        FROM Director
        ORDER BY IdDirector
        ''').fetchall()
    
    return render_template('director_list.html', search=search, search_director=search_director, directors=directors)


# DIRECTORES INFO
# function that allows to search for a director from its Id and show all its info
@APP.route('/directors/info/<int:id>/')
def info_director(id):
    director = db.execute(
        '''
        SELECT IdDirector, Name, Gender 
        FROM Director
        WHERE IdDirector = ?
        ''', [id]).fetchone()


    movies = db.execute(
        '''
        SELECT m.name,IdMovie
        FROM MOVIE m
        JOIN DIRECTOR d ON m.IdDirector = d.IdDirector
        WHERE m.IdDirector = ? 
        ORDER BY m.name;
        ''', [id]).fetchall()

    return render_template('director.html', movies=movies, director=director)


# ----------------------------------------GENRES----------------------------------------

# GENRES TABLE
# function that lists all genres with all its attributes from its table
@APP.route('/genres/')
def list_genres():
    genres = db.execute(
        '''
        SELECT IdGenre, Name, Description
        FROM genre
        ORDER BY IdGenre
        ''').fetchall()

    search_genres = None
    search = {'expr' : None}

    return render_template('genre_list.html', genres = genres, search_genres = search_genres, search = search)

# GENRES - SEARCH NAME
# function that allows to search for genres by its NAME within the 'genre_list.html'
@APP.route('/genres/name/<expr>/')
def name_get_genre(expr):
    search = {'expr' : expr, 'type': 'name'}
    expr = '%' + expr + '%'

    search_genres = db.execute(
        '''
        SELECT IdGenre, Name
        FROM genre
        WHERE Name LIKE ?
        ''', [expr]).fetchall()
    
    # in order to not have problems with the overlap
    genres = db.execute(
        '''
        SELECT IdGenre, Name, Description
        FROM Genre
        ORDER BY IdGenre
        ''').fetchall()

    return render_template('genre_list.html', search_genres = search_genres, search = search, genres = genres)

# GENRES - SEARCH ID
# function that allows to search for genres by its ID within the 'genre_list.html'
@APP.route('/genres/id/<int:expr>/')
def id_get_genre(expr):
    search = {'expr' : expr, 'type': 'id'}

    search_genres = db.execute(
        '''
        SELECT IdGenre, Name
        FROM Genre
        WHERE IdGenre == ?
        ''', [expr]).fetchall()
    
    # in order to not have problems with the overlap
    genres = db.execute(
        '''
        SELECT IdGenre, Name, Description
        FROM genre
        ORDER BY IdGenre
        ''').fetchall()

    return render_template('genre_list.html', search_genres = search_genres, search = search, genres = genres)

# GENRES INFO
# function that allows to search for a genre from its Id and show all its info
@APP.route('/genres/info/<int:id>/')
def info_genre(id):
    # get genre's specific atributes (Id, Name and description)
    genre = db.execute(
        '''
        SELECT IdGenre, Name, Description
        FROM Genre
        WHERE IdGenre = ?
        ''', [id]).fetchone()
    
    # get the name of the movie/movies where the genre belongs to 
    movie = db.execute(
        '''
       SELECT Name AS n_m, IdMovie AS id_m
       FROM Movie NATURAL JOIN GenresOfMovies
       WHERE IdGenre = ?
       ORDER BY n_m
        ''', [id]).fetchall()
    
    return render_template('genre.html', genre = genre, movie = movie)


# -------------------------------------------------------------------------------------
# ----------------------------------------EXTRA----------------------------------------
# -------------------------------------------------------------------------------------


# SPECIES INFO
@APP.route('/species/info/<expr>/')
def species_info(expr):
    search = expr

    species = db.execute(
        '''
        SELECT c.Name AS n_c, c.IdCharacter AS id_c, m.Name as n_m, m.IdMovie AS id_m
        FROM Character c
            JOIN Movie m ON c.IdMovie = m.IdMovie
        WHERE c.Species = ?
        ''', [expr]).fetchall()
    
    return render_template('species.html', search = search, species = species)

# ROLES INFO
@APP.route('/roles/info/<expr>/')
def roles_info(expr):
    search = expr

    roles = db.execute(
        '''
        SELECT c.Name AS n_c, c.IdCharacter AS id_c, m.Name as n_m, m.IdMovie AS id_m
        FROM Character c
            JOIN Movie m ON c.IdMovie = m.IdMovie
        WHERE c.Role = ?
        ''', [expr]).fetchall()
    
    return render_template('roles.html', search = search, roles = roles)

# MALE/FEMALE INFO
@APP.route('/gender/info/<expr>/')
def gender_info(expr):
    search = expr

    gender = db.execute(
        '''
        SELECT a.IdActor AS id, a.Name AS name, 'Actor' AS source
        FROM Actor a
        WHERE a.Gender = ?

        UNION

        SELECT d.IdDirector AS id, d.Name AS name,'Director' AS source
        FROM Director d
        WHERE d.Gender = ?
        ''', [expr, expr]).fetchall()
    
    return render_template('gender.html', search = search, gender = gender)
