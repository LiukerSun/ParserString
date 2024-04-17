from custom_tokenize import TokenType, Token


class Node:
    def __init__(self, token):
        self.token = token
        self.children = []


def build_syntax_tree(tokens):
    root = Node(Token(TokenType.Function, "ROOT"))
    current_node = root
    stack = [root]

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
            stack.append(current_node)
        elif token.token_type == TokenType.RightParenthesis:
            stack.pop()
            current_node = stack[-1]
        elif token.token_type == TokenType.Split:
            current_node = stack[-1]

    return root.children[
        0
    ]  # Return the first child of the root (the actual syntax tree)


def calculate_tree_value(node, data):
    match node.token.token_type:
        case TokenType.Function:
            match node.token.value:
                case "SUM":
                    return sum(calculate_tree_value(child, data) for child in node.children)
                case "AVG":
                    return sum(calculate_tree_value(child, data) for child in node.children) / len(node.children)
                case "MAX":
                    return max(calculate_tree_value(child, data) for child in node.children)
        case TokenType.Variable:
            variable_path = node.token.value.split('.')
            current_data = data
            for segment in variable_path:
                current_data = current_data.get(segment, 0)  # Default to 0 if segment is not found
            return current_data
        case TokenType.Number:
            return node.token.value

