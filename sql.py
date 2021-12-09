insert_movie = ('''
    TODO
''')

create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl2;
''')

insert_ml = ('''
    INSERT INTO petl2.movie_list 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
''')

create_table = ('''
    CREATE TABLE IF NOT EXISTS petl2.movie_list(
        title text,
        rated text,
        released date,
        runtime integer,
        genre text[],
        director text,
        writers text[],
        actors text[],
        plot text,
        awards text,
        poster text
    );
''')