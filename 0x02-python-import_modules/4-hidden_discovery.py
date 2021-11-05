#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for xx in dir(hidden_4):
        if xx[:2] != "__":
            print(xx)
