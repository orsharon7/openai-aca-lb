from openai import AzureOpenAI
from time import sleep

client = AzureOpenAI(
    azure_endpoint="https://aoai-slb-u3idaedrye-ca.thankfulglacier-4949ac0f.northeurope.azurecontainerapps.io",  #if you deployed to Azure Container Apps, it will be 'https://app-[something].[region].azurecontainerapps.io'
    api_key="does-not-matter", #The api-key sent by the client SDKs will be overriden by the ones configured in the backend environment variables
    api_version="2023-12-01-preview"
)

while True:
    response = client.chat.completions.create(
        model="chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the first letter of the alphabet?"}
        ]
    )
    print(response)
    sleep(5)