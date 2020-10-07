import os
import instaloader

# load_env
from dotenv import load_dotenv

load_dotenv(verbose=True)

if __name__ == "__main__":
    list_target = [os.environ.get("TARGET_IG").split(" ")]
    user = os.getenv("IG_USERNAME")
    password = os.getenv("IG_PASSWORD")
    # Get instance
    L = instaloader.Instaloader()

    # Login or load session to see some public ig follower or private followed ig
    L.login(user, password)

    # Obtain profile metadata
    profile = instaloader.Profile.from_username(L.context, "agasyanp")

    # Print list of followees
    counter = 0
    # followee to profile.get_followees() who the target follow and profile.get_followers to get target follower
    for follower in profile.get_followers():
        counter = counter + 1
        print(counter + ":" + follower.username)
