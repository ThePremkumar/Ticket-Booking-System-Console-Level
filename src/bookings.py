from database import sql_executor

from admin import Movie

class Booking:
    def book_ticket(self):
        try:
            Movie().get_all_movies()

            user_id = int(input("Enter your user ID: "))
            movie_id = int(input("Enter the movie id "))
        
            result = sql_executor('SELECT available_seats FROM Movies WHERE movie_id = ?', (movie_id,), fetch=True)
            if not result or result[0][0] < seats_booked:
                print("Not enough seats available.")
                return
            
            seats_booked = int(input("Enter the number of seats"))

            if seats_booked <= 0:
                raise ValueError("Seats must be at least 1.")
                
            
            query = 'INSERT INTO Bookings (user_id, movie_id, seats_booked) VALUES (?, ?, ?)'
            data = (user_id, movie_id, seats_booked)

            sql_executor(query, data)

        except Exception as error:
            print(error)

    def cancel_booking():
        try:
            user_id = int(input("Enter your user ID: "))
            movie_id = int(input("Enter the movie id to cancel the booking "))

            result = sql_executor('SELECT * FROM bookings WHERE user_id AND movie_id = ?', (user_id, movie_id,), fetch=True)

            if not result:
                    print("No booking found.")
                    return

            seats_booked = result[0][0]
            
            sql_executor('DELETE FROM bookings WHERE user_id = ? AND movie_id = ?', (user_id, movie_id))
            sql_executor('UPDATE movies SET available_seats = available_seats + ? WHERE movie_id = ?',(seats_booked, movie_id))

            print(f"\nSuccess: Booking cancelled and {seats_booked} seats restored!")

        except Exception as error:
            print(error)

    def view_user_bookings(self):
        try:
            user_id = int(input("Enter your user ID: "))
            result = sql_executor('SELECT * FROM bookings WHERE user_id = ?', (user_id,), fetch=True)

            if not result:
                print("No booking found.")
                return

            for booking in result:
                print(f"Booking ID: {booking[0]} | User ID: {booking[1]} | Movie ID: {booking[2]} | Seats: {booking[3]} | Time: {booking[4]}")

        except Exception as error:
            print(error)
        


if __name__ == "__main__":
    booking = Booking()
    booking.book_ticket()
    booking.cancel_booking()
    booking.view_user_bookings()
