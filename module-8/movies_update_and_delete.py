import mysql.connector

# Connect to the MySQL movies database
db = mysql.connector.connect(
    host="localhost",
    user="root",             # Your MySQL username
    password="Nitika1994",   # Your MySQL password
    database="movies"        # The database name
)

cursor = db.cursor()

# Function to display films
def show_films(cursor, title):
    cursor.execute("""
        SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)
    films = cursor.fetchall()
    print(f"\n-- {title} --")
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre Name ID: {film[2]}")
        print(f"Studio Name: {film[3]}\n")

# Display initial films
show_films(cursor, "DISPLAYING FILMS")

# Insert a new record
cursor.execute("""
    INSERT INTO film (film_name, film_director, genre_id, studio_id)
    VALUES ('Star Wars', 'George Lucas', 2, 1)
""")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update a record
cursor.execute("""
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
""")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

# Delete a record
cursor.execute("""
    DELETE FROM film
    WHERE film_name = 'Gladiator'
""")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Close the database connection
db.close()
