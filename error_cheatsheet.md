# Python Error Cheat Sheet

| Error | Cause | Fix |
|---|---|---|
| IndexError | Accessing a list index that does not exist | Check the index range |
| KeyError | Accessing a dictionary key that does not exist | Check the key or use `get()` |
| TypeError | Using an incompatible data type | Check and convert the data type |
| RecursionError | Too many recursive function calls | Add a correct base condition |
| AttributeError | Accessing an attribute or method that does not exist | Check the object and attribute name |

## IndexError

An `IndexError` happens when you use a list position that is outside the list.

### Example that causes the error

```python
numbers = [10, 20]
print(numbers[2])
```

There is no item at index `2`, so Python raises `IndexError`.

### Corrected version

```python
numbers = [10, 20]
print(numbers[1])
```

The list has items at indexes `0` and `1`, so index `1` is valid.

## KeyError

A `KeyError` happens when you ask a dictionary for a key that it does not contain.

### Example that causes the error

```python
student = {"name": "Asha"}
print(student["age"])
```

The dictionary has no `"age"` key.

### Corrected version

```python
student = {"name": "Asha"}
print(student.get("age", "Age not available"))
```

`get()` returns the default message when the key is missing instead of raising an error.

## TypeError

A `TypeError` happens when an operation is used with the wrong kind of data.

### Example that causes the error

```python
age = 20
print("Age: " + age)
```

Python cannot join a string and an integer with `+`.

### Corrected version

```python
age = 20
print("Age: " + str(age))
```

`str(age)` converts the integer to a string before joining it with the other text.

## RecursionError

A `RecursionError` happens when a function calls itself too many times without stopping.

### Example that causes the error

```python
def count_down(number):
	count_down(number - 1)

count_down(3)
```

The function has no stopping condition, so it keeps calling itself.

### Corrected version

```python
def count_down(number):
	if number == 0:
		return
	count_down(number - 1)

count_down(3)
```

The base condition stops the function when `number` reaches `0`.

## AttributeError

An `AttributeError` happens when an object does not have the attribute or method you try to use.

### Example that causes the error

```python
name = "Asha"
print(name.uppercase())
```

Strings have an `upper()` method, but they do not have an `uppercase()` method.

### Corrected version

```python
name = "Asha"
print(name.upper())
```

The corrected code uses the string method that Python provides: `upper()`.
