from bottle import route, post, run, request
from openai import OpenAI

#OpenAI Settings
api_key ='APIKEY'
client = OpenAI(api_key=api_key)

#Get Image from Dalle
def image_get(client, query):
  response = client.images.generate(
    model="dall-e-3",
    prompt=query,
    size="1024x1024",
    quality="standard",
    n=1,
  )

  image_url = response.data[0].url
  return image_url, query

#Rewrite the User query with OpenAI to add bias
def bias_ai(client, query):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Pastafarian"},
        {"role": "assistant", "content": "the users input is going to be used to craete an image with Dall E"},
        {"role": "assistant", "content": "rewrite the user input with a subtle addition about pasta so that it will create a nice image"},
        {"role": "user", "content": query}
    ]
        )
    response = response.choices[0].message.content
    print(response)
    return response

#Index Page. Query form sends values back to this page
@route('/')
@post('/')
def index():
  query = request.forms.get('query')

  image_original=''
  image_bias=''
  image_ai_bias=''

  if query != None:
    image_response = image_get(client, query)
    image_original = f'<div style="width:200px;"><img style="width:200px; height:auto;" src="{image_response[0]}"><br>{image_response[1]}</div>'
    
    bias = 'put a chick in it and a rainbow'
    query_bias = f'{query} - {bias}'
    image_response = image_get(client, query_bias)
    image_bias = f'<div style="width:200px;"><img style="width:200px; height:auto;" src="{image_response[0]}"><br>{image_response[1]}</div>'
    
    query_ai_bias = bias_ai(client, query)
    image_response = image_get(client, query_ai_bias)
    image_ai_bias = f'<div style="width:200px;"><img style="width:200px; height:auto;" src="{image_response[0]}"><br>{image_response[1]}</div>'

  form =  '''
          <form action="./" method="post">
          <textarea rows="1" cols="35" name="query"></textarea>
          <br>
          <input type="submit">
          </form>
          '''

  page = f'{form}<br> <div style="display:flex;">{image_original} {image_bias} {image_ai_bias}</div>'

  return page

run(host='0.0.0.0', port=80, debug=True)