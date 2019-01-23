from flask import Flask, request, make_response, jsonify
from drqa import pipeline

app = Flask(__name__)

p = pipeline.DrQA(cuda=False)

@app.route('/')
def home():
    question = "What is Trump?"

    if 'q' in request.args:
        question = request.args['q']

    result = p.process(question, None, 1, 1)

    return 'Question: ' + question + '<br />' + 'Answer: ' + result[0]['span']

@app.route('/ask', methods=["POST"])
def ask():
    question = "What is the meaning of life?"
    
    print(request.form)

    if 'question' in request.form:
        question = request.form['question']
    
    try:
        result = p.process(question, None, 1, 1)
    except:
        result = [{ 'span': "I'm sorry I couldn't find an answer to that question" }]
        
    return make_response(jsonify({ 'question': question, 'answer': result[0]['span'] }))
       

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
