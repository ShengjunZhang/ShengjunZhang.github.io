import sys

def dev():
    print('dev mode')

def default():
    print('Hello')

def main():
    if sys.argv[1] == 'dev':
        dev()
    else:
        default()

if __name__ == '__main__':
    main()

