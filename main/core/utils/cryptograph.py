import hashlib


def md5(data):
    data_hash = hashlib.md5()
    data_hash.update(str(data).encode('utf-8'))
    return str(data_hash.hexdigest())


def sha1(data):
    data_hash = hashlib.sha1()
    data_hash.update(str(data).encode('utf-8'))
    return str(data_hash.hexdigest())


def sha256(data):
    data_hash = hashlib.sha256()
    data_hash.update(str(data).encode('utf-8'))
    return str(data_hash.hexdigest())


def sha512(data):
    data_hash = hashlib.sha512()
    data_hash.update(str(data).encode('utf-8'))
    return str(data_hash.hexdigest())
