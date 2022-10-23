def AddWorker(personal):
    with open('Data_base.csv', 'a', encoding='utf-8') as f:
        f.write(personal + '\n')
