import bcrypt
import hashlib


def hash(password: str):
# 1. Pre-hash the password using SHA-256
    pre_hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
# 2. Hash the resulting 64-byte string with bcrypt
    hashed = bcrypt.hashpw(pre_hashed.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")

def verify_password(plain_password, hash_password):
    prehashed = hashlib.sha256(plain_password.encode("utf-8")).hexdigest()
    return bcrypt.checkpw(prehashed.encode("utf-8"), hash_password.encode("utf-8"))