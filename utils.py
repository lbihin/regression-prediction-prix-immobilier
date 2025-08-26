import pickle


RANDOM_STATE = 0
TEST_SIZE = 0.2
ALPHA = 0.02
TARGET = "SalePrice"


def sauvegarder_model(
    model,
    file_name: str = "../data/models/best-model",
    timestamp=None,
    only_latest: bool = False,
):
    if not only_latest:
        with open(f"{file_name}-{str(timestamp)}.pkl", "wb") as f:
            pickle.dump(model, f)
    with open(f"{file_name}-latest.pkl", "wb") as f:
        pickle.dump(model, f)


def ouvrir_model(file_name: str = "../data/models/best-model-latest.pkl"):
    with open(file_name, "rb") as f:
        clf = pickle.load(f)
    return clf
