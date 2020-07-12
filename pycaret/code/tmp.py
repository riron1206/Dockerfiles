"""
pycaretはpythonモジュールとしては実行できない。。。
"""

import pycaret

# 「糖尿病」データセット
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

from pycaret.classification import *
exp1 = setup(diabetes,
             session_id=123,
             target='Class variable')
