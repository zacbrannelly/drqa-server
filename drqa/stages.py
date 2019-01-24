import logging
from surround import Stage, SurroundData

class DrqaData(SurroundData):
    input_data = None
    output_data = None

    def __init__(self, input_data):
        self.input_data = input_data

class ProcessQuestion(Stage):
    def operate(self, data, config):
        data.output_data = None

class ValidateData(Stage):
    def operate(self, data, config):
        data.output_data = data.output_data if data.output_data != None else { "answer": "No response was found!" }
