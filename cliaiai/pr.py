import json
from json import JSONDecodeError

import click
from cliaiai.api import get_client


def execute(text, ):
    resp = get_client().chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are giving opinion about provided sourcecode diff"
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    try:
        response = json.loads(resp.choices[0].message.content)
        return (response["notes"], [solution for solution in response["solutions"]])
    except JSONDecodeError as e:
        click.echo(e.msg, err=True)
