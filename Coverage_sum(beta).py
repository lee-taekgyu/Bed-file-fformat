import sys
import argparse
import time
import gzip

start_time = time.time()

Chromosome = []
for num in range(1,23):
	Chromosome.append('chr'+str(num))
Chromosome.extend(['chrX','chrY'])


with open(sys.argv[2], 'r') as bed:
	bed_pos = {}
	for bed_line in bed:
		bed_line = bed_line.strip()
		bed_line_list = bed_line.split('\t')
		bed_chr = bed_line_list[0]
		bed_start = bed_line_list[1]
		bed_end = bed_line_list[2]
		bed_enrich = bed_line_list[6]
		bed_pos[bed_chr +" "+ bed_start +" "+ bed_end] = {}
#		bed_pos[bed_chr +" "+ bed_start +" "+ bed_end][bed_enrich] = {}

with open(sys.argv[1], 'r') as CpG:
	CpG_info = {}
	for cpg_line in CpG:
		cpg_line = cpg_line.strip()
		cpg_line_list = cpg_line.split('\t')
		cpg_chr = cpg_line_list[0]
		cpg_pos = cpg_line_list[1]
		cpg_character = []
		for num in range(2,len(cpg_line_list)):
			cov = cpg_line_list[num].split(';')[0:2]
			cov = ','.join(cov)
			cpg_character.append(cov)
		cpg_character = tuple(map(str,cpg_character))
		CpG_info[cpg_chr+" "+cpg_pos] = cpg_character


check_duplicate = []


def search_position():
	for key_bed in bed_pos.keys():
		for key_cpg in CpG_info.keys():
			if key_cpg.split(" ")[0] == key_bed.split(" ") and int(key_bed.split(" ")[1]) <= int(key_cpg.split(" ")[1]) <= int(key_bed.split(" ")[2]):
