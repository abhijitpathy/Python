print("1-> search book,2-> Issue box, 3-> Return book, 4 ->  view Issued Books, 5 -> Exit")
library = int(input("enter library menu to choice"))

match library:
    case 1:
        print("Search Book n")
     
    case 2:
        print("Issue Book")
    case 3:
        print("Returned book")
    case 4:
        print("View Issued Books")
    case 5:
        print("exit")
    case _:
        print("invalid choice")