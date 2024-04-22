# Check for answer 42 in any form by stipping spaces and making lowercase.

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

if answer == "42" or answer == "forty-two" or answer =="forty two":
    print("Yes")
else:
    print("No")
