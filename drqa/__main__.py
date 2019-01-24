import logging
import argparse
import os
from flask import Flask, request, make_response, jsonify
from surround import Surround, Config
from drqa.stages import ValidateData, DrqaData, ProcessQuestion

logging.basicConfig(level=logging.INFO)

def is_valid_dir(arg_parser, arg):
    if not os.path.isdir(arg):
        arg_parser.error("Invalid directory %s" % arg)
    else:
        return arg

def is_valid_file(arg_parser, arg):
    if not os.path.isfile(arg):
        arg_parser.error("Invalid file %s" % arg)
    else:
        return arg

parser = argparse.ArgumentParser(description="The Surround Command Line Interface")
parser.add_argument('-c', '--config-file', required=True, help="Path to config file",
                                     type=lambda x: is_valid_file(parser, x))

app = Flask(__name__)
surround = None

def init_surround(config_path):
    surround = Surround([ValidateData(), ProcessQuestion()])

    # Read config file
    config = Config()
    config.read_config_files([config_path])
    surround.set_config(config)


@app.route('/')
def home():
    return 'This is a server not for your eyes obviously'

@app.route('/ask', methods=['POST'])
def ask():
    form_data = request.form

    question = 'Where is Batman?'

    if 'question' in form_data:
        question = form_data['question']

    # Process the question
    data = DrqaData(question)
    surround.process(data)

    # Get the question answer
    output = data.output_data

    # Convert output dict to JSON and send back
    return make_response(jsonify(output)) 


if __name__ == "__main__":
    # Initialize surround and it's stages
    args = parser.parse_args()
    init_surround(args.config_path)

    # Run the flask server to receive input
    app.run("0.0.0.0", 80)