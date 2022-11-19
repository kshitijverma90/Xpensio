def findstring():

    str = "Dear SBI User, your A/c X4954-debited by Rs50.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI"

    words = str.split()
    i=0
    str1=""
    str2=""
    str3=""

    for word in words :
        if word == 'by' and str1=='':
            str1=words[i+1]
        if word== 'on' and str2=='':
            str2=words[i+1]
        if word=='to' and str3=='':
            str3=words[i+1]
        i+=1
    # print (str1)
    # print(str2)
    # print(str3)  
    
    return [str1,str2,str3]