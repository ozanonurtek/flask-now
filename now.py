from parser import Parser
from architect import Architect

if __name__ == '__main__':
    parser = Parser()
    if parser.parse():
        architect = Architect("")
        architect.build()


