import argparse
from os.path import expanduser


# argparsing
parser = argparse.ArgumentParser(description='get N most used commands')
parser.add_argument('-n', type=int, help='show N most used commands')
args = parser.parse_args()
if not args.n:
    args.n = 20


# generating dict
home = expanduser('~')
with open(f'{home}/.bash_history') as f:
    commands = f.read().splitlines()
    d = dict()
    for c in commands:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

#sorting by use
sorted_commands = sorted(d.items(), key=lambda x: x[1], reverse=1)
max_len = len(max(sorted_commands[:args.n], key=lambda x: len(x[0]))[0])
for i in range(args.n):
    print("{:<{max_len}} {} times used".format(*sorted_commands[i],
                                               max_len=max_len))
