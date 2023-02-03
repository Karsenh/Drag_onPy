import subprocess
import os
import pymongo
from Connection import USER_COLLECTION


def update_user_hwid(curr_user):
    global user_collection

    user_query = {"email": curr_user.email}

    curr_hwid = get_curr_hwid()

    if not curr_user.hwid:
        # Save current HWID to their user doc
        print(f'No HWID found for current user... Saving HWID: {curr_hwid} to user with email: {curr_user.email}')
        update_query = {"$set": {"hwid": curr_hwid}}
        user_collection.update_one(user_query, update_query)
    return


def get_curr_hwid():
    hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    return hwid

# print(f'Get id: {get_hwid()}')


