# FASTADB - A DATABASE FOR YOUR FASTA FILES
from Bio.SeqIO import FastaIO, parse

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
        sequences = parse(open(fastafile), 'fasta')
        for fasta in sequences:
            name, sequence = fasta.id, str(fasta.seq)
            print(name, sequence)


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
