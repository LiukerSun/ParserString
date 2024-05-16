FUNC_ARGS = {
    "SUM": {
        "args": [(int, float, list), (int, float, list)],
        "return": (int, float, list),
        "description": "求两个参数的和.",
    },
    "SUB": {
        "args": [(int, list), (int, list)],
        "return": (int, float, list),
        "description": "求两个参数的差.",
    },
    "MUL": {
        "args": [(int, list), (int, list)],
        "return": (int, float, list),
        "description": "求两个参数的积.",
    },
    "DIV": {
        "args": [(int, list), (int, list)],
        "return": (int, float, list),
        "description": "求两个参数的商.",
    },
    "AVG": {
        "args": [(list)],
        "return": (int, float),
        "description": "求平均值.",
    },
    "MAX": {
        "args": [(list)],
        "return": (int, float),
        "description": "求最大值.",
    },
    "MIN": {
        "args": [(list)],
        "return": (int, float),
        "description": "求最小值.",
    },
    "COUNT": {
        "args": [(list)],
        "return": (int),
        "description": "求元素个数.",
    },
}
