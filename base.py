import openai
import os
from promptlabs import create_client, Client
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
promptlabs: Client = create_client(api_key=os.environ.get("PROMPTLABS_API_KEY"))

