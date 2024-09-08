from openai import AzureOpenAI
import requests
import os


key="c9852a5c136a4b5f976808ef89c168d1"
endpoint_url="https://chatbot7318408224.openai.azure.com/"
whisper_model="whisper"
chat_model="gpt-4o"
region="eastus"

final_url="https://chatbot7318408224.openai.azure.com/openai/deployments/whisper/audio/translations?api-version=2024-06-01"

headers = {
    "api-key": key
}

filePath="C:\\Sakthivel\\Recording.m4a"

with open(filePath, "rb") as file:
    files = {"file": (os.path.basename(filePath), file, "application/octet-stream")}

    finalResponse=requests.post(final_url, headers=headers,files=files).json();
    print(finalResponse)

    userPrompt = finalResponse['text']

    client=AzureOpenAI(
        api_key="763679521f0b43fe90f4268417b48995",
        api_version="2023-03-15-preview",
        azure_endpoint="https://azure-ai-learn-new.cognitiveservices.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2023-03-15-preview/"
    )

    response = client.chat.completions.create(
            model="gpt-4o",  # You can change this to "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Query:"+ userPrompt}
            ],
            max_tokens=150,  # Adjust the number of tokens according to your needs
            temperature=0.7,  # Adjust for more or less randomness
            top_p=1.0,  # Nucleus sampling
            n=1,  # Generate one response
            stop=None  # No stop condition
        )
    
    print(response.choices[0].message.content)
