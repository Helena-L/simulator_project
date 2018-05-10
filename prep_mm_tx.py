from Bio import SeqIO
import re

# check if the transcript only have one isoform
# record the transcript

# Mouse chrosomes: 1-19 + X/Y
# Consider 1-19

chr_name_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', \
	'11', '12', '13', '14', '15', '16', '17', '18', '19']

def get_ref_positions(description_str):
	re_exp = '(?<=GRCm38:).+:[0-9]+:[0-9]+:'
	m = re.search(re_exp, description_str)
	# print (description_str)
	match_str = (m.group(0))
	chr_num, ref_start, ref_end, _ = match_str.split(":")
	return (chr_num), int(ref_start), int(ref_end)

def get_transcript_list():
	transcript_list = []
	i = 0
	fasta = SeqIO.parse("Mus_musculus.GRCm38.cdna.all.fa", "fasta")
	for record in fasta:
		chr_num, ref_start, ref_end = get_ref_positions(record.description)
		# check if the transcript only has one isoform
		if ( (chr_num in chr_name_list) and ((ref_end - ref_start + 1) == len(record)) and len(record) > 200):
			transcript_list.append([i, record, int(chr_num), len(record), ref_start, ref_end])
		i += 1
	return transcript_list

transcript_list = get_transcript_list()
print (len(transcript_list))
# print ("\n")

# print (transcript_list[:10])
