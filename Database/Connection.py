import pymongo
import bcrypt
from bson import ObjectId

CURR_CLIENT_VERSION = '1.0.0'
INTENDED_CLIENT_VERSION = None

client = pymongo.MongoClient("mongodb+srv://admin:karsen1212@cluster0.te0zc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# print(f'{client.list_database_names()}')

PROJECT_DATABASE = client.get_database("myFirstDatabase")
USER_COLLECTION = PROJECT_DATABASE.get_collection("users")
CLIENT_COLLECTION = PROJECT_DATABASE.get_collection('client')

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

    # print(f'found_user: {raw_user}')

    for element in raw_user:
        found_user = element

    if not found_user:
        print(f'Failed to find user.')
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


# Update the users licenses in the DB and local data
def update_user_licenses(user_email, new_license_arr):
    print(f'Updating {user_email} document with new_license_arr of length: {len(new_license_arr)}')

    # Update db user data
    user_query = {'email': user_email}
    update_license_query = {'$set': {'licenses': new_license_arr}}
    update_result = USER_COLLECTION.update_one(user_query, update_license_query)
    # Update local user data
    AUTHED_USER.licenses = new_license_arr

    print(f'Updated: {update_result.modified_count} document(s) license arrays.')
    return


def check_client_version():
    global INTENDED_CLIENT_VERSION

    version_doc_id = '6446282118f8e42ac6a14979'
    objInstance = ObjectId(version_doc_id)

    client_version_query = {"_id": objInstance}

    raw_client_doc = CLIENT_COLLECTION.find(client_version_query)

    print(f'raw_client_doc: {raw_client_doc}')

    for element in raw_client_doc:
        print(f'element: {element}')
        found_client_doc = element

    if found_client_doc:
        INTENDED_CLIENT_VERSION = found_client_doc.get('client_version')
        print(f'intended version: {INTENDED_CLIENT_VERSION}')
    else:
        print(f'Failed to fetch intended version.')

    if CURR_CLIENT_VERSION != INTENDED_CLIENT_VERSION:
        print(f'Client requires an update!')
        return False
    else:
        print(f'Client is up to date with latest version.')
        return True


def get_intended_version():
    return INTENDED_CLIENT_VERSION


def get_authed_user():
    return AUTHED_USER