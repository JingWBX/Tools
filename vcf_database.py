#coding:utf-8 

import pysam
from pysam import VariantFile
import os  
import math
import numpy as np


def create_vcf_1(chrom):
	vcffile = pysam.VariantFile('/mnt/hde/gao/wj/vcf/ALL.wgs.integrated_sv_map.20130502.svs.genotypes.vcf.gz')
	sample = 'NA12878'
	header=vcffile.header
	scan_l_pos=0
	scan_r_pos = header.contigs[chrom].length

	sample_vcffile = open("/mnt/hde/gao/wj/NA12878.chrom.all.SV.vcf", "a")
	count=0
	for rec in vcffile.fetch(chrom, scan_l_pos, scan_r_pos):
		gt= rec.samples['NA12878']['GT']
		if (gt[0]+gt[1])>0:
			p1= rec.start
			p2= rec.stop
			print (rec.info['SVTYPE'])
			print (rec.start)
			print (p2)
			count=count+1
			sample_vcffile.write('('+str(chrom)+","+str(rec.info['SVTYPE'])+','+str(p1)+","+str(p2)+")"+'\t')

	sample_vcffile.write('\n') #注意，每行是同一个染色体的所有变异，每行末尾是'\t\n'
	print ("SV总个数为： "),
	print (count)
	sample_vcffile.close()
	vcffile.close()
def create_vcf_2(chrom):
	chrom='chr'+chrom
	vcffile = pysam.VariantFile('/mnt/hde/gao/wj/vcf/NA12878_hg19_deletions.vcf.gz')
	sample = 'NA12878'
	scan_l_pos=0
	scan_r_pos = 500000000 	

	sample_vcffile = open("/mnt/hde/gao/wj/SV_image/NA12878.chrom.all.SV.v2.vcf", "a")
	count=0
	for rec in vcffile.fetch(chrom, scan_l_pos, scan_r_pos):
		gt= rec.samples['27055']['GT']
		if (gt[0]+gt[1])>0:
			p1= rec.start
			p2= rec.stop
			print (rec.info['SVTYPE'])
			print (rec.start)
			print (p2)
			count=count+1
			sample_vcffile.write('('+str(chrom)+","+str(rec.info['SVTYPE'])+','+str(p1)+","+str(p2)+")"+'\t')

	sample_vcffile.write('\n') #注意，每行是同一个染色体的所有变异，每行末尾是'\t\n'
	print ("SV总个数为： "),
	print (count)
	sample_vcffile.close()
	vcffile.close()

def main():
	chrom=[]
	for t in range(22): #chrom ['1','2'...'22','X','Y']
		chrom.append(str(t+1))
	chrom.append('X')
	# chrom.append('Y') #没有Y，这是个女性
	for i in chrom:
		create_vcf_2(i)


if __name__ == '__main__':
	main()

#生成vcf索引文件
#bgzip -c NA12878.low.vcf > NA12878.low.vcf.gz
#tabix -p vcf NA12878.low.vcf.gz 

