import hashlib
import requests


def get_passwords():
    """ Get passwords from passwords.txt file """
    with open("./passwords.txt") as pw_file:
        return pw_file.read().split()


def password_to_hash(password):
    """ Convert the password to SHA1 hexadecimal hash """
    return hashlib.sha1(str(password).encode("utf-8")).hexdigest().upper()


def hash_splitter(hash):
    """ Split hash according to Pwned Passwords API """
    return {"prefix": hash[:5], "suffix": hash[5:]}


def api_password_search(prefix_hash):
    """ Pwned Passwords => Search by range """
    res = requests.get(
        f"https://api.pwnedpasswords.com/range/{prefix_hash}")

    if (res.status_code != requests.codes.ok):
        res.raise_for_status()

    return res.text.split()


def format_api_matches(api_matches):
    """ Return a list of [hash, count] pairs """
    return list(map(lambda a: a.split(":"), api_matches))


def compare_hashes(hashes_list, user_hash):
    """ Compare the hash suffixes between the API list and the password
        and return the coincidences """
    for hash_pair in hashes_list:
        if (hash_pair[0] == user_hash):
            # Returns the count
            return hash_pair[1]
    return 0


def main():
    user_passwords = get_passwords()
    for user_pw in user_passwords:
        hashed_pw = password_to_hash(user_pw)
        hashes_splitted = hash_splitter(hashed_pw)
        api_matches = api_password_search(hashes_splitted["prefix"])
        hashes_list = format_api_matches(api_matches)
        pw_matches = compare_hashes(hashes_list, hashes_splitted["suffix"])
        if (int(pw_matches) > 0):
            print(
                f'Alert! Your password "{user_pw}" has been leaked {pw_matches} times!')
        else:
            print(
                f'Good news, your password "{user_pw}" has not been leaked! :D')


main()
