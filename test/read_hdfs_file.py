import pyhdfs
import pandas as pd
import time

fs= pyhdfs.HdfsClient(hosts='192.168.2.21:50070', user_name='root')
def concatFiles(sourcePath,targetPath,concateDate,remove=False):
    """
    根据时间合并小文件
    params:
        sourcePath=targetPath(只能同目录合并)
        concateDate:2020-10-10 23:40:00
        remove:删除length=0的文件
    """
    fileNameList=fs.listdir(sourcePath)
    fileList=[]
    timeStamp=int(time.mktime(time.strptime(concateDate,"%Y-%m-%d %H:%M:%S")))
    for fileName in fileNameList:
        if fileName.endswith(".json"):
            filePath=sourcePath+fileName
            fileStatus=fs.get_file_status(filePath)
            if fileStatus["length"]==0 and remove:
                fs.delete(filePath)
            if fileStatus["length"]>0 and fileStatus["modificationTime"]/1000<timeStamp:
                fileList.append(filePath)
    if len(fileList)>0:
        if not fs.exists(targetPath):
            fs.create(targetPath,"")
        fs.concat(targetPath,fileList)
    return fileList
    


#print(fs.listdir('/data/dev/dwdata/dwd_event_log'))
inputFile=fs.open("/data/dev/dwdata/dwd_event_log/part-00002-d346bcc1-c2fa-45b2-9c70-93ec2062bf92-c000.json")
print(fs.list_status("/data/dev/dwdata/dwd_event_log/part-00001-67b5a9b2-ecd6-411c-a709-f0562606ac5c-c000.json"))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
concatFiles("/data/dev/rawdata/dwd_account/","/data/dev/testdata/ods_event_log/new_2.json",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),remove=True)
df=pd.read_json(inputFile,lines=True)
#print(df["location"])