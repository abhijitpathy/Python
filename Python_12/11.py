file_type= (input("Enter file extension :")).lower()

match file_type:
    case "pdf":
        print("Document")
    case "jpg":
        print("image")
    case "png":
        print("image")
    case "mp3":
        print("Audio")
    case "mp4":
        print("video")
    case _:
        print("Invalid Choice")