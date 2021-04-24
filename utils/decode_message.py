import numpy as np
import base64 

def xor_encrypt(tips,key):
    ltips=len(tips)
    lkey=len(key)
    secret=[]
    num=0
    for each in tips:
        if num>=lkey:
            num=num%lkey
        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1
    print(secret)
    return base64.b64encode( "".join( secret ).encode() ).decode()

def xor_decrypt(secret,key):
    tips = base64.b64decode( secret.encode() ).decode()
    print(tips)
    ltips=len(tips)
    lkey=len(key)
    secret=[]
    num=0
    for each in tips:
        if num>=lkey:
            num=num%lkey
        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1
    print(secret)
    return "".join( secret )

def encode_msg(sn,msg):
    """
    对整个短信进行加密
    """
    snBytes=sn.split(":")
    snBytes4=int("0x"+snBytes[4],16) #将sn字符转为16进制int
    msgInt=int.from_bytes(msg,'big')
    emsg=msgInt^snBytes4
    return emsg

def decode_msg(sn,msg):
    """
    input:
        sn:"00:A0:50:AD:5C:68"
        msg: 加密后的信息，每个字节(byte)第5个字节进行异或
        isByte:表示是否二进文件
    return:
        dmsg:先对每个字节与第5个字节进行异或
    """
    snBytes=sn.split(":")
    snBytes4=int("0x"+snBytes[4],16) #将sn字符转为16进制int
    #snBytes5=int("0x"+snBytes[5],16)
    num=len(msg)
    decodeMsg=b''
    for i in range(num):
        print(msg[i])
        dmsg=msg[i]^snBytes4
        decodeMsg+=bytes([dmsg])
    #print(decodeMsg)
    return decodeMsg.decode('utf8')
    

if __name__=="__main__":
    
    tips= "11234456qweqw中国人物"
    key= "owen"
    secret = xor_encrypt(tips,key)
    print( "cipher_text:", secret )
    plaintxt = xor_decrypt( secret, key )
    print( "plain_text:",plaintxt )
    
    
    f=open("C:/Users/zhyi/Desktop/test4(1).txt","rb")
    while True:
        line=f.readline()
        if not line:
            break
        else:
            print(line)
            dmsg=decode_msg("00:A0:50:AD:5C:68",line)
            print(dmsg)
    

