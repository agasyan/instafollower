# instafollower
Get same follower from some acc, i open this project to particapate in hacktoberfest. This project is for fun to know public instagram follower from several instagram account. Anyone can contribute anything to make this project better and better :)

## Setup
How to run the project locally

### Running Program
In order to run this repo, you need to:

1. Clone the repo
2. Navigate to the project's folder on Terminal/Cmd
3. Install requirements with `pip install -r requirements.txt`
4. Set environment variable with `.env` file
```
IG_USERNAME=[YOUR_IG_USERNAME]
IG_PASSWORD=[YOUR_IG_PASS]
TARGET_IG="FOO BAR"
```
`TARGET_IG` is target to get instagram list of account to check the same follower seperated by space
5. run the program with `python3 main.py`


***

### Reference:
* https://stackoverflow.com/questions/37658723/how-to-get-followers-and-following-list-in-instagram-via-http-requests
