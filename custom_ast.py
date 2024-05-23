from custom_tokenize import TokenType, Token
from loguru import logger


class Node:
    def __init__(self, token):
        self.token = token
        self.children = []


def build_syntax_tree(tokens):
    root = Node(Token(TokenType.Function, "ROOT"))
    current_node = root
    syntax_tree = [root]

    for token in tokens:
        if (
            token.token_type == TokenType.Function
            or token.token_type == TokenType.Number
            or token.token_type == TokenType.Variable
        ):
            new_node = Node(token)
            current_node.children.append(new_node)
            current_node = new_node
        elif token.token_type == TokenType.LeftParenthesis:
            syntax_tree.append(current_node)
        elif token.token_type == TokenType.RightParenthesis:
            syntax_tree.pop()
            current_node = syntax_tree[-1]
        elif token.token_type == TokenType.Split:
            current_node = syntax_tree[-1]
    return root.children[0]


def calculate_tree_value(node, data):
    match node.token.token_type:
        case TokenType.Function:
            match node.token.value:
                case "SUM":
                    args_list = [
                        calculate_tree_value(child, data) for child in node.children
                    ]
                    a, b = args_list
                    # 如果a和b都是列表，且长度相同，则逐元素相加
                    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
                        return [x + y for x, y in zip(a, b)]
                    # 如果a是整数，b是列表，则将a加到b的每个元素上
                    elif isinstance(a, (int, float)) and isinstance(b, list):
                        return [x + a for x in b]
                    # 如果b是整数，a是列表，则将b加到a的每个元素上
                    elif isinstance(b, (int, float)) and isinstance(a, list):
                        return [x + b for x in a]
                    # 如果两者都是整数，则直接相加
                    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                        return a + b
                    else:
                        raise ValueError(
                            "Unsupported input types or list lengths do not match."
                        )
                case "SUB":
                    args_list = [
                        calculate_tree_value(child, data) for child in node.children
                    ]
                    a, b = args_list
                    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
                        return [x - y for x, y in zip(a, b)]
                    elif isinstance(a, (int, float)) and isinstance(b, list):
                        return [a - x for x in b]
                    elif isinstance(b, (int, float)) and isinstance(a, list):
                        return [x - b for x in a]
                    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                        return a - b
                    else:
                        raise ValueError(
                            "Unsupported input types or list lengths do not match."
                        )
                case "MUL":
                    args_list = [
                        calculate_tree_value(child, data) for child in node.children
                    ]
                    a, b = args_list
                    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
                        return [x * y for x, y in zip(a, b)]
                    elif isinstance(a, (int, float)) and isinstance(b, list):
                        return [x * a for x in b]
                    elif isinstance(b, (int, float)) and isinstance(a, list):
                        return [x * b for x in a]
                    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                        return a * b
                    else:
                        raise ValueError(
                            "Unsupported input types or list lengths do not match."
                        )
                case "DIV":
                    args_list = [
                        calculate_tree_value(child, data) for child in node.children
                    ]
                    a, b = args_list
                    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
                        return [x / y if y != 0 else float("inf") for x, y in zip(a, b)]
                    elif isinstance(a, (int, float)) and isinstance(b, list):
                        return [a / x if x != 0 else float("inf") for x in b]
                    elif isinstance(b, (int, float)) and isinstance(a, list):
                        return [b / x if x != 0 else float("inf") for x in a]
                    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                        if b == 0:
                            raise ZeroDivisionError("Cannot divide by zero.")
                        return a / b
                    else:
                        raise ValueError(
                            "Unsupported input types or list lengths do not match."
                        )
                case "AVG":
                    return sum(
                        calculate_tree_value(child, data) for child in node.children
                    ) / len(node.children)
                case "MAX":
                    return max(
                        calculate_tree_value(child, data) for child in node.children
                    )
        case TokenType.Variable:
            variable_path = node.token.value.split(".")
            current_data = data
            for segment in variable_path:
                current_data = current_data.get(segment, 0)
            return current_data
        case TokenType.Number:
            return node.token.value
