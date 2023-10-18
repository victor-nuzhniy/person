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
            type=openapi.TYPE_OBJECT,
            description="Team to join. Can be blank.",
            properties={
                "id": openapi.Schema(
                    type=openapi.TYPE_INTEGER, description="Team id", example=1
                ),
                "name": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Team name.",
                    example="Good fellas.",
                ),
            },
        ),
        "password": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="User password.",
            example="111",
        ),
    },
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
            type=openapi.TYPE_OBJECT,
            description="Team to join. Can be blank.",
            properties={
                "id": openapi.Schema(
                    type=openapi.TYPE_INTEGER, description="Team id", example=1
                ),
                "name": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Team name.",
                    example="Good fellas.",
                ),
            },
        ),
    },
)


swagger_user_responses = {
    200: "Operation successfully performed.",
    400: "Validation errors.",
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