import sys

def ws2bf(file):
  ops = []
  for line in file:
    for i in range(len(ops)):
      ops[i] += 1
      if ops[i] >= 8:
        ops[i] = 0
      else:
        break
    else:
      ops.append(0)

  for op in ops:
    print ['+', '-', '<', '>', '[', ']', '.', ','][op],

if __name__ == '__main__':
  ws2bf(sys.stdin)