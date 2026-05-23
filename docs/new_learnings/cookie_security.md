# Cookie Security Flags

When storing a JWT in a browser cookie (e.g. after login), three flags protect it from common attacks.

## 1. `httponly=True`

Prevents JavaScript from accessing the cookie via `document.cookie`.

**What it blocks:** XSS (Cross-Site Scripting) attacks. Even if an attacker injects malicious JavaScript into your page, they cannot read the cookie value.

**Without it:** Any script running on the page can do `document.cookie` and steal the token.

## 2. `secure=True`

The cookie is only sent over HTTPS connections, never plain HTTP.

**What it blocks:** Network sniffing / man-in-the-middle attacks. An attacker monitoring unencrypted traffic (e.g. public Wi-Fi) cannot intercept the cookie.

**Without it:** The cookie is sent in cleartext over HTTP, visible to anyone on the same network.

**Note:** Set `secure=False` during local development (HTTP), and `secure=True` in production (HTTPS). We use `secure=not DEBUG` to handle this automatically.

## 3. `samesite='lax'`

The cookie is only sent with requests originating from the same site. It is included on top-level navigations (clicking a link) but not on cross-site POST requests or embedded resources.

**What it blocks:** CSRF (Cross-Site Request Forgery) attacks. A malicious site cannot trick the user's browser into making authenticated POST requests to your app.

**Options:**
- `'strict'` - cookie is never sent on cross-site requests (even clicking a link from another site)
- `'lax'` - cookie is sent on top-level navigations but not on cross-site form submissions (recommended)
- `'none'` - cookie is always sent (requires `secure=True`)

## Usage in this project

```python
response.set_cookie(
    key='access_token',
    value=f"Bearer {access_token}",
    httponly=True,       # block JavaScript access
    secure=not DEBUG,    # HTTPS only in production
    samesite='lax'       # block cross-site requests
)
```

Located in `routes/auth_routes.py`, inside the `POST /login` handler.
