from pathlib import Path 
BASE_PATH = Path(__file__) / ".." / ".." / ".." / "Markdowns"

class Markdowns():
    def __init__(self):
        pass
    def ML_models(self,Filename="NA"):
        try:
            return (BASE_PATH / f"{Filename}.md").read_text()
        except FileNotFoundError:
            return (BASE_PATH / f"NA.md").read_text()


# if __name__ == "__main__":
#     test = Markdowns()
#     print(test.ML_models())