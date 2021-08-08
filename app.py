from utils.util_funcs import get_followers, get_followings, get_who_never_follow_back, get_whom_i_never_follow_back, unfollow_user, follow_user

if __name__ == "__main__":
    followers = get_followers()
    print("-------------------------------------------------------------")
    following = get_followings()

    print("-------------------------------------------------------------")
    who_never_follow_back = get_who_never_follow_back(
        following=following, followers=followers)

    print('There are {who_never_follow_back_length} user who never follow you back'.format(
        who_never_follow_back_length=len(who_never_follow_back)))

    print("-------------------------------------------------------------")
    print("Unfollowing those who never follow you back...")
    for user in who_never_follow_back:
        unfollow_user(user['login'])

    print("-------------------------------------------------------------")
    whom_i_never_follow_back = get_whom_i_never_follow_back(
        following=following, followers=followers)

    print('There are {whom_i_never_follow_back_length} user whom I never follow back'.format(
        whom_i_never_follow_back_length=len(whom_i_never_follow_back)))

    print("-------------------------------------------------------------")
    print("Following those whom I never follow back...")
    for user in whom_i_never_follow_back:
        follow_user(user['login'])
