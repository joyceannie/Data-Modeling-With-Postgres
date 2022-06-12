# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
                            songplay_id SERIAL PRIMARY KEY, 
                            start_time TIMESTAMP, 
                            user_id int, 
                            level VARCHAR NOT NULL, 
                            song_id int, 
                            artist_id VARCHAR, 
                            session_id INT NOT NULL, 
                            location VARCHAR, 
                            user_agent TEXT

)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
                        user_id int PRIMARY KEY, 
                        first_name VARCHAR NOT NULL, 
                        last_name VARCHAR NOT NULL, 
                        gender CHAR(1), 
                        level VARCHAR NOT NULL
)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
                        song_id VARCHAR PRIMARY KEY, 
                        title VARCHAR NOT NULL, 
                        artist_id VARCHAR NOT NULL, 
                        year int CHECK(year >= 0), 
                        duration numeric
)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
                          artist_id VARCHAR PRIMARY KEY, 
                          artist_name VARCHAR NOT NULL, 
                          location VARCHAR, 
                          latitude DECIMAL(9, 6), 
                          longitude DECIMAL(9, 6)
)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
                        start_time TIMESTAMP PRIMARY KEY, 
                        hour INT, 
                        day VARCHAR, 
                        week INT, 
                        month INT, 
                        year INT, 
                        weekday VARCHAR
)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT(songplay_id) DO NOTHING;
""")

user_table_insert = ("""INSERT INTO users VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""INSERT INTO songs VALUES ( %s, %s, %s, %s, %s)
                        ON CONFLICT(song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists VALUES (%s, %s, %s, %s, %s)
                          ON CONFLICT(artist_id) DO UPDATE SET location = EXCLUDED.location,
                                                               latitude = EXCLUDED.latitude,
                                                               longitude = EXCLUDED.longitude;
""")


time_table_insert = ("""INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT(start_time) DO NOTHING; 
""")

# FIND SONGS

song_select = ("""SELECT songs.title, artists.name
                  FROM songs JOIN artists
                  ON songs.artist_id = artists.artist_id
                  WHERE songs.title = %s AND
                        artists.artist_name = %s AND
                        songs.duration = %s;
                        
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]