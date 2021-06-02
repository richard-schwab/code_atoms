import traceback


def get_error(print_error=False):
    tb = None
    try:
        raise ValueError
    except ValueError:
        tb = traceback.format_exc()
    else:
        tb = "No error"
    finally:
        if print_error:
            print(tb)
    return tb


if __name__ == "__main__":
    print("Program began running.\n")
    the_error = get_error(print_error=True)
    print("Program finished running.")
