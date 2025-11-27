class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("opening")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing")
        self.file.close()

# Now it works:
with FileManager("demo.txt", "w") as f:
    f.write("Hello!")
