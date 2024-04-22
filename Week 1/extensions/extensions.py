# Prompt user for name of a file then output the media type

ask_for_file = (input("File name: ")).lower().strip()


if ask_for_file.endswith(".gif"):
    print("image/gif")
elif ask_for_file.endswith(".jpg"):
    print("image/jpeg")
elif ask_for_file.endswith(".png"):
    print("image/png")
elif ask_for_file.endswith("jpeg"):
    print("image/jpeg")
elif ask_for_file.endswith(".pdf"):
    print("application/pdf")
elif ask_for_file.endswith(".txt"):
    print("text/plain")
elif ask_for_file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
