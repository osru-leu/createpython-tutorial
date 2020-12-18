"""
Common utility functions
"""

def snake_case(string_to_convert):
    ''' in case of CamelCase, returns snake_case '''
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in string_to_convert]).lstrip('_')

