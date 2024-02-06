a = input("File name: ")

b = a.split(".")

match b[-1].strip():
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf" | "PDF":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case "bin" | _:
        print("application/octet-stream")
