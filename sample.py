import os

# load_env
from dotenv import load_dotenv

load_dotenv(verbose=True)

if __name__ == "__main__":
    print(os.getenv("COBA"))
    print(os.getenv("GOPATH"))