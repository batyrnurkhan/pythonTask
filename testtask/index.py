import os
import pandas as pd
from art import tprint

def fileName_to_Excel():
    res_element = []
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(""):
                res_element.append(os.path.join(file))
    return res_element

def fileName_extensions():
    res_element = []
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(""):
                file_name, file_extension = os.path.splitext(file)
                if(file_extension == ""): file_extension = "undefined"
                res_element.append(os.path.join(file_extension))
    return res_element

def folderName_to_Excel():
    path = os.getcwd()
    res_index = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(""):
                res_index.append(os.path.join(root))
    return res_index

tprint('FILES_NAME>> TO >> EXCEL')

try:
    print('Loading....')
    df = pd.DataFrame({'file\'s\ name': fileName_to_Excel(), 'file\'s\ root':folderName_to_Excel(), 'typeof file': fileName_extensions()})  
    df.to_excel(excel_writer='result.xlsx')
    print('Check file <3')
except:
    print("Something went wrong!")
