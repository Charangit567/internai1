import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def process_with_llm(search_results, entity):
    prompt = f"Extract the email address of {entity} from the following:\n\n"
    for result in search_results:
        prompt += f"- {result['snippet']}\n"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50,
        temperature=0.5
    )
    return response.choices[0].text.strip()
