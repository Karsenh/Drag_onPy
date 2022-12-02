import pymongo
import bcrypt
from Database.Hwid import get_hwid


client = pymongo.MongoClient("mongodb+srv://admin:karsen1212@cluster0.te0zc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(f'{client.list_database_names()}')

project_database = client.get_database("myFirstDatabase")
user_collection = project_database.get_collection("users")


def get_user(email, password):
    user_query = {"email": email}

    searched_user = user_collection.find(user_query)

    i = 0

    for data in searched_user:
        i += 1
        user_data = data
        print(f'Found data: {i} - {data}')

    # email_var = searched_user[0].get("email")
    print(f'user_data: {user_data.get("email")}')

    encoded_user_pass = user_data.get("password").encode('utf8')
    # Get HWID of curr user
    user_hwid = user_data.get("hwid")

    print(f'Fetched users HWID: {user_hwid}')

    is_pass_matching = bcrypt.checkpw(password.encode('utf8'), encoded_user_pass)

    print(f'Do passwords match? {is_pass_matching}')

    # If the password is matching...
    if is_pass_matching:
        # But, if the curr user doesn't have HWID in their user doc...
        curr_hwid = get_hwid()

        if not user_hwid:
            # Save current HWID to their user doc
            print(f'No HWID found for current user... Saving HWID: {curr_hwid} to user with email: {email}')
            update_query = { "$set": { "hwid": curr_hwid}}
            user_collection.update_one(user_query, update_query)
            return True
        else:
            # Otherwise, the user DOES have HWID associated with their account - check if it's the same as current hwid
            if user_hwid == curr_hwid:
                print(f'✅ user_hwid matches curr_hwid')
                return True
            else:
                print(f'⛔ user_hwid does NOT match curr_hwid - Only one system is registered to use this application.')
                return False

    else:
        return False
