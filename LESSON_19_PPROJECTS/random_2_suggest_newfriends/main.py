# Create a scenario where we use Python to implement a simplified version of suggestion NEW FRIENDS



# import the function and the array/list with the users, within the function that you importing , you are also importing the "suggested_user"
from helper import suggest_random_user, users

def main():
    #Simulating a current user (in real application, this could come from session or login)
    # this current_user_id is coming from the helper TOO
    current_user_id = 1 # Assuming current user is Alice with user ID 1


    # Suggesting 3 random users that the current user may know
    # If current_user_id is 1, then users[current_user_id - 1] means we're looking at the first user in the list (because computers start counting from 0, not 1).
    # :🟧 If the current user's ID is 2 (Mario), we want to ensure that Mario is excluded from the list of suggested friends. In programming, we typically start counting from 0 for the first element in a list, so users[current_user_id - 1] refers to the user at index current_user_id - 1 in the users list.
    print(f"Suggested friends for {users[current_user_id - 1]['name']}:")
    # This syntax (["name"]) is used because users[current_user_id - 1] returns a dictionary (a type of collection in Python), and dictionaries use keys to access their values.

    for i in range(3): # suggest 3 users
        #
        suggested_user = suggest_random_user(current_user_id)
        print(f"- {suggested_user['name']}")


if __name__ == "__main__":
    main()