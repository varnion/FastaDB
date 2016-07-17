# FASTADB - A DATABASE FOR YOUR FASTA FILES

from Bio.SeqIO import parse
from fdb_registers import FDBRegister
from datetime import date


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

    def generate_fdb_file_header(self):
        dict_header = {}
        dict_header['FastaDB'] = 'GENOME.FDB'
        dict_header['ModifiedDate'] = date.today().strftime('%d-%m-%Y')

        return dict_header

    def mount_fdb_file(self, fdb_registers):
        if fdb_registers is None:
            return None

        dict_header = self.generate_fdb_file_header()
        fdb_file = dict_header

        for i_register in range(len(fdb_registers)):
            new_dict = fdb_registers[i_register].build_dictionary()
            new_dict['id'] = i_register

            fdb_file[str(i_register)] = new_dict

        return fdb_file

    def FastaToFDB(self, fastafile, username):
        fdb_registers = []
        content = open(fastafile, "r")

        sequences = parse(content, 'fasta')

        for sequence in sequences:
            fdb_register = FDBRegister()
            fdb_register.description = sequence.description
            fdb_register.gene = str(sequence.seq)
            fdb_register.geneinfo = sequence.annotations
            fdb_register.filename = fastafile
            fdb_register.date = date.today()
            fdb_register.user = username

            fdb_registers.append(fdb_register)

        content.close()

        return self.mount_fdb_file(fdb_registers)

    def ImportFasta(self, fastafile, username):
        try:
            return self.FastaToFDB(fastafile, username)
        except ValueError:
            return ValueError
