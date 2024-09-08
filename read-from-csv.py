# %%
import json
import pandas as pd
import openai


# %%
df=pd.read_csv("csv1.csv")
df.head()

# %%
from openai import AzureOpenAI
client=AzureOpenAI(
    api_key="", # Update with your api key
    api_version="2023-03-15-preview",
    azure_endpoint="" # Update with your end point
)

# %%
prompt="give me the records which has the id as 1 and 5"
context=df.head().to_json(orient="records")

# %%
response = client.chat.completions.create(
        model="gpt-4o",  # You can change this to "gpt-3.5-turbo" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Context:"+ context +"Query:"+ prompt}
        ],
        max_tokens=150,  # Adjust the number of tokens according to your needs
        temperature=0.7,  # Adjust for more or less randomness
        top_p=1.0,  # Nucleus sampling
        n=1,  # Generate one response
        stop=None  # No stop condition
    )

response.choices[0].message.content



