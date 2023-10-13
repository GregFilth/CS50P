file_name = input("File name: ").strip().lower()

number = file_name.rfind('.')
replacement = file_name[:number]
file_name = file_name.replace(replacement, "")

match file_name:
    case ".gif":
        print("image/gif")

    case ".jpg":
        print("image/jpeg")

    case ".jpeg":
        print("image/jpeg")

    case ".png":
        print("image/png")

    case ".pdf":
        print("application/pdf")

    case ".txt":
        print("text/plain")

    case ".zip":
        print("application/zip")

    case _ :
        print("application/octet-stream")