import sys

keywords = ['abstract', 'assert', 'boolean', 'break', 'byte',
            'case', 'catch', 'char', 'class', 'const', 'continue',
            'default', 'do', 'double', 'else', 'enum', 'extends',
            'final', 'finally', 'float', 'for', 'if', 'goto',
            'implements', 'import', 'instanceof', 'int', 'interface',
            'long', 'native', 'new', 'package', 'private', 'protected',
            'public', 'return', 'short', 'static', 'strictfp', 'super',
            'switch', 'synchronized', 'this', 'throw', 'throws',
            'transient', 'try', 'void', 'volatile', 'while', '_',
            'true', 'false', 'null']

for line in sys.stdin:
    line = line.replace('\n','')
    line = line.replace('\r','')
    if line not in keywords:
        print(line)
        