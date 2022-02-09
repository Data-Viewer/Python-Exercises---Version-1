def is_isogram(string):
    string = string.lower().replace(" ", "").replace("-", "")
    string = [i for i in string]
    string_set = list(set(string))
    result = len(string)-len(string_set)
    return result == 0


print (is_isogram("hello"))