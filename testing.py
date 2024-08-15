from openai import AzureOpenAI
from time import sleep

client = AzureOpenAI(
    azure_endpoint="https://aoai-slb-u3idaedrye-ca.ambitiousisland-6e1de7f2.northeurope.azurecontainerapps.io",  #if you deployed to Azure Container Apps, it will be 'https://app-[something].[region].azurecontainerapps.io'
    api_key="does-not-matter", #The api-key sent by the client SDKs will be overriden by the ones configured in the backend environment variables
    api_version="2023-12-01-preview"
)

while True:
    
    try:
        response = client.chat.completions.create(
            model="chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the first letter of the alphabet?"}
            ]
        )
        #print(response)
        completion_message = response.choices[0].message.content
        formatted_output = f"Response: {completion_message}"
        print(formatted_output)
        sleep(5)
    except Exception as e:
        error_code = int(getattr(e, 'code', None))
        if error_code in [429, 500, 403]:
            print(f"An error occurred: {str(e)}. Retrying...")
            sleep(5)
            continue
        elif error_code >= 500:
            print(f"An error occurred: {str(e)}. Retrying...")
            sleep(5)
            continue
        else:
            print(f"An error occurred: {str(e)}")
            break