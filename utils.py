import os
import requests
import json
import openai
from duckduckgo_search import ddg


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
    
    
def webgpt_result(query : str, number_of_results : int) -> str:
    params = (
        ('q', f'{query}'),
        ('max_results', f'{number_of_results}'),
        ('region', 'wt-wt'),
    )

    headers = {
        'authority': 'ddg-webapp-aagd.vercel.app',
        'accept': '*/*',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://chat.openai.com',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50',
    }
    response = requests.get('https://ddg-webapp-aagd.vercel.app/search', headers=headers, params=params)
    json_data = response.json()

    Result_ = ""
    for result in json_data:
        Result_ += "\"" + result["title"] + "\"" + "\n"
        Result_ += "\"" + result["body"] + "\"" + "\n"
        Result_ += "URL: " + result["href"] + "\n\n"
        
    prompt_filepath = os.path.join(os.getcwd(), "prompts.txt")
        
    prompt = open_file(prompt_filepath).replace('<<web_results>>', Result_)
    prompt = prompt.replace("<<query>>", query)

    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    
    openai.api_key = ""
    openai.api_base =  ""
    openai.api_type = 'azure'
    openai.api_version = '2022-12-01' 
    deployment_name=''
    
    r = openai.Completion.create(engine=deployment_name, prompt=prompt, temperature=0.3, max_tokens=800)
    response_ = r.choices[0]['text']
    
    return response_



def webgpt_results1(query : str, number_of_results : int):
    
    results = ddg(query, region='wt-wt', safesearch='Off', max_results = number_of_results)

    results = str(results)
    
    prompt_filepath = os.path.join(os.getcwd(), "prompts.txt")
    
    prompt = open_file(prompt_filepath).replace('<<web_results>>', results)
    prompt = prompt.replace("<<query>>", query)

    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    
    openai.api_key = ""
    openai.api_base =  ""
    openai.api_type = 'azure'
    openai.api_version = '2022-12-01' 
    deployment_name=''
    
    r = openai.Completion.create(engine=deployment_name, prompt=prompt, temperature=0.3, max_tokens=800)
    response_ = r.choices[0]['text']
    
    return response_
