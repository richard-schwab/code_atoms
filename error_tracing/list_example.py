import traceback

def make_list_error():
    empty_list = []
    tb = None
    try:
        first_item = empty_list[0]

    except IndexError:
        tb = traceback.format_exc()
        pass

    if not tb:
        print("\nProgram ran successfully.\n")
    else:
        print("Program failed.")
        print("Program received the following error:\n")
        print(tb)


if __name__ == "__main__":
    make_list_error()
