class EvenOddIdentifier:
    def __init__(self, filename: str = "./numbers.txt"): # sets up the first state
        self.filename = filename

    def read_file(self) -> list[int]:
        try:
            with open(self.filename, "r") as file:
                return [int(num.rstrip("\n")) for num in file.readlines()]
        except:
            print("Ensure that the file exists with integers only and is readable.")

    def write_file(self, filename: str, content: int):
        with open(filename, "a") as file:
            file.write(f"{content}\n")

    def categorize(self):
        data = self.read_file()
        for number in data:
            if number % 2 == 0:
                self.write_file("even.txt", number)
            else:
                self.write_file("odd.txt", number)
