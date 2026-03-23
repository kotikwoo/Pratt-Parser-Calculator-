from lexer import Lexer
from parser_ import Parser
from interpeter import Interpeter

while True:
    try:
        text = input("calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        interpeter = Interpeter()
        value = interpeter.visit(tree)
        print(value)
    except Exception as e:
        print(e)