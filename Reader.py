# by neverfriendme
def func():
    extensions = (".cpp", ".hpp", ".h", ".cxx", ".hxx", ".py", ".pyc", ".pyd", ".pyo", ".pyw", ".pyx", ".pxd", ".pxi", ".pyzw", ".js", ".C", ".c")
    Choices = ["read", "quit"]
    choice = input("read to read the contents of a file or quit:\n").strip().lower()
    if choice == Choices[0]:
        directory = input("What is the file you want to open (Please input the directory correctly):\n")
        if not directory.endswith(extensions):
            warning = input("Are you sure? The file you are entering could contain malware.Y/N:").strip().upper()
        if warning == "Y":
            pass
        elif warning == "N":
            print("Quiting for your safety")
            quit()
        try:
            with open(directory, "r") as file:
                text = file.read()
                print(text)
        except FileNotFoundError:
            print("File was not found")
        except PermissionError:
            print("You don't have permission to read this file")
        except IOError:
            print("An error occurred while trying to read the file")
        except Exception as e:
            print("An unexpected error occurred:", str(e))
    elif choice == Choices[1]:
        print("Quiting")
        return
    else:
        print("Invalid")
        return

func()


