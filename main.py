from custom_tokenize import tokenize
from custom_ast import build_syntax_tree, calculate_tree_value
from loguru import logger
formula = "SUM(2,SUM(1,2),step2.aa.bb)"
data = {"step1": {"aa": {"bb": 1}}, "step2": {"aa": {"bb": 2}}}

tokens = tokenize(formula)
for token in tokens:
    logger.info(rf"token.token_type is {token.token_type}: token.value is {token.value}")
syntax_tree = build_syntax_tree(tokens)
result = calculate_tree_value(syntax_tree, data)

logger.info(rf"formula : {formula}")
logger.info(rf"Result : {result}")
