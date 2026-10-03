def main():
    value = input("File name: ").lower()
    if value.endswith(".gif"):
        print("image/gif")
    elif value.endswith(".jpg") or value.endswith(".jpeg"):
        print("image/jpeg")
    elif value.endswith(".png"):
        print("image/png")
    elif value.endswith(".pdf"):
        print("application/pdf")
    elif value.endswith(".txt"):
        print("text/plain")
    elif value.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
main()