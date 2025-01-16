from openai import OpenAI
import os


# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

openai.api_key = api_key  # Correctly set the API key for the OpenAI client



def answer_question(document_text, question):
    messages = [
        {"role": "system", "content": "You are a legal assistant. Answer questions based on the provided document."},
        {"role": "user", "content": f"Document: {document_text}\n\nQuestion: {question}"}
    ]

    # Create a chat completion
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Replace with "gpt-4" if you have access
        messages=messages,
        max_tokens=50
    )

    # Access response data correctly
    answer = response.choices[0].message.content.strip()

    # Monitor and log token usage
    usage = response.usage  # Token usage details
    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    # Calculate cost
    cost_per_1k_tokens = 0.002  # $0.002 per 1,000 tokens for gpt-3.5-turbo
    estimated_cost = (total_tokens / 1000) * cost_per_1k_tokens

    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Completion tokens: {completion_tokens}")
    print(f"Total tokens: {total_tokens}")
    print(f"Estimated cost for this request: ${estimated_cost:.6f}")

    # Log usage and cost to a file
    log_path = "logs/usage_log.txt"  # Use a subdirectory

    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    with open(log_path, "a") as log_file:
        log_file.write(f"Total tokens: {total_tokens}, Cost: ${estimated_cost:.6f}\n")

    return answer
