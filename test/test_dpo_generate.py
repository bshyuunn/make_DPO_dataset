import os
import sys

# Add parent directory to sys.path to allow importing util
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from util.gpt_utils import ask_gpt

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def generate_response(system_prompt_path, user_prompt_path, model="gpt-4o", temperature=0.7):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    system_prompt_path = os.path.join(script_dir, system_prompt_path)
    
    # Read system prompt file
    with open(system_prompt_path, 'r') as f:
        system_prompt = f.read().strip()
    
    # Check if user_prompt_path is a file path or a string
    if os.path.exists(user_prompt_path):  # If it's a file path, read the file
        user_prompt_path = os.path.join(script_dir, user_prompt_path)
        with open(user_prompt_path, 'r') as f:
            user_prompt = f.read().strip()
    else:  # If it's a string (e.g., previous response), use it directly
        user_prompt = user_prompt_path
    
    # Call ask_gpt to generate response
    response = ask_gpt(
        api_key=API_KEY,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        model=model,
        temperature=temperature
    )
    return response

if __name__ == "__main__":
    # Default prompt paths for make_question
    dpo_generate_question_path = "../prompts/dpo_generate_question.prompt"
    dpo_generate_question_user_path = "../prompts/dpo_generate_question_user.prompt"
    dpo_generate_chose_path = "../prompts/dpo_generate_chosen.prompt"
    dpo_generate_rejected_path = "../prompts/dpo_generate_rejected.prompt"

    # Generate question
    question = generate_response(dpo_generate_question_path, dpo_generate_question_user_path)
    print("Generated Question:")
    print(question, "\n")

    # Generate chosen response using the question as user_prompt
    chosen_response = generate_response(dpo_generate_chose_path, question)
    print("Chosen Response:")
    print(chosen_response, "\n")

    # Generate rejected response using the question as user_prompt
    rejected_response = generate_response(dpo_generate_rejected_path, question)
    print("Rejected Response:")
    print(rejected_response)