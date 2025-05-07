from openai import OpenAI

def ask_gpt(api_key: str, system_prompt: str, user_prompt: str, model: str = "gpt-4o", temperature: float = 0.7):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content