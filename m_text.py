import re

title = "Regular Expressions (regex)/By Allegsu"
print(title)

lower_outcome = "HELLO WORLD".lower()
print(f"Lower Outcome: {lower_outcome}")

upper_outcome = "hello world".upper()
print(f"Upper Outcome: {upper_outcome}")

x = "let's divide the string into an array".split(" ")
print(f"Split String: {x}")

" ".join(x)
print(f"Join: {x}")

y = "let's divide the chain into an array"
len(y)
print(f"Length: {len(y)}")

y.count("a")
print(f"Letter Count into the string (a): {y.count("a")}")

show_string_part = y[0:14]
print(f"Part of a String: {show_string_part}")

x1 = "cat"

pattern1 = re.compile("c.t")
print(f"Exact Match Check: {pattern1.search(x1)}")

pattern2 = re.compile(r"ca?")
print(f"Optional Character Match: {pattern2.search(x1)}")

pattern3 = "ca{1,2}t"
re.search(pattern3, x1)
print(f"Repetition Match: {re.search(pattern3, x1)}")
