#!/bin/bash


insert_size=300 # 先不要计算dev,先计算出insert size
sdev=30
read_len=128
chr=chr1 # or else

samtools view NA12878.bam |awk '{if ($3=="chr1") print $0}' |head -n 2000|awk 'BEGIN{a=0;c=0;d=0} {if($2==147||$2==83||$2==163||$2==99) if ($9 < 0) $9 = -$9; a=a+1;c=c+$9;tmp=$9-297;if(tmp<0)tmp=-tmp;d=d+tmp } END{print c,a,d}'