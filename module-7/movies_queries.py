import mysql.connector

# Connect to the MySQL movies database
db = mysql.connector.connect(
    host="localhost",
    user="root",             
    password="Nitika1994",  
    database="movies"        
)

cursor = db.cursor()

# Query 1: All fields for the studio table
print("-- DISPLAYING Studio RECORDS --")
cursor.execute("SELECT studio_id, studio_name FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print(f"Studio ID: {studio[0]}")
    print(f"Studio Name: {studio[1]}\n")

# Query 2: All fields for the genre table
print("-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT genre_id, genre_name FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print(f"Genre ID: {genre[0]}")
    print(f"Genre Name: {genre[1]}\n")

# Query 3: Movies with runtime less than two hours
print("-- DISPLAYING Short Film RECORDS --")
cursor.execute("SELECT movie_name, runtime FROM movie WHERE runtime < 120")
short_films = cursor.fetchall()
for film in short_films:
    print(f"Film Name: {film[0]}")
    print(f"Runtime: {film[1]}\n")

# Query 4: Movies grouped by director
print("-- DISPLAYING Director RECORDS in Order --")
cursor.execute("SELECT director, movie_name FROM movie ORDER BY director")
director_movies = cursor.fetchall()
for director, movie in director_movies:
    print(f"Film Name: {movie}")
    print(f"Director: {director}\n")

# Close the database connection
db.close()
