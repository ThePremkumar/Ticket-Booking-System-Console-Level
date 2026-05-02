from src.database import sql_executor

class Movie:
    #--- Add a New Movie ---

    def add_movie(self):
        try:
            print("--- Add a New Movie ---")
            movie_name = input("Enter the Movie Name: ")
            genre = input("Enter the Genre: ")
            show_time = input("Enter the Show Time (e.g., 7 PM): ")
            available_seats= int(input("Enter Number of Available Seats: "))
            
            query = f"INSERT INTO Movies (title, genre, show_time, available_seats) VALUES (?, ?, ?, ?)"
            data = (movie_name, genre, show_time, available_seats)

            sql_executor(query, data)
            print(f"\nSuccess: '{movie_name}' has been added to the database!")

            if type(available_seats) == str:
                raise ValueError("Error: Seats must be a number (e.g., 50).")
            
        except Exception as error:
            print(error)


#--- Update Movies ---
    def update_movie(self):
        try:
            self.get_all_movies()

            movie_id = int(input("Enter the movie id to update: "))

            print("What do you want to update?")
            print("1. Title")
            print("2. Genre")
            print("3. Show Time")
            print("4. Available Seats")
            choice = int(input("Enter choice: "))

            if choice == 1:
                new_title = input("Enter the New title: ")
                query = 'UPDATE movies SET title = ? WHERE movie_id = ?'
                sql_executor(query, (new_title, movie_id))
                print(f"\nSuccessfully updated movie ID {movie_id}. New title: {new_title}")

            elif choice == 2:
                new_genre = input("Enter the New Genre: ")
                query = 'UPDATE movies SET genre = ? WHERE movie_id = ?'
                sql_executor(query, (new_genre, movie_id))
                print(f"\nSuccessfully updated movie ID {movie_id}. New title: {new_genre}")

            elif choice == 3:
                new_show_time = input("Enter the New Show time: ")
                query = 'UPDATE movies SET show_time = ? WHERE movie_id = ?'
                sql_executor(query, (new_show_time, movie_id))
                print(f"\nSuccessfully updated movie ID {movie_id}. New title: {new_show_time}")

            elif choice == 4:
                new_available_seats = int(input("Enter the New Availabel seats: "))
                query = 'UPDATE movies SET available_seats = ? WHERE movie_id = ?'
                sql_executor(query, (new_available_seats, movie_id))
                print(f"\nSuccessfully updated movie ID {movie_id}. New title: {new_available_seats}")
            
            else:
                print("Invalid choice.")

        except Exception as error:
            print(error)


#--- Delete Movie ---

    def delete_movie(self):
        try:
            self.get_all_movies()

            query = 'DELETE FROM movies WHERE movie_id = ?'
            movie_id = int(input("Enter the movie id to delete: "))
            
            sql_executor(query, (movie_id,))
            print(f"\nSuccess: '{movie_id}' has been delete in the database!")
            
        except Exception as error:
            print(error)



    #--- Update a Movie ---
    def get_all_movies(self):
        try:
            print("\n--- All Movies ---")

            query = 'SELECT movie_id, title, genre, show_time, available_seats FROM movies'

            result = sql_executor(query, fetch=True)

            if not result:
                print("No movies found.")
                return

            for movie in result:
                print(movie)
        
        except Exception as error:
            print(error)


if __name__ == '__main__':
    movies=Movie()
    movies.add_movie()
    movies.get_all_movies()
    movies.delete_movie()
    movies.update_movie()