from models import  Movies, MovieCreate 


def create_conntection():
    connection = sqlite3.connect('movies.db')
    connection.row_factory = sqlite3.Row
    return connection

def create_tables():
    connection = create_conntection()
    cursor = connection.cursor()
    cursor.execute('''
        create table if not exists movies (
            id integer primary key autoincrement,
                   title text not null,
                   director text not null
                   date text not null
                   )
                   ''')
    
    connection.commit()
    connection.close()



def add_movie(movie: MovieCreate) -> int:
    connection = create_conntection()
    cursor = connection.cursor()
    cursor.execute('''
                   insert into movies ( title, director) values ( ?, ?)
                   ''', (movie.title, movie.director))
    connection.commit()
    movie_id = cursor.lastrowid
    connection.close()
    return movie_id



def read_movies() -> list[Movies]:
    connection = create_conntection()
    cursor = connection.cursor()
    cursor.execute(''' select * from movies''')
    rows = cursor.fetchall()
    connection.close()
    movies = [Movies(id=row[0], title=row[1], director=row[2], date=row[3]) for row in rows]
    return movies

def read_movie(movie_id: int):
    connection = create_conntection()
    cursor = connection.cursor()
    cursor.execute(''' select from * movies where id = ?''', (movie_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return Movies(id=row['id'], title=row['title'], director=row['director'], date=row['date'])


def update_movie(movie_id: int, movie: MovieCreate) -> bool:
    connection = create_conntection()
    cursor = connection.cursor()
    cursor.execute (''' update movies set title = ?, director = ?, date = ? where id = ?''', (movie.title, movie.director, movie.date, movie_id))
    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()
    return updated


def delete_movie(movie_id: int) -> bool:
    connection = create_conntection()
    cursor = connection.cursor()
    cursor.execute ('delete from movies where id = ?', (movie_id))
    connection.commit()
    connection.close()
    return delete_movie > 0     

