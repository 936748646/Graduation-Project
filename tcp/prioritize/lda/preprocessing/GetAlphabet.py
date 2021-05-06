import sys

for line in sys.stdin:
    pre_ch = ''
    maybe_apostrophe = False
    for ch in list(line):
        if maybe_apostrophe:
            if ch.isalpha():
                print('\'', end='')
                print(ch, end='')
            else:
                print(' ', end='')
                maybe_apostrophe = False
            continue
        if ch.isalpha():
            print(ch, end='')
        elif ch == '\'' and pre_ch.isalpha():
            maybe_apostrophe = True
        else:
            print(' ', end='')
        pre_ch = ch
    print()
    