import json
import openai
from azure_config import AzureConfig

# Load JSON configuration
def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

outline_config = load_config("prompt_config/outline.JSON")
diagram_config = load_config("prompt_config/diagram.JSON")

# Initialize message lists
outline_messages = [{"role": "system", "content": outline_config.get("systemPrompt", "You are an AI assistant.") }]
diagram_messages = [{"role": "system", "content": diagram_config.get("systemPrompt", "You are an AI assistant.") }]

# Apply Azure OpenAI settings
openai.api_type = AzureConfig.API_TYPE
openai.api_key = AzureConfig.API_KEY
openai.api_base = AzureConfig.API_BASE
openai.api_version = AzureConfig.API_VERSION

def generate_chat_response(config, messages, user_input):
    for example in config.get("fewShotExamples", []):
        if isinstance(example.get("userInput"), str) and isinstance(example.get("chatbotResponse"), str):
            messages.extend([
                {"role": "user", "content": example["userInput"]},
                {"role": "assistant", "content": example["chatbotResponse"]}
            ])
    
    messages.append({"role": "user", "content": str(user_input)})
    
    try:
        response = openai.ChatCompletion.create(
            engine=AzureConfig.ENGINE,
            messages=messages,
            temperature=float(config["chatParameters"].get("temperature", 0.7)),
            max_tokens=int(config["chatParameters"].get("maxResponseLength", 500)),
            top_p=float(config["chatParameters"].get("top_p", 1.0)),
            frequency_penalty=float(config["chatParameters"].get("frequencyPenalty", 0)),
            presence_penalty=float(config["chatParameters"].get("presencePenalty", 0))
        )
        # print(response["choices"][0]["message"]["content"])
        return response["choices"][0]["message"]["content"]
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        raise Exception(f"Error generating response: {str(e)}")

def generate_response(user_input):
    return generate_chat_response(outline_config, outline_messages, user_input)

def generate_diagram(user_input):
    return generate_chat_response(diagram_config, diagram_messages, user_input)
