import openai
import os

# Set up your OpenAI API credentials
openai.api_key = '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'

#os.environ["OPENAI_API_KEY"] = "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"
#os.environ["SERPAPI_API_KEY"] = "a04ee48f71a634d065405ad27fb43c7d189c2086be2fd931d1ff3e389ce7fe5f"

# Function to read law data from text files
def read_law_data(file_paths):
    law_data = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            law_content = file.read().strip()
            law_data.append(law_content)
    return law_data

# Function to get AI-generated response based on user input and law data
def get_ai_response(user_input, law_data):
    prompt = f"User: {user_input}\nData: " + "\n".join(law_data)
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    answer = response.choices[0].text.strip().split('\n')[0]
    return answer

# Example usage
file_paths = ['/Users/yaya/Desktop/Text Mining Project/ChatBot/DIVISION OF ASSETS AFTER DIVORCE.txt']
law_data = read_law_data(file_paths)

user_query = input("Enter your query: ")
response = get_ai_response(user_query, law_data)
print(response)
