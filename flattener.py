#! /usr/bin/python3

class arrayFlattener:
    def __init__(self):
        pass

    
    # if it's a list or tuple, flatten the subelement recursively
    # otherwise just append it.
    def flatten(self, array):
        out_array = []
        for item in array:
            if isinstance(item, list) or isinstance(item,tuple):
                for sub_array in self.flatten(item):
                    out_array.append(sub_array)
            else:
                out_array.append(item)

        return out_array
