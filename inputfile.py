from Bio import SeqIO #module to break fastq format
count = 0
for file in 'number1.fq', 'number2.fq': #get files
    for seq_record in SeqIO.parse(file, "fastq"):
        count = count +1
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))
        seq_id = seq_record.id
        seq_id = seq_id.split(':')
        print(seq_id)
        print(count)
        xpos = seq_id[5]    #gets the x-cordinate
        ypos = seq_id[6]    #gets the y-cordinate

        print(xpos)         #gets x,y for ploting in QGIS
        print(ypos)
