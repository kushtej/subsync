def synctime():
    import datetime as dt
    from . import color
    
    sub_start_min=int(input("Enter subtitle start min : "))
    sub_start_sec=int(input("Enter subtitle start sec : "))
    video_start_min=int(input("Enter video-audio start min : "))
    video_start_sec=int(input("Enter video-audio start sec : "))


    a = dt.datetime(100,1,1,0,video_start_min,video_start_sec)
    b = dt.datetime(100,1,1,0,sub_start_min,sub_start_sec)


    if('-' in str((a-b).total_seconds()) ):
        color.prYellow("\nTime Difference : ")
        color.prRed(str((a-b).total_seconds()))
        color.prRed(" seconds\n\n")
    else:
        color.prYellow("\nTime Difference : ")
        color.prGreen(str((a-b).total_seconds()))
        color.prGreen(" seconds\n\n")
