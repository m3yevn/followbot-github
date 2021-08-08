import requests
import os

headers = {'Authorization': 'token {access_token}'.format(
    access_token=os.environ['TOKEN'])}


def get_followers():
    followers = []
    count = 1

    print('Fetching page {page}'.format(page=count))
    r = requests.get(
        'https://api.github.com/user/followers?page=1', headers=headers)
    result = r.json()
    followers = followers + result

    while len(result) != 0:
        count = count + 1
        print('Fetching page {page}'.format(page=count))
        r = requests.get(
            'https://api.github.com/user/followers?page={count}'.format(count=count), headers=headers)
        result = r.json()
        followers = followers + result

    print('There are {followers_length} followers'.format(
        followers_length=len(followers)))
    return followers


def get_followings():
    followings = []
    count = 1

    print('Fetching page {page}'.format(page=count))
    r = requests.get(
        'https://api.github.com/user/following?page=1', headers=headers)
    result = r.json()
    followings = followings + result

    while len(result) != 0:
        count = count + 1
        print('Fetching page {page}'.format(page=count))
        r = requests.get(
            'https://api.github.com/user/following?page={count}'.format(count=count), headers=headers)
        result = r.json()
        followings = followings + result

    print('There are {followings_length} followings'.format(
        followings_length=len(followings)))
    return followings


def get_who_never_follow_back(following=[], followers=[]):
    result = []
    follower_names = list(map(lambda x: x['login'], followers))
    for user in following:
        if user['login'] not in follower_names:
            result.append(user)
    return result


def get_whom_i_never_follow_back(following=[], followers=[]):
    result = []
    following_names = list(map(lambda x: x['login'], following))
    for user in followers:
        if user['login'] not in following_names:
            result.append(user)
    return result


def unfollow_user(username):
    requests.delete(
        'https://api.github.com/user/following/{username}'.format(username=username), headers=headers)
    print("Successfully unfollow {username}".format(username=username))


def follow_user(username):
    requests.put(
        'https://api.github.com/user/following/{username}'.format(username=username), headers=headers)
    print("Successfully follow {username}".format(username=username))
