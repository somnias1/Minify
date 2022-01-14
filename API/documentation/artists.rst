========================
    Resource Artists
========================

resource POST
------------

    .. http:post:: /api/artists/

    Creates an artists

    * **Required fields**

        :Authorization (HEADER): **(token)** JWT admin Token
        :artist_name: **(string)** Name of the artist
        :description: **(string)** Description of the artist
        :origin: **(int)** Id of the origin country, see countries for more


    * **Optional fields**

        :language: **(string)** Artist's language, can be instrumental

    * **Sample request**

        .. host:: http

            POST /api/artists/
            Authorization: Bearer JWTtype.access.token
            Content-Type: json

            {
                "artist_name": "My artist",
                "description": "First artist in my country",
                "origin": 1,
                "language": "Spanish"
            }   

    * **Sample response**

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "id": 1,
                "artist_name": "My artist",
                "language": "Spanish"
                "description": "First artist in my country",
                "origin": {
                        "id": 1,
                        "country_name": "Colombia",
                        "country_image": null
                    },
            }  

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "artist_name": "This field is required."
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Authentication credentials were not provided."
            }

resource GET
-----------
    .. http:get:: /api/artists/

    Receives artistss

    * **Sample request**

        .. host:: http

            GET /api/artists/
            Content-Type: None

    * **Sample response**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            [
                {
                    "id": 1,
                    "artist_name": "My artist",
                    "language": "Spanish"
                    "description": "First artist in my country",
                    "origin": {
                            "id": 1,
                            "country_name": "Colombia",
                            "country_image": null
                        },
                }
            ]



    .. http:get:: /api/artists/<pk>

    Gets specific artists

    * **Sample request**

        .. host:: http

            GET /api/artists/1
            Content-Type: None

    * **Sample response**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "id": 1,
                    "artist_name": "My artist",
                    "language": "Spanish"
                    "description": "First artist in my country",
                    "origin": {
                            "id": 1,
                            "country_name": "Colombia",
                            "country_image": null
                        },
            }  

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "Not found."
            }

resource DELETE
--------------

    .. http:delete:: /api/artists/<pk>

    Deletes specific artists

    * **Sample request**

        .. host:: http

            DELETE /api/artists/1
            Authorization: Bearer JWTtype.access.token
            Content-Type: None

    * **Sample response**

        .. host:: http

            HTTP/1.1 204 NO CONTENT
            Content-Type: None

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Authentication credentials were not provided."
            }

            HTTP/1.1 403 FORBIDDEN
            Content-Type: json

            {
                "detail": "You do not have permission to perform this action."
            }

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "Not found."
            }

resource PATCH
-------------

    .. http:patch:: /api/artists/<pk>/

    Partially updates an artist

    * **Optional fields**

        :artist_name: **(string)** Name of the artist
        :description: **(string)** Description of the artist
        :origin: **(int)** Id of the origin country, see countries for more
        :language: **(string)** Artist's language, can be instrumental


    * **Sample request**

        .. host:: http

            PATCH /api/artists/1/
            Authorization: Bearer JWTtype.access.token
            Content-Type: json

            {
                "artist_name": "My favorite artist"
            }

    * **Sample response**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "artist_name": "My favorite artist",
                "language": "Spanish",
                "description": "First artist in my country",
                "origin": 1
            } 

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Authentication credentials were not provided."
            }

            HTTP/1.1 403 FORBIDDEN
            Content-Type: json

            {
                "detail": "You do not have permission to perform this action."
            }

            HTTP/1.1 404 NOT FOUND
                Content-Type: json

                {
                    "detail": "Not found."
                }

resource PUT
-----------

    .. http:put:: /api/artists/<pk>/

    Updates the artist entirely

    * **Required fields**

        :artist_name: **(string)** Name of the artist
        :description: **(string)** Description of the artist
        :origin: **(int)** Id of the origin country, see countries for more

    * **Optional fields**

        :language: **(string)** Artist's language, can be instrumental

    * **Sample request**

        .. host:: http

            PUT /api/artists/1/
            Authorization: Bearer JWTtype.access.token
            Content-Type: json

            {
                "artist_name": "My artist",
                "language": "English",
                "description": "First artist in my city",
                "origin": 1
                
            } 

    * **Sample response**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "artist_name": "My artist",
                "language": "English",
                "description": "First artist in my city",
                "origin": 1
                
            } 

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "field": "This field is required"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Authentication credentials were not provided."
            }

            HTTP/1.1 403 FORBIDDEN
            Content-Type: json

            {
                "detail": "You do not have permission to perform this action."
            }

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "Not found"
            }


:status 200: Request completed
:status 201: artists created
:status 204: artists deleted
:status 400: Wrong values
:status 401: Invalid token
:status 403: Not enough permissions
:status 404: artists not found