import logging
from surround import Stage, SurroundData
from drqa import pipeline

class DrqaData(SurroundData):
    input_data = None
    output_data = None

    def __init__(self, input_data):
        self.input_data = input_data

class ProcessQuestion(Stage):
    def __init__(self):
        logging.log(logging.INFO, "Initializing the DrQA pipeline..")
        self.processor = pipeline.DrQA(cuda=False)

    def operate(self, data, config):
        # Attempt to process the question from input_data
        try:
            result = self.processor.process(data.input_data, None, config['topAnswers'], config['numDocuments'])
            data.output_data = { 'question': data.input_data, 'answer': result[0]['span'] }
        except:
            data.output_data = None
            
class ValidateData(Stage):
    def operate(self, data, config):
        data.output_data = data.output_data if data.output_data != None else { "answer": "No response was found!" }
