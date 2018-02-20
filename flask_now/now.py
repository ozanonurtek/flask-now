from .parser import Parser
from .architect import Architect

def build():
    parser = Parser()
    result, architecture = parser.parse()
    if result:
        architect = Architect(architecture)
        architect.build()

def main():
    build()
