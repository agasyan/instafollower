import os
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
    for i in arr_of_targets_follower:
        print(i)
