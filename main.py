import os
from dotenv import load_dotenv
import sys
from functions.config import *
from functions.schemas import *
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types



def main():
    
    if len(sys.argv)>1:
        user_prompt = sys.argv[1]
        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
        verbose = False
        if len(sys.argv) > 2:
            if sys.argv[2]=="--verbose":
                verbose = True
        for i in range(20):
            try:
                response = client.models.generate_content(
                    model='gemini-2.0-flash-001', contents=messages,
                    config=types.GenerateContentConfig(
                        tools=[available_functions], system_instruction=system_prompt
                    )
                )
                for candidate in response.candidates:
                    messages.append(candidate.content)
                if response.function_calls:
                    for function_call_part in response.function_calls:
                        result = call_function(function_call_part,verbose)
                        messages.append(result)
                        function_response = result.parts[0].function_response.response # type: ignore
                else:
                    print(f"Final response: {response.text}")
                    break
            except Exception as e:
                print(f"Error:{e}")
                break

        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}") # type: ignore
        
    else:
        print("No input error")
        exit(1)

if __name__ == "__main__":
    main()