from Bio import SeqIO
import os
import re

def check_motif(seq,motif):
  pattern = re.compile(fr'{motif}')
  matches = pattern.finditer(seq)
  matches = [match for match in matches]
  if len(matches) == 0:
    return None
  else:
    return matches

#motif = '(D|E).P.PLR(S|T)D'

#motif = 'P.PLR'

motif = '[DE].P.[PST]LR[ST]D'

print(motif)

print('STING_HUMAN Crtl +:',check_motif('GMEKPLPLRTDFS', motif))

direc = '../raw/TBK1_interacting_prots/'

files = os.listdir(direc)

for file in files:
  for record in SeqIO.parse(direc + file,'fasta'):
    print(record.id,check_motif(str(record.seq),motif))
