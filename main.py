from custom_tokenize import tokenize
from custom_ast import build_syntax_tree, calculate_tree_value
from loguru import logger

data_dict = {"step1": {"aa": {"bb": [1, 2]}}, "step2": {"aa": {"bb": [1, 2, 3]}}}
formula1 = "SUM(SUM(3,2),step2.aa.bb)"
formula2 = "SUB(SUB(1,2),step2.aa.bb)"
formula3 = "MUL(MUL(1,2),step2.aa.bb)"
formula4 = "DIV(DIV(1,2),step2.aa.bb)"


def parser(formula, data):
    tokens = tokenize(formula)
    syntax_tree = build_syntax_tree(tokens)
    result = calculate_tree_value(syntax_tree, data)
    logger.info(rf"formula:{formula},result: {result}")
    return result


logger.info(rf"data_dict is :{data_dict}")
parser(formula=formula1, data=data_dict)
parser(formula=formula2, data=data_dict)
parser(formula=formula3, data=data_dict)
parser(formula=formula4, data=data_dict)
