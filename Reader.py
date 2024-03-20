class Reader:
    def __init__(self, string) -> None:
        self.charArray = [char for char in string]
        self.lastConsumed = 0

    def peek(self, k) -> None:
        return self.charArray[self.lastConsumed+k]

    def consume(self, k) -> None:
        self.lastConsumed = self.lastConsumed+k
        return self.charArray[self.lastConsumed]
