from custom_tokenize import TokenType, Token
from loguru import logger
from custom_func_config import FUNC_ARGS


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

    logger.info(syntax_tree)
    return root.children[0]


def calculate_tree_value(node, data):
    match node.token.token_type:
        case TokenType.Function:
            # 取出函数配置
            func_config = FUNC_ARGS[node.token.value]
            match node.token.value:
                case "SUM":
                    # 判断sum的每一个参数.
                    # 如果有多个列表,需要判断列表长度是否一致.
                    # 如果没有列表,则返回数字,如果只有一个列表,则返回列表,·
                    sum_list = [
                        calculate_tree_value(child, data) for child in node.children
                    ]
                    list_index_list = []
                    list_length_list = []
                    for item_index in range(len(sum_list)):
                        if isinstance(sum_list[item_index], list):
                            list_index_list.append(item_index)
                            list_length_list.append(len(sum_list[item_index]))
                    if len(list_index_list) > 1:
                        ...

                    # if all(isinstance(item, (int, float)) for item in sum_list):
                    #     return sum(sum_list)
                    # else:
                    #     list_count = 0
                    #     list_length = set()
                    #     for item in sum_list:
                    #         if isinstance(item, list):
                    #             list_count += 1
                    #             list_length.add(len(item))
                    #     if list_count > 1 and len(list_length) > 1:
                    #         raise ValueError("ERROR! 传入了多个长度不同列表!")
                    #     else:
                    #         if list_count == 1:
                    #             # 找到列表元素所在位置
                    #             return [item for item in sum_list]
                    #         else:
                    #             return [sum(item) for item in zip(*sum_list)]
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
