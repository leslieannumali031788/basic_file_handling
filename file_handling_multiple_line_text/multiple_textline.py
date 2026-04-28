class WriteMultipleLineText:
    def __init__(self, filename: str = "mylife.txt"):
        self.filename = filename

    def write_multiple_textlines(self):
        try:
            with open(self.filename, "a") as file:
                while True:
                    line = input("Enter line: ")
                    file.write(f"{line}\n")

                    more = input("Enter more text: ").lower()
                    if more == "y":
                        print("Saved")
                        break

        except Exception as error:
            print(f"Something went wrong: {error}")

if __name__ == "__main__":
    writer = WriteMultipleLineText()
    writer.write_multiple_textlines()