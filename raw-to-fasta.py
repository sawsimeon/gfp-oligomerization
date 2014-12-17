#!/usr/bin/env python
'''Converts raw data in Excel format to FASTA format.'''

import sys
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC

def to_fasta(row):
    s = SeqRecord(Seq(row['Amino Acid Sequence'].replace('\n',''),
                                    IUPAC.protein))
    s.id = '%s' % row['Number']
    s.description = '%s|%s' % (row['Name'],
                        row['Oligomerization State'])

    SeqIO.write(s, sys.stdout, 'fasta')


sys.stderr.write('Reading the Excel file...\n')
data = pd.read_excel(sys.argv[1], 0)

sys.stderr.write('Writing the FASTA file...\n')
data.apply(to_fasta, axis=1)

