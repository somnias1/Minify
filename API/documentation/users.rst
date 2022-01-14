========================
    Resource Users
========================

Resource LOGIN
--------------

    .. http:post:: /API/users/login/

    Logs with users credentials

    * **Required fields**

        :username: **(string)** Username previously registered
        :password: **(string)** password used in registration

    * **Sample request**

        .. host:: http

            POST /API/users/login/
            Content-Type: json

            {
                "username": "minifyuser1",
                "password": "minifyuser"
            }

    * **Sample response** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "user": {
                        "id":11,
                        "username": "minifyuser1",
                        "email": "minify@user1.com",
                        "signup_date": "2022-01-10",
                        "birth_date": "1998-06-06",
                        "membership": 1,
                        "queue": 11,
                        "last_login": "2022-01-11T01:30:27.460745"
                },
                "refresh": "JWTtype.refresh.token",
                "access": "JWTtype.access.token"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "non_field_errors": [
                    "Incorrect credentials"
                ]
            }

Resource SIGNUP
---------------

    .. http:post:: /API/users/signup/

    Registration form for the user

    * **Required fields**

        :username: **(string)** Username, bust be unique
        :password: **(string)** Password, requires strength
        :password_confirmation: **(string)** Password verification
        :birth_date: **(date)** Birth date, format recommended YYYY-MM-DD
        :email: **(email)** Email format required

    * **Sample request**

        .. host:: http

            POST /API/users/signup/
            Content-Type: json

            {
                "username": "minifyuser1",
                "password": "minifyuser1",
                "password_confirmation": "minifyuser1",
                "birth_date": "1998-06-06",
                "email": "minify@user1.com"
            }

    * **Sample response** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "user": {
                    "id": 11,
                    "username": "usuario",
                    "email": "email@usuario.com",
                    "signup_date": "2022-01-10",
                    "birth_date": "1998-06-06",
                    "membership": 1,
                    "queue": 11
                },
                "refresh": "JWTtype.refresh.token",
                "access": "JWTtype.access.token"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "username": [
                    "This field must be unique."
                ],
                "email": [
                    "This field must be unique."
                ]
            }  


Resource TOKEN
--------------

    .. http:post:: /api/token/

    Request token for the user

    * **Required fields**

        :username: **(string)** Username previously registered
        :password: **(string)** password used in registration

    * **Sample request**

        .. host:: http

            POST /API/token/
            Content-Type: json

            {
                "username": "minifyuser1",
                "password": "minifyuser"
            }

    * **Sample response** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "refresh": "JWTtype.refresh.token",
                "access": "JWTtype.access.token"
            }

Resource REFRESH TOKEN
----------------------

    .. http:post:: /api/token/refresh/

    Refresh token for the user

    * **Required fields**

        :refresh: **(JWTToken)** JWT refresh token

    * **Sample request**

        .. host:: http

            POST /API/token/refresh/
            Content-Type: json

            {
                "refresh": JWTtype.refresh.token
            }

    * **Sample response** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "access": "JWTtype.access.token"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Token is invalid or expired",
                "code": "token_not_valid"
            }



:status 200: Request complete
:status 201: User created
:status 400: Invalid values
:status 401: Authorization Token invalid or expired