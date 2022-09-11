import pickle
import argparse
import random

'''--------------------Parsing argumnts--------------------'''
parser = argparse.ArgumentParser(description="Этот код создаёт сгенерированный текст")
parser.add_argument(
    '--model',
    type=str,
    help="Путь к моделе"
)
parser.add_argument(
    '--prefix',
    type=str,
    help="Начальное слово"
)
parser.add_argument(
    '--length',
    type=int,
    help="Длина генерируемой последовательности"
)
args = parser.parse_args()
if args.model==None:
    args.model = input("Введите путь к модели: ")
if args.length == None:
    args.length = int(input("Введите длину последовательности: "))
'''--------------------Importing model--------------------'''
with open(args.model,"rb") as f:
    data = pickle.load(f)
#print(len(data.keys()))
if args.prefix==None:
    start = random.choice(list(data.keys()))
else:
    start = args.prefix
'''--------------------Generating text--------------------'''
count = 0
lst = []
while count<args.length:
    lst.append(start)
    if count==0:
        print(start[0].upper()+start[1:],end=" ")
    else:
        print(start,end=" ")
    try:
        if count>1:
            if data.get(lst[-2]+" "+lst[-1],[])!=[]:
                start = random.choice(data[lst[-2]+" "+lst[-1]])
            else:
                start = random.choice(data[start])
        else:
            start = random.choice(data[start])
    except:
        print("\nЧто-то пошло не так")
    count += 1