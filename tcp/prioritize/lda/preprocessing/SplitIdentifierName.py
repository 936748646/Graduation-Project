import sys

for line in sys.stdin:
    line = line.replace('\n','')
    line = line.replace('\r','')
    status = 0
    for ch in line:
        if status == 0:
            print(ch, end='')
            status = 1
            if ch.isupper():
                status = 2
            continue
        if status == 1:
            if ch.isupper():
                print()
                status = 2
            print(ch, end='')
            continue
        if status == 2:
            if not ch.isupper():
                status = 1
            print(ch, end='')
            continue
    print()
    