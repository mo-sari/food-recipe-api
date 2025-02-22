## Authentication urls

#### Register

http://localhost:8000/auth/users/
you'll get an email after registeration, the link contains uid and a token, send them to

#### Account Activation

http://localhost:8000/auth/users/activation/?content-type=application/json

example:
{
"uid":"NQ",
"token":"clmpvz-f797f6d21e98302b56823d49c789cc96"
}

after activation was complete, you can log into your account

#### Login

http://localhost:8000/auth/jwt/create/?Content-Type=application/json

use your email and password

#### Refresh

http://localhost:8000/auth/jwt/refresh/?Content-Type=application/json

send the refresh token you recieved after login to this url to get a new access token

#### Reset Password

http://localhost:8000/auth/users/reset_password/

send your email to this url to get an email with a link for resetting the password

#### Reset Password Confirm

http://localhost:8000/auth/users/reset_password_confirm/?content-type=application/json

example:
{
"uid":"NQ",
"token":"clmq8a-acf59938474c6334481c728326b05bdd",
"new_password":"aaa???123"
}
