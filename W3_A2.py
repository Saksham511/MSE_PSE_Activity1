class FileRead:
    def __init__(self,filepath):
        self.filepath = filepath

    def readandappend(self):
        filepath = self.filepath
        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\nEnd of file\n")
        f.close()

        with open(filepath, "r", encoding="utf-8") as f:
            content=f.read()
            print(content)
        f.close()

def main():
    obj1 = FileRead("demo_file.txt")
    obj1.readandappend()

if __name__=="__main__":
    main()