from src.admin import Movie
from src.bookings import Booking
from src.user import Users

def main():
    try: 
        print("--------------------------------------")
        print("Welcome to Mr_PK Movies")
        print("--------------------------------------")

        admin = Movie()
        user = Users()
        booking = Booking()


        while True:
            print("Select an Option: ")
            print("1. Admin Panel")
            print("2. User Panel")
            print("3. Movie Booking")
            print("4. Exit" )

            user_input = int(input("Enter your choice: "))

            if user_input == 1:
                print("Entering Admin Panel")

                print("--------------------------------------")
                print("Welcome to Mr_PK Movies")
                print("--------------------------------------")

                while True:
                    print("Select an Option: ")
                    print("1. Add New Movies")
                    print("2. Update the Movies")
                    print("3. Delete the Movies")
                    print("4. View all Movies")
                    print("5. Exit")

                    admin_choice = int(input("Enter your choice: "))

                    if admin_choice == 1:
                        admin.add_movie()
                    elif admin_choice == 2:
                        admin.update_movie()
                    elif admin_choice == 3:
                        admin.delete_movie()
                    elif admin_choice == 4:
                        admin.get_all_movies()
                    elif admin_choice == 5:
                        print("Exiting the admin Panel")
                        break
                    else:
                        print("Invalid Input, Use only 1,2,3,4,5")


            elif user_input == 2:
                print("Entering User Panel")

                print("--------------------------------------")
                print("Welcome to Mr_PK Movies")
                print("--------------------------------------")

                while True:
                    print("Select an Option: ")
                    print("1. Register the New user")
                    print("2. Find the user by email id")
                    print("3. Exit")

                    user_choice = int(input("Enter your choice: "))

                    if user_choice == 1:
                        user.register_user()
                    elif user_choice == 2:
                        user.get_user_by_email()
                    elif user_choice == 3:
                        print("Exiting the user Panel")
                        break
                    else:
                        print("Invalid Input, Use only 1,2,3")

                
            elif user_input == 3:
                print("Entering booking Panel")

                print("--------------------------------------")
                print("Welcome to Mr_PK Movies")
                print("--------------------------------------")

                while True:
                    print("Select an Option: ")
                    print("1. Book a ticket")
                    print("2. Cancel the booking")
                    print("3. View the bookings")
                    print("4. Exit")

                    user_option = int(input("Enter your choice: "))

                    if user_option == 1:
                        booking.book_ticket()
                    elif user_option == 2:
                        booking.cancel_booking()
                    elif user_option == 3:
                        booking.view_user_bookings() 
                    elif user_option == 4:
                        print("Exiting the booking Panel")
                        break
                    else:
                        print("Invalid Input, Use only 1,2,3,4")


            elif user_input == 4:
                print("Exiting the Main Panel")
                break
            
            else:
                print("Invalid Input, Use only 1,2,3,4")


    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()