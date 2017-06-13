#coding:utf-8  

import sys  
def delete(filepath):  
    f=open(filepath,'r')  
    fnew=open(filepath+'.new','w')            #将结果存入新的文本中  
    for line in f.readlines(): 
 #对每一行先删除空格，\n等无用的字符，再检查此行是否长度为0  
        data=line.strip('\t')   
        if data!='\n' :
            fnew.write(data)  

    f.close()  
    fnew.close()  
  
  
if __name__=='__main__':  

    delete("out.merge6_10000len_300_D.format")
    delete("out.merge5_3000len_350_D.format")  
    delete("out.merge1_1000len_350_D.format") 
    delete("out.merge2_100len_400_D.format")  

