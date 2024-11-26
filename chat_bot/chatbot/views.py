from django.shortcuts import render
from django.http import JsonResponse
from openai import Client
#from config import key
import time

client = Client(api_key="")

assistant_id = ""
thread_id = ""

def home(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        bot_response = get_bot_response(user_message)
        return JsonResponse({'response' : bot_response})
    return render(request, 'home.html')


def get_bot_response(user_message):
    message_create = client.beta.threads.messages.create(
        role="user",
        thread_id=thread_id,
        content=f"{user_message}"
    )
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    time.sleep(7)

    run_info = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run.id
    )

    messages = client.beta.threads.messages.list(
        thread_id=thread_id,
    )
    #print(messages.data[0].content[0].text.value)
    return messages.data[0].content[0].text.value
    #return f'{user_message}'
