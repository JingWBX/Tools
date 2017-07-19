#!/bin/bash

samtools view xx.bam |awk '{if ($3=="20") print $0}' |head -n 2000|   \
awk 'BEGIN{ID=0;c=0} {if($2==147||$2==83||$2==163||$2==99) if ($9 < 0) $9 = -$9; ID=ID+1;c=c+$9 } END{print c,ID} '
# 用c % ID 就是大概 insert size

insert_size=300 # 先不要计算dev,先计算出insert size
sdev=30
read_len=128
chr=chr1 # or else

# 假设我们现在算出来insert size 是 297
samtools view NA12878.bam |awk '{if ($3=="chr1") print $0}' |head -n 2000|  \
awk 'BEGIN{a=0;c=0;d=0} {if($2==147||$2==83||$2==163||$2==99) if ($9 < 0) $9 = -$9; a=a+1;c=c+$9;tmp=$9-297; \
     if(tmp<0)tmp=-tmp;d=d+tmp*tmp } END{print c,a,d}'
# d % a 再开方就是大概的
