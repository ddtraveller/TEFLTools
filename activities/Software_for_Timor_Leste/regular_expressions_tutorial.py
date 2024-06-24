import re

# Introduction to regular expressions
print("Regular expressions (regex) are powerful tools for pattern matching and text manipulation.")
print("They allow you to search for specific patterns within text and perform operations based on those patterns.")

# Basic regex syntax
print("\nBasic regex syntax:")
text = "The quick brown fox jumps over the lazy dog."

# Literal characters
print("Matching literal characters:")
pattern = r"quick"
match = re.search(pattern, text)
print(f"Pattern '{pattern}' found at index: {match.start() if match else 'Not found'}")
# Explanation: This matches the exact word "quick" in the text.

# Metacharacters
print("\nUsing metacharacters:")
pattern = r"qu..k"
match = re.search(pattern, text)
print(f"Pattern '{pattern}' found at index: {match.start() if match else 'Not found'}")
# Explanation: The '.' metacharacter matches any single character, so this pattern matches "quick".

# Character classes
print("\nCharacter classes:")
text = "The year is 2023, and the date is 05/25."

print("Matching digits:")
pattern = r"\d+"
matches = re.findall(pattern, text)
print(f"Digits found: {matches}")
# Explanation: \d matches any digit, and + means "one or more", so this finds all sequences of digits.

print("\nMatching word characters:")
pattern = r"\w+"
matches = re.findall(pattern, text)
print(f"Words found: {matches}")
# Explanation: \w matches any word character (letters, digits, underscores), finding all "words".

# Quantifiers
print("\nQuantifiers:")
text = "aaa bbb ccccc"

print("Using '*' (zero or more):")
pattern = r"a*"
matches = re.findall(pattern, text)
print(f"Matches: {matches}")
# Explanation: a* matches zero or more 'a' characters.

print("\nUsing '+' (one or more):")
pattern = r"c+"
matches = re.findall(pattern, text)
print(f"Matches: {matches}")
# Explanation: c+ matches one or more 'c' characters.

# Anchors
print("\nAnchors:")
text = "hello world\nhello universe"

print("Using '^' (start of line):")
pattern = r"^hello"
matches = re.findall(pattern, text, re.MULTILINE)
print(f"Matches: {matches}")
# Explanation: ^ matches the start of a line, finding "hello" at the beginning of lines.

# Groups
print("\nGroups:")
text = "John Doe (john@example.com)"

print("Using groups to extract information:")
pattern = r"(\w+) (\w+) \((\w+@\w+\.\w+)\)"
match = re.search(pattern, text)
if match:
    print(f"Full Name: {match.group(1)} {match.group(2)}")
    print(f"Email: {match.group(3)}")
# Explanation: Parentheses create groups, allowing extraction of specific parts of the match.

# Backreferences
print("\nBackreferences:")
text = "hello hello world world"

print("Using backreferences to match repeated words:")
pattern = r"(\b\w+\b) \1"
matches = re.findall(pattern, text)
print(f"Repeated words: {matches}")
# Explanation: \1 refers back to the first group, matching repeated words.

# re.search() and re.match()
print("\nUsing re.search() and re.match():")
text = "Python is awesome"

print("re.search() (searches anywhere in the string):")
pattern = r"is"
match = re.search(pattern, text)
print(f"Pattern '{pattern}' found at index: {match.start() if match else 'Not found'}")
# Explanation: re.search() finds a pattern anywhere in the string.

print("\nre.match() (matches at the beginning of the string):")
pattern = r"Python"
match = re.match(pattern, text)
print(f"Pattern '{pattern}' matched: {'Yes' if match else 'No'}")
# Explanation: re.match() only matches at the beginning of the string.

# re.findall() and re.sub()
print("\nUsing re.findall() and re.sub():")
text = "The price is $10, $20, and $30"

print("re.findall() (finds all non-overlapping matches):")
pattern = r"\$\d+"
matches = re.findall(pattern, text)
print(f"Prices found: {matches}")
# Explanation: re.findall() returns all non-overlapping matches of the pattern.

print("\nre.sub() (replaces matches with a specified string):")
pattern = r"\$(\d+)"
replaced_text = re.sub(pattern, r"€\1", text)
print(f"Replaced text: {replaced_text}")
# Explanation: re.sub() replaces matches with a new string, using \1 to refer to the group.

# re.compile()
print("\nUsing re.compile():")
pattern = re.compile(r"\d+")
text1 = "There are 123 apples"
text2 = "We need 456 oranges"

print(f"Matches in text1: {pattern.findall(text1)}")
print(f"Matches in text2: {pattern.findall(text2)}")
# Explanation: re.compile() creates a reusable regex object, improving efficiency for multiple uses.

print("\nThis concludes our interactive tutorial on regular expressions in Python.")