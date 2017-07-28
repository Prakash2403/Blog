# Credit goes to https://gist.github.com/ndarville/3452907

import os


def get_secret_key(secret_file):
    try:
        secret_key = open(secret_file).read().strip()
        return secret_key
    except IOError:
        try:
            import random
            secret_key = ''.join(
                [random.SystemRandom()
                    .choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
                 for _ in range(50)])
            secret = open(secret_file, 'w')
            secret.write(secret_key)
            secret.close()
            return secret_key
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % secret_file)
