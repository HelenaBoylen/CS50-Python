# Prompt for a greeting. If output = hello return $0, If output starts with H return $20 else $100

greeting = input("Hi There ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")


