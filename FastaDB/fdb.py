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

    def FastaToFDB(self, fastafile):
        content = open(fastafile,"r")
        fdbformat = {}
        for line in content:
            if line.startswith(">") == True:
                print("COORDENADA")

            if line.startswith(";") == True:
                print("Comentário")


            if line.startswith(";") == False and line.startswith(">") == False:
                print("sequencia")

    def ImportFasta(self, fastafile):
        try:
            a = open(fastafile, "r")
            f = open(self.filename, "r+")
            #print(a.read())
            FastaDB().FastaToFDB(fastafile)
        except ValueError:
            return ValueError



FDB = FastaDB()
FDB.DB("file3.fdb")
FDB.ImportFasta("test.fasta")
