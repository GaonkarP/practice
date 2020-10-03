import os
import sys
import requests
import hashlib


def check_response(sha_head):
  apiurl = 'https://api.pwnedpasswords.com/range/' + sha_head

  response = requests.get(apiurl)
  if response.status_code != 200:
    raise RuntimeError(f"error in validating url: {response.status_code}, check the input api")

  return response

def split_hash_count(response, sha_tail):
  response = (line.split(':') for line in response.text.splitlines())
  print(response)
  for hash, count in response:
    if hash == sha_tail:
      return count
  return 0

def hash_password(password="password123145"):
  shapassword = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
  sha_head, sha_tail = shapassword[:5], shapassword[5:]

  response = check_response(sha_head)
  count = split_hash_count(response, sha_tail)
  if count != 0:
    print(f"our password is leaked for {count} times")

  else:
    print(f"password is not leaked. Go ahead and use it")


def main():

    cwd = os.getcwd()
    print(cwd)

    args = sys.argv[1:]
    hash_password()

    print("done")


if __name__ == "__main__":
    sys.exit(main())
