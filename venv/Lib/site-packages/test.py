__author__ = 'drornr'

"""This is a test module - we are just learning python - do not use this code"""

def print_lol(the_list):
    """This function is a recursive function that prints all the contents of nested lists"""
    for each_item in the_list:

        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)