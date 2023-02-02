import pymongo
import bcrypt


client = pymongo.MongoClient("mongodb+srv://admin:karsen1212@cluster0.te0zc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# print(f'{client.list_database_names()}')

PROJECT_DATABASE = client.get_database("myFirstDatabase")
USER_COLLECTION = PROJECT_DATABASE.get_collection("users")

AUTHED_USER = None


class User:
    def __init__(self, email, licenses, hwid):
        self.email = email,
        self.licenses_arr = licenses
        self.hwid = hwid


def get_user(email, password):
    global AUTHED_USER

    user_query = {"email": email}

    raw_user = USER_COLLECTION.find(user_query)

    print(f'found_user: {raw_user}')

    for element in raw_user:
        found_user = element

    if not found_user:
        return False

    print_user_data(found_user)

    encoded_user_pass = found_user.get("password").encode('utf8')

    is_pass_matching = bcrypt.checkpw(password.encode('utf8'), encoded_user_pass)

    # If the password is matching...
    if is_pass_matching:
        AUTHED_USER = User(email=found_user.get('email'), licenses=found_user.get('licenses'), hwid=found_user.get('hwid'))
        print(f'🔓 Returning AUTHED_USER: {AUTHED_USER}')
        # But, if the curr user doesn't have HWID in their user doc...
        return AUTHED_USER
    else:
        return False


def print_user_data(user):
    i = 0
    for data in user:
        i += 1
        print(f'Found user attribute: {i} - {data}')
    return
