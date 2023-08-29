from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai


api_key = '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'
openai.api_key = api_key

@api_view(['POST'])
def generate_question(request):
   
    topic = request.data.get('topic', '') 
    user_message = f"give me random question about {topic} and create question, random 5 choices, and answer replay with JSON format only"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    assistant_reply = response['choices'][0]['message']['content']

    return Response(assistant_reply)