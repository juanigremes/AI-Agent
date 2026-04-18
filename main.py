import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types




def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("api_key wasn't found")

    # Parser
    parser = argparse.ArgumentParser(description="Send cmd to my Agent")
    parser.add_argument("user_prompt", type=str, help="prompt help")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Messages
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Gemini Client Instance
    client = genai.Client(api_key=api_key)
    
    response = interact_with_gemini(client, messages)

    if args.verbose:
        print("User prompt: ",args.user_prompt)
        print("Prompt tokens: ",response.usage_metadata.prompt_token_count)
        print("Response tokens: ",response.usage_metadata.prompt_token_count) 

    print(response.text)




def interact_with_gemini(client, messages):
    response = client.models.generate_content(model='gemini-2.5-flash', contents=messages)
    if response.usage_metadata == None:
        raise RuntimeError("response's usage metadata is None, failed API request")
    return response


# call to main() func
main()
