from gpt_index import GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os
import requests
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/query', methods=['POST'])
def query():
    query_text = request.json['query']
    os.environ['OPENAI_API_KEY'] = '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'
    index = GPTSimpleVectorIndex.load_from_disk("bubble-index.json")
    response = index.query(query_text, response_mode="compact")
    return jsonify({'response': response})
    #print(response.response)

if __name__ == '__main__':
    app.run(debug=True)


