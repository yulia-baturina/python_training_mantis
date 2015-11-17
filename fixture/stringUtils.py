__author__ = 'IEUser'
import random
import string


class StringsHelper:

    def randomstring(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
