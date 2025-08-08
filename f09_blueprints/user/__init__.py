# This folder marks 'user' as a python package

from .user_routes import userBP

# Explanation of the import line
# .(dot) is used for referring to the user_routes present in the current package's level
# Also by importing this object inside __init__.py file we can directly import userBP like:-
# from user import userBp