def hasten(time,sec):
    import datetime
    a = datetime.datetime(100,1,1,int(time[0]),int(time[1]),int(time[2]))
    b = a - datetime.timedelta(seconds=sec)
    return b.time()   


def delay(time,sec): 
    import datetime
    a = datetime.datetime(100,1,1,int(time[0]),int(time[1]),int(time[2]))
    b = a + datetime.timedelta(seconds=sec)
    return b.time()


def calibrate():

    from . import color

    color.prCyan("\nType : TEXT (Input in text only)")
    color.prYellow("\nFile Name : ")
    name=input()
    
    color.prCyan("\nType : INT (Input in number only)\n")
    color.prYellow("Seconds : ")
    sec=int(input())

    ch=input("\n1.Delay[D/d]\t2.Hasten[H/h]\n\nChoose[Hh/Dd] = ")

    f=open(name,"r")
    f1=open("sync_"+name,"w")

    if(ch=='D' or ch=='d'):
        color.prYellow("\nFile Name : ")
        print(str(name))
        color.prYellow("Delay : ")
        print(str(sec)+" seconds")

    elif(ch=='H' or ch=='h'):
        color.prYellow("\nFile Name : ")
        print(str(name))
        color.prYellow("Hast : ")
        print(str(sec)+" seconds")
    else:
        color.prRed("\nEnter Valid Choice\n\n")
        exit(0)

    for line in f:
        all_line=line.split()
        if('-->'in all_line):
            if(ch=='D' or ch=='d'):
                #start_time
                start_time=all_line[0].split(":")
                start_time_end=start_time[2].split(",")[1]
                start_time=[re.sub(',.*$', '', i) for i in start_time]
                delayed_start_time=delay(start_time,sec)

                #end_time
                end_time=all_line[2].split(":")
                end_time_end=end_time[2].split(",")[1]
                end_time=[re.sub(',.*$', '', i) for i in end_time]
                delayed_end_time=delay(end_time,sec)

                #writing to file
                f1.write(str(delayed_start_time)+','+str(start_time_end)+' --> '+str(delayed_end_time)+','+str(end_time_end))
                f1.write("\n")

            elif(ch=='H' or ch=='h'):
                #start_time
                start_time=all_line[0].split(":")
                start_time_end=start_time[2].split(",")[1]
                start_time=[re.sub(',.*$', '', i) for i in start_time]
                hastened_start_time=hasten(start_time,sec)
        
                #end_time
                end_time=all_line[2].split(":")
                end_time_end=end_time[2].split(",")[1]
                end_time=[re.sub(',.*$', '', i) for i in end_time]
                hastened_end_time=hasten(end_time,sec)

                #writing to file
                f1.write(str(hastened_start_time)+','+str(start_time_end)+' --> '+str(hastened_end_time)+','+str(end_time_end))
                f1.write("\n")

        else:
            f1.write(line)

    color.prGreen("\nSUCCESS!\n")
    print("File Generated : sync_"+name)
    print("")
