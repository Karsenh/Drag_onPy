import pymongo
import bcrypt


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

    # index = 0
    # user = None
    #
    # for data in searched_user:
    #     index += 1
    #     user = data
    #     print(f'Data ▶ {data}\n')
    #
    # if index < 1:
    #     print(f'User not found.')
    #     return -1
    # else:
    #     # print(f'Found user for email: {email}')
    #     print(f'email_var: {email_var}')

    # print(f'email: {}')

    # db_pass = "pw-string123"
    # db_hashed_pass = bcrypt.hashpw(db_pass.encode('utf8'), bcrypt.gensalt())
    # print(f'Hashed pass to save in db: {db_hashed_pass}')
    is_pass_matching = bcrypt.checkpw(password.encode('utf8'), encoded_user_pass)

    print(f'Do passwords match? {is_pass_matching}')


    return
