var_string = "Test"  # "" vs '' -> the same
# char not exist in python,  "a" is just a one element string

var_float = 1.0
print(1/2)
print(1//2)

var_int = 1


var_bool = True  # False if 0, None, [], (), {}
print(bool(1))
print(bool(-1))

var_list = [1, 1.0, "test", [1, 2, 3]]
print(var_list)
print(var_list[1])
print(var_list[-1])

var_dict = {
    "animal": "cat",
    "age": 2,
}
print(var_dict["animal"])

var_tuple = (1, 2)
