def convert(number):
    factors = [3,5,7]
    keywords = {3:"Pling", 5:"Plang", 7:"Plong"}
    results = []

    for i in factors:
        if number % i == 0:
            results.append(i)
    if len(results) > 0:
        first = ""
        second = ""
        third = ""
        if 3 in results:
            first = keywords[3]
        if 5 in results:
            second = keywords[5]
        if 7 in results:
            third = keywords[7]
        return first+second+third
    else:
        return str(number)


print (convert(28))