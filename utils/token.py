import jwt
from datetime import timedelta, datetime

from conf.global_vars import JWT_SECRET


def create_access_token(user_id: int):
    to_encode = {
        "user_id": user_id,
        "exp": (datetime.now() + timedelta(days=1)).timestamp(),
    }
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm="HS256")
    return encoded_jwt
