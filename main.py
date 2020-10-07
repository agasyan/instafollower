import os
import copy
import instaloader

# load_env
from dotenv import load_dotenv

load_dotenv(verbose=True)

if __name__ == "__main__":
    list_target = os.environ.get("TARGET_IG").split(" ")
    user = os.getenv("IG_USERNAME")
    password = os.getenv("IG_PASSWORD")
    # Get instance
    L = instaloader.Instaloader()

    # Login or load session to see some public ig follower or private followed ig
    L.login(user, password)
    arr_of_targets_follower = []
    for target in list_target:
        arr = []
        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, target)
        # Print list of followees
        counter = 0
        # followee to profile.get_followees() who the target follow and profile.get_followers to get target follower
        for follower in profile.get_followers():
            counter = counter + 1
            print(str(counter) + ":" + follower.username)
            arr.append(follower.username)
        arr_of_targets_follower.append(arr)
    # Same checker
    arr_copy_tmp = copy.copy(arr_of_targets_follower)
    arr_copy_tmp.pop(0)
    ans = []
    counter = 1
    for i in range(len(arr_of_targets_follower[0])):
        print("counter:" + str(i))
        temp = arr_of_targets_follower[0][i]
        checker = []
        for elem in arr_copy_tmp:
            if temp in elem:
                checker.append(True)
            else:
                checker.append(False)
        if not (False in checker):
            ans.append(temp)
        counter += 1
    print(ans)
    print(len(ans))
