import os
import wget
from dotenv import load_dotenv

load_dotenv()

file_url = 'https://raw.githubusercontent.com/thaiminhnguyen1999/potcoder/main/src/potcoder/potcoder-ver.txt'

try:
    wget.download(file_url, 'potcoder-ver.txt')
except Exception as e:
    print(f"Error downloading the file: {e}")
    exit(1)

with open("potcoder-ver.txt", "r") as file:
    data = file.read()

if data == os.getenv("POTCODER-VERSION"):
    print(f"\nYou are using the latest version of potcoder [v{os.getenv('POTCODER-VERSION')}]")
else:
    print(f"\nInstalling new potcoder version [v{data}]")
    os.system("git clone -b v" + data + " https://github.com/thaiminhnguyen1999/potcoder.git")
    os.system("cd potcoder")
    os.system("pip install potcoder-" + data + "-py3-none-any.whl")
