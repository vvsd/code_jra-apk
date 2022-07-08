import jsonpath

json = {"a": "c", "b": "d"}
print(jsonpath.jsonpath(json, "$.a"))
