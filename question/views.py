from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai
import json


api_key = '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'
openai.api_key = api_key

@api_view(['POST'])
def generate_question(request):
   
    topic = request.data.get('topic', '') 
    user_message1 = f"give me random one question about {topic}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message1}
        ]
    )

    assistant_reply1 = response['choices'][0]['message']['content']

    print(assistant_reply1)

    user_message2 = f"give me solution of question {assistant_reply1} only reply with integer"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message2}
        ]
    )

    assistant_reply2 = response['choices'][0]['message']['content']

    print(assistant_reply2)

    user_message3 = f"give me random choises of question {assistant_reply1}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message3}
        ]
    )

    assistant_reply3 = response['choices'][0]['message']['content']

    print(assistant_reply3)

    data = {
    "question":assistant_reply1,
    "choises":assistant_reply3,
    "solution":assistant_reply2
    }

    return Response(data)