import sys, os , json
sys.path.append(os.path.abspath(os.path.join('..', 'data_parse')))
read_file = open("sample_data_question_2.txt","r")


class Database:
    def read(self):
        return read_file.readlines()

