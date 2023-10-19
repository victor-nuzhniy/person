"""Schemas module for 'api' app."""
from drf_yasg import openapi

swagger_user_register_schema = openapi.Schema(
    title="Create user.",
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(
            type=openapi.TYPE_INTEGER, description="User id", example=1
        ),
        "email": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="User email. Required. Unique.",
            example="ex@example.com",
        ),
        "first_name": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="User first name.",
            example="Alex",
        ),
        "last_name": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="User last name.",
            example="Alan",
        ),
        "team": openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description="Team id to join. Can be blank.",
            example=1,
        ),
        "password": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="User password.",
            example="111",
        ),
    },
    required=["email", "password"],
)


swagger_user_schema = openapi.Schema(
    title="User operations.",
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(
            type=openapi.TYPE_INTEGER, description="User id", example=1
        ),
        "email": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="User email. Required. Unique.",
            example="ex@example.com",
        ),
        "first_name": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="User first name.",
            example="Alex",
        ),
        "last_name": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="User last name.",
            example="Alan",
        ),
        "team": openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description="Team id to join. Can be blank.",
            example=1,
        ),
    },
    required=["email"],
)


swagger_put_responses = {
    200: "Operation successfully performed.",
    400: "Validation errors.",
    401: "Unauthorized.",
    403: "You don't have permission to perform this action.",
    404: "Object not found.",
    415: "Invalid format.",
}


swagger_get_responses = {
    200: "Operation successfully performed.",
    401: "Unauthorized.",
    403: "You don't have permission to perform this action.",
    404: "Object not found.",
}


swagger_post_responses = {
    201: "Object successfully created.",
    400: "Validation errors.",
    401: "Unauthorized.",
    403: "You don't have permission to perform this action.",
    404: "Object not found.",
    415: "Invalid format.",
}


swagger_delete_responses = {
    204: "Operation successfully performed.",
    401: "Unauthorized.",
    403: "You don't have permission to perform this action.",
    404: "Object not found.",
}


swagger_team_schema = openapi.Schema(
    title="Team operations.",
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(
            type=openapi.TYPE_INTEGER, description="Team id", example=1
        ),
        "name": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="Team name.",
            example="Bad girls",
        ),
    },
)
