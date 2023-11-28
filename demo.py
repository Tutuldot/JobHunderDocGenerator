import requests
import json



url = 'https://api.deepinfra.com/v1/inference/meta-llama/Llama-2-70b-chat-hf'
headers = {
    'Authorization': f'Bearer ABC',
    'Content-Type': 'application/json'
}
data = {
    'input': 'Current Employer: StMicroelectronics as Senior Data Analyst for 1 year, Previous Employer: Asurion as Senior Business Intelligence Developer for 6 years, skills: Skills: Data Modelling, Data Visualization, Database Design, Data management, ETL Development,   SQL Scripting, Data Management and Data Analysis. please generate a cover letter for senior data analyst at ABC Corporation.'
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())