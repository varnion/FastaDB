# FASTADB - A DATABASE FOR YOUR FASTA FILES

class FastaDB():
    def __init__(self):
        self.filename = ""

    def DB(self, filename):
        """
        Function for loading the database file
        :param: filename
        """
        try:
            self.filename = filename
            file = open(filename, "r+")
        except:
            self.filename = filename
            file = open(filename, "w")

        return file

    def ImportFasta(self):
        f = open(self.filename, "r+")



FDB = FastaDB()
FDB.DB("file3.fdb")
FDB.InsertFasta()
