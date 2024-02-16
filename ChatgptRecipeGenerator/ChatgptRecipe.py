import openai

import os
#orange line
from flask import Flask, render_template_string, request  

openai.api_key = os.environ['OPENAI_API_KEY'] 

def generate_tutorial(components):

 response = openai.ChatCompletion.create(

  model="gpt-3.5-turbo",

  messages=[{

   "role": "system",

   "content": "You are a helpful assistant"

  }, {

   "role":

   "user",

   "content":

   f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"

  }])

 return response['choices'][0]['message']['content']  
app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])

def hello():

 output = ""

 if request.method == 'POST':

  components = request.form['components']

  output = generate_tutorial(components)

@app.route('/generate', methods=['POST'])

def generate():

 components = request.form['components']

 return generate_tutorial(components)

if _name_ == '_main_':

 app.run(host='0.0.0.0', port=8080)

return render_template_string('''

<!DOCTYPE html> 
<html>
<head>
 <title>Project generator</title>
 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" >

<script>

async function generateTutorial(){

 const components=documents.queryselector(#'components').value 

const output=documents.queryselector('output'); 

output.textcontext="Cooking a recipe for you.." 

}
 
