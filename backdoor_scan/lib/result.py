class Result:
    def __init__(self):
        self.image_id = ""
        self.image_ref = ""
        self.filepath = ""
        self.description = ""

    def __str__(self):
        str = ""
        str = str + "+----------------------------------------------------------------------------------------------+\n"
        str = str + "| 📑ImageName: " + self.image_ref + "\n"
        str = str + "| 📑Filepath: " + self.filepath  + "\n"
        str = str + "| 📑Description: " + self.description + "\n"
        str = str + "+----------------------------------------------------------------------------------------------+\n"
        return str

