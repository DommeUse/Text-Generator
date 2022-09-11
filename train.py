import argparse
import re
import os
import pickle

'''--------------------Parsing argumnts--------------------'''
parser = argparse.ArgumentParser(description="Этот код создаёт модель, обученную на текстах песен")
parser.add_argument(
    '--input_dir',
    type=str,
    help="Путь к папке с песнями"
)
parser.add_argument(
    '--model',
    type=str,
    default="model.pkl",
    help="Путь к файлу, в который сохраняется модель(с расширением pkl)"
)
args = parser.parse_args()
if args.input_dir==None:
    args.input_dir = input("Введите путь к папке с текстами: ")

'''--------------------Generating model--------------------'''
model = {}
data = os.listdir(path=args.input_dir)
for file in data:
    with open(args.input_dir+"/"+file,"r",encoding="utf-8") as file:
        text = ""
        for i in file:
            text += i
        text = re.sub(r'\W+',' ',text)
        text = text.lower().strip().split()
        for i in range(len(text)-1):
            if i>0:
                model[text[i-1]+" "+text[i]] = model.get(text[i-1]+" "+text[i],[])
                model[text[i-1]+" "+text[i]].append(text[i+1])
            model[text[i]] = model.get(text[i],[])
            model[text[i]].append(text[i+1])
'''--------------------Saving model--------------------'''
with open(args.model,"wb") as f:
    pickle.dump(model,f)
