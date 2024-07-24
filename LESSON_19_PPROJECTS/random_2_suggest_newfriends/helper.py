# Within the helper.py, I will define a function that generates random users or profiles

# This will simulate fetching friends or suggested connections

#
import random

users = [
    {"id": 1, "name": "Alice"},
      {"id": 2, "name": "Mario"},
       {"id": 3, "name": "Anastacia"}
]



#suggest_random_user(current_user_id): This function takes current_user_id as a parameter and suggests a random user from users excluding the current user. It uses random.choice to select a random user from other_users, which are all users except the current one.
def suggest_random_user(current_user_id):
    #
    # Exclude the current user from suggestions

    other_users = [user for user in users if user["id"] != current_user_id]




    suggested_user = random.choice(other_users)

    return suggested_user