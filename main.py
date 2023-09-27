# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import torch


# Press the green button in the gutter to run the script.
class Main:

    def __init__(self):
        print(torch.__version__)
        scalar = torch.tensor(7)
        print(scalar.item())
        vector = torch.tensor([[7, 7, 7],[1,2,3],[1,2,3]],)
        print(vector[1].ndim)
        print(vector.ndim)
        print(vector.tolist())
        print(vector)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


if __name__ == '__main__':
    Main()
