import sys
from levenstein import levenstein_m

read, write = sys.argv[1:]
try:
    file_input = open(read).read().split()
except FileNotFoundError:
    print('Create an input file!')
    file_input = ''

answer = ''
for i in range(0, len(file_input), 2):
    a = ''.join(open(file_input[i]).read().split())
    b = ''.join(open(file_input[i + 1]).read().split())
    answer += str(levenstein_m(a, b)) + '\n'

file_scores = open(write, 'w')
file_scores.write(answer)
file_scores.close()
