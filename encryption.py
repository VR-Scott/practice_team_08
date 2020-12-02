import bcrypt

def encrypt_password(password):
    """
    Encrypt a password with a randomly generated salt then a hash.
    :param password: The password to encrypt in clear text.
    :return: The encrypted password as a unicode string.
    """
    encoded_password = password.encode('utf8')
    cost_rounds = 4
    random_salt = bcrypt.gensalt(cost_rounds)
    hashed_password = bcrypt.hashpw(encoded_password, random_salt).decode('utf8', 'strict')
    return hashed_password


def check_password(password, password_hash):
    """
    Check a password against its encrypted hash for a match.
    :param password: the password to check in clear text. (Unicode)
    :param password_hash: The encrypted hash to check against. (Unicode)
    :return: Whether the password and the hash match
    """
    encoded_password = password.encode('utf8')
    encoded_password_hash = password_hash.encode('utf8')
    password_matches = bcrypt.checkpw(encoded_password, encoded_password_hash)
    return password_matches


if __name__ == '__main__':
    test_password = 'doobeedoo'
    hashed_test_password = encrypt_password(test_password)
    print(f'hashed_password: {hashed_test_password}')
    password_matches_hash = check_password(test_password, hashed_test_password)
    print(f'password matches hash? {password_matches_hash}')