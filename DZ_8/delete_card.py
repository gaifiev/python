def DelCardWorker(number):
    number = int(number - 1)
    with open("Data_base.csv", "r+", encoding='utf-8') as f:
        lines = f.read().splitlines()
        lines.pop(number)

    with open("Data_base.csv", "w", encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
        print('\n'.join(lines))
