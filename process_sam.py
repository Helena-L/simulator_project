import pysam
from prep_mm_tx import get_transcript_list

TX_NAME = {}
for i in range(1,20):
        TX_NAME[i] = "MOUSE_" + str(i)

mm_tx_list = get_transcript_list()

reads_for_transcripts = [[] for i in range(len(mm_tx_list))]


bamfile = pysam.AlignmentFile("starAligned.out.bam", "rb")
bam_iter = bamfile.fetch(until_eof=True)
for read in bam_iter:
        '''
        print ("get_reference_positions", read.get_reference_positions())
        print ("get_reference_sequence", read.get_reference_sequence())
        print ("reference_id", read.reference_id)
        print ("reference_name", read.reference_name)
        print ("reference_start (pos)", read.reference_start)
        print ("reference_end", read.reference_end)
        print ("reference_length", read.reference_length)
        print ("query_alignment_start", read.query_alignment_start)
        print ("query_alignment_end", read.query_alignment_end)
        print ("query_alignment_length", read.query_alignment_length)
        print ("query_alignment_sequence", read.query_alignment_sequence)
        print ("query_sequence", read.query_sequence)
        '''
        if read.reference_name not in TX_NAME.values():
                        continue
        find = False
        for i in range(len(mm_tx_list)):
        # for tx_idx, tx_record, tx_chr_num, tx_len, tx_st, tx_end in mm_tx_list:
        # [i, record, int(chr_num), len(record), ref_start, ref_end]
                tx_idx, tx_record, tx_chr_num, tx_len, tx_st, tx_end = mm_tx_list[i]
                if (read.reference_name == TX_NAME[tx_chr_num]):
                        if ((tx_st <= read.reference_start) and (read.reference_end <= tx_end)):
                                find = True
                                print ("tx index: ", tx_idx)
                                print ("tx info: ", TX_NAME[tx_chr_num], tx_st, tx_end)
                                print ("read info: ", [read.query_sequence, read.reference_start, read.reference_end])
                                reads_for_transcripts[i].append([read.query_sequence, read.reference_start, read.reference_end])
                if (find):
                        break

print (reads_for_transcripts)
print ("\n\n\n")
print ([len(x) for x in reads_for_transcripts])