import re


class TokenType:
    Number = "Number"
    Function = "Function"
    LeftParenthesis = "LeftParenthesis"
    RightParenthesis = "RightParenthesis"
    Split = "Split"
    Operator = "Operator"
    Variable = "Variable"


class Token:
    def __init__(self, token_type, value=None, children=None):
        self.token_type = token_type
        self.value = value
        self.children = children if children else []


def tokenize(formula):
    tokens = []
    current = 0

    while current < len(formula):
        char = formula[current]
        if re.match(r"(step|stage)[a-zA-Z\d._]*", formula[current:]):
            value = re.match(r"(step|stage)[a-zA-Z\d._]*", formula[current:]).group(0)
            tokens.append(Token(TokenType.Variable, value))
            current += len(value)
        elif re.match(r"\d", char):
            value = ""
            while re.match(r"\d", char):
                value += char
                current += 1
                if current < len(formula):
                    char = formula[current]
                else:
                    break
            tokens.append(Token(TokenType.Number, float(value)))
        elif re.match(r"[A-Z_]", char):
            value = ""
            while re.match(r"[A-Z_]", char):
                value += char
                current += 1
                if current < len(formula):
                    char = formula[current]
                else:
                    break
            tokens.append(Token(TokenType.Function, value))
        elif re.match(r"[(]", char):
            tokens.append(Token(TokenType.LeftParenthesis, char))
            current += 1
        elif re.match(r"[)]", char):
            tokens.append(Token(TokenType.RightParenthesis, char))
            current += 1
        elif re.match(r"[,]", char):
            tokens.append(Token(TokenType.Split, char))
            current += 1
        elif char == " ":
            current += 1
        else:
            raise ValueError("Invalid character: " + char)
    return tokens
