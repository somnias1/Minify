========================
    Resource Endpoint
========================

resource POST
------------

    .. http:post:: /api/endpoint/

    Creates an object

    * **Required fields**

        :Authorization (HEADER): **(token)** JWT admin Token
        :field: **(type)** Field description


    * **Optional fields**

        :field: **(type)** Field description

    * **Sample request**

        .. host:: http

            POST /api/endpoint/
            Authorization: Bearer JWTtype.access.token
            Content-Type: json

            {
                "field": "Field content",
                "dictionary_list":
                [
                    {
                        "field_dict1":"Field of the first dictionary",
                    },
                    {
                        "field_dict2":"Field of the second dictionary",
                    }
                ]
            }   

    * **Sample response**

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "field": "Field content",
                "dictionary_list":
                [
                    {
                        "field_dict1":"Field of the first dictionary",
                    },
                    {
                        "field_dict2":"Field of the second dictionary",
                    }
                ]
            }  

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "field": "Wrong values for the field"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Authentication credentials were not provided."
            }

resource GET
-----------
    .. http:get:: /api/endpoint/

    Receives objects

    * **Sample request**

        .. host:: http

            GET /api/endpoint/
            Content-Type: None

    * **Sample response**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            [
                {
                    "id": 1,
                    "field": "Field content",
                    "dictionary_list":
                    [
                        {
                            "field_dict1":"Field of the first dictionary",
                        },
                        {
                            "field_dict2":"Field of the second dictionary",
                        }
                    ]
                }, 
                {
                    "id": 2,
                    "field": "Field content",
                    "dictionary_list":
                    [
                        {
                            "field_dict1":"Field of the first dictionary",
                        },
                        {
                            "field_dict2":"Field of the second dictionary",
                        }
                    ]
                }
            ]



    .. http:get:: /api/endpoint/<pk>

    Gets specific object

    * **Sample request**

        .. host:: http

            GET /api/endpoint/1
            Content-Type: None

    * **Sample response**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "field": "Field content",
                "dictionary_list":
                [
                    {
                        "field_dict1":"Field of the first dictionary",
                    },
                    {
                        "field_dict2":"Field of the second dictionary",
                    }
                ]
            }  

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "Not found."
            }

resource DELETE
--------------

    .. http:delete:: /api/endpoint/<pk>

    Deletes specific object

    * **Required fields**

            :field: **(type)** Field description


    * **Sample request**

        .. host:: http

            DELETE /api/endpoint/1
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
                "detail": "You don't have permissions for this action."
            }

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "Not found."
            }

resource PATCH
-------------

    .. http:patch:: /api/endpoint/<pk>/

    Updates object

    * **Required fields**

        :field: **(type)** Field description


    * **Optional fields**

        :field: **(type)** Field description

    * **Sample request**

        .. host:: http

            PATCH /api/endpoint/1/
            Authorization: Bearer JWTtype.access.token
            Content-Type: json

            {
                "field": "Updated field"
            }

    * **Sample response**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "field": "Updated field",
                "dictionary_list":
                [
                    {
                        "field_dict1":"Field of the first dictionary",
                    },
                    {
                        "field_dict2":"Field of the second dictionary",
                    }
                ]
            } 

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Authentication credentials were not provided."
            }

            HTTP/1.1 403 FORBIDDEN
            Content-Type: json

            {
                "detail": "You don't have enough permissions for this action."
            }

            HTTP/1.1 404 NOT FOUND
                Content-Type: json

                {
                    "detail": "Not found."
                }

resource PUT
-----------

    .. http:put:: /api/endpoint/<pk>/

    Updates the object entirely

    * **Required fields**

        :field1: **(field type)** Field1 description
        :field2: **(field type)** Field2 description

    * **Optional fields**

        :optfield: **(field type)** Optfield description

    * **Sample request**

        .. host:: http

            PUT /api/endpoint/1/
            Authorization: Bearer JWTtype.access.token
            Content-Type: json

            {
                "field1": "Updated field1",
                "field2": "Updated field2",
                
            } 

    * **Sample response**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "field1": "Updated field1",
                "field2": "Updated field2",
                
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
                "detail": "You don't have enough permissions for this action."
            }

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "Not found"
            }


:status 200: Request completed
:status 201: object created
:status 204: Object deleted
:status 400: Wrong values
:status 401: Invalid token
:status 403: Not enough permissions
:status 404: Object not found