from django.shortcuts import render
import openai
import requests
import keys
import json

message_list = []
def chat(chat):
    global message_list
    querry = chat
    _querry = {"role": "user", "content": str(querry)}
    message_list.append(_querry)
    api_key = keys.openAI_key
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": message_list
    }
    response = requests.post(url, headers=headers, json=payload)
    result = json.loads(response.text)["choices"][0]['message']['content']
    return result


def index(request):
  context = {}
  if request.method == "POST":
      _query = request.POST["query"]
      answer = (chat(_query))
      context["answer_response"] = answer
  return render(request, "index.html", context)
