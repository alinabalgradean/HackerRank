from collections import OrderedDict

def merge_the_tools(string, k):
    """Function to split a given string into k equal parts.

    Prints only unique combinations of k equal parts.

    Args:
        string [str]: a given string to split
        k [int]: how many parts to split the string into

    Returns:
         None
    """
    for i in range(0, len(string, k):
        print(''.join(OrderedDict.fromkeys(string[i:i+k])))
    

