import pickle

# ===== Pickle Functions =====
def save_pickle(a_var, a_file):
    with open(a_file, "wb") as file_handler:
        try:
            pickle.dump(a_var, file_handler, protocol=pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print("Error saving pickle:", a_file)
            print(e)
            return False


def load_pickle(a_file):
    with open(a_file, 'rb') as handle:
        object_file = pickle.load(handle)
    return object_file


# Sometimes I rename it in my head.
def read_pickle_file(a_file):
    return load_pickle(a_file)
