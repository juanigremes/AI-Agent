import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import *

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

    function_results = []

    if response.function_calls != None:
        for function_call in response.function_calls:
            #print(f"Calling function: {function_call.name}({function_call.args})")

            if args.verbose:
                f_call_res = call_function(function_call, verbose=True)
            else:
                f_call_res = call_function(function_call)

            parts = f_call_res.parts
            if parts == []:
                raise Exception("types.Content object \"f_call_res\" has an empty .parts list")
            parts_function_response = parts[0].function_response
            if parts_function_response == None:
                raise Exception(".parts[0].function_response is None")
            parts_function_response_response = parts_function_response.response
            if parts_function_response_response == None:
                raise Exception("response is None")

            function_results.append(parts[0])

            if args.verbose :
                print(f"-> {f_call_res.parts[0].function_response.response}")
    else:
        print(response.text)



def interact_with_gemini(client, messages):
    response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],
                                               system_instruction=system_prompt)
            )
    if response.usage_metadata == None:
        raise RuntimeError("response's usage metadata is None, failed API request")
    return response


# call to main() func
main()
