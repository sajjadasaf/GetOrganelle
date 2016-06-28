def read_fasta(fasta_dir):
    fasta_file = open(fasta_dir, 'rU')
    names = []
    seqs = []
    this_line = fasta_file.readline()
    while this_line:
        if this_line.startswith('>'):
            names.append(this_line[1:].strip())
            this_seq = ''
            this_line = fasta_file.readline()
            while this_line and not this_line.startswith('>'):
                this_seq += this_line.strip()
                this_line = fasta_file.readline()
            seqs.append(this_seq)
        else:
            this_line = fasta_file.readline()
    fasta_file.close()
    return [names, seqs]
    
in_fasta = raw_input('fasta:').strip()
f_matrix = read_fasta(in_fasta)
for i in xrange(len(f_matrix[0])):
    f_matrix[0][i] = 'noncoding '+f_matrix[0][i]
i = 0
del_count = 0
seq_sets = set()
while i < len(f_matrix[0]):
    if len(f_matrix[1][i]) < 50 or f_matrix[1][i] in seq_sets:
        del f_matrix[0][i]
        del f_matrix[1][i]
        del_count += 1
    else:
        seq_sets.add(f_matrix[1][i])
        i += 1
print 'delete', del_count
out_fasta = open(in_fasta+'.new.fasta', 'wb')
for i in xrange(len(f_matrix[0])):
    out_fasta.write('>'+f_matrix[0][i]+'\n'+f_matrix[1][i]+'\n')
out_fasta.close()