import os

import openai
from openai import OpenAI


def get_client() -> OpenAI:
    # print(os.environ)
    match os.getenv('OPENAI_API_TYPE'):
        case 'azure':
            return openai.AzureOpenAI(
                api_key=os.getenv('OPENAI_APIKEY'),
                azure_endpoint=os.getenv('OPENAI_APIURL'),
                api_version='2023-03-15-preview',
                azure_deployment=os.getenv('OPENAI_DEPLOYMENT_NAME'),
            )
        case 'openai':
            return openai.Client(
                api_key=os.getenv('OPENAI_APIKEY'),
                base_url=os.getenv('OPENAI_APIURL')
            )
        case _ as other:
            raise ValueError(f"unknown type {other}")
