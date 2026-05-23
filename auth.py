from fastapi import Request, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from database import SUPABASE_URL

security = HTTPBearer()

jwks_client = jwt.PyJWKClient(f"{SUPABASE_URL}/auth/v1/.well-known/jwks.json")


async def auth_middleware(request: Request, call_next):
    """Read JWT from access_token cookie and inject it into the Authorization header."""
    token = request.cookies.get('access_token')

    if token and token.startswith('Bearer '):
        token = token.split(' ')[1]

        request.headers.__dict__['_list'].append(
            (b"authorization", f"Bearer {token}".encode())
        )

    response = await call_next(request)

    return response


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Decode and verify the JWT from the Authorization header using Supabase JWKS."""
    try:
        token = credentials.credentials

        if token.startswith('Bearer '):
            token = token.split(' ')[1]

        signing_key = jwks_client.get_signing_key_from_jwt(token)
        payload = jwt.decode(
            token,
            signing_key,
            algorithms=['ES256'],
            options={'verify_aud': False}
        )

        user_id = payload.get('sub')

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid auth creds'
            )

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token has expired'
        )

    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate user'
        )
