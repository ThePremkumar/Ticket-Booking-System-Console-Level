from src.database import sql_executor
class Users:
    def register_user(self):
        try:
            name = input("Enter your name: ")
            email = input("Enter your email id: ")

            query = "INSERT INTO users (name, email) VALUES (?, ?)"
            data = (name, email)

            sql_executor(query, data)
            print(f"\nSuccess: '{name}' has been added to the database!")
        except Exception as error:
            print(error)

    def get_user_by_email(self):
        try:
            print("\n--- All Users ---")
            email = input("Enter email to search: ")
            query = 'SELECT user_id, name, email FROM users WHERE email = ?'

            result = sql_executor(query,(email,), fetch=True)

            if not result:
                print("No users found.")
                return

            for user in result:
                print(user)
        
        except Exception as error:
            print(error)



        
if __name__ == '__main__':
    user=Users()
    # user.register_user()
    user.get_user_by_email()
    # sql_executor("DELETE FROM Users WHERE user_id = 1")