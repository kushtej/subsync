# Subtitle Synchronization

We all have faced problem when it comes to syncing subtitles with a movie or a video we are watching.This is a raw script to sync subtitles with audio/video written in **python**.

## Setting up the script  

**Step 1 :** Download the subsync script from [https://github.com/kushtej/subsync](https://github.com/kushtej/subsync).

**Step 2 :** Type the following commands in the Terminal.
```
$ chmod +x subsync
$ mv subsync /usr/local/bin/
```
## Usage :

The subsync script contains 2 options
-  `--sync-time`
-  `--calibrate`

The script also contains `--help` option to elaborate the content in the terminal.

### 1. subsync --sync-time
  
The `--sync-time` option finds haste or delay between video/audio and subtitle. The input to this option is in minutes and seconds of subtitle and video-audio. The output is the time difference between the video-audio and subtitle. This output can then be used in the `--calibrate` option to sync the subtitle. The difference will be **-seconds** if its a haste and **+seconds** if its a delay.

  

**Sample Output :**

**(i).** If in a movie, The subtitle starts at 00:01:33 (HH:MM:SS) and audio/video starts at 00:01:54
```
$ subsync --sync-time

Type : INT (Input in number only)
Enter subtitle start min : 1
Enter subtitle start min : 33
Enter video-audio start min : 1
Enter video-audio start sec : 54
```
Then, The Time Difference is in haste and the output would look like this.
```
Time Difference : 21.0 seconds
```

**(ii).** If in a movie, The subtitle starts at 00:01:32 (HH:MM:SS) and audio/video starts at 00:01:17

```
$ subsync --sync-time

Type : INT (Input in number only)
Enter subtitle start min : 1
Enter subtitle start min : 32
Enter video-audio start min : 1
Enter video-audio start sec : 17
```
Then, The Time Difference is in haste and the output would look like this.
```
Time Difference : -15.0 seconds
```
### 2. subsync --calibrate

The `--calibrate` option is used to sync the subtitle with the audio-video with the delay/haste seconds found in `--sync-time` option. It inputs **file_name.srt** and the number of seconds in delay or haste.
Then, The file is calibrated to the given time and the output file is generated by the name of **sync_filename.srt** 

**Sample output :**

```
$ subsync --calibrate

  Type : TEXT (Input in text only)
  File Name : subtitlename.srt
  Type : INT (Input in number only)
  Seconds : 21

  1.Delay[D/d]	2.Hasten[H/h]
  Choose[Hh/Dd] = d

  File Name : subtitlename.srt
  Delay : 21 seconds

  SUCCESS!
  File Generated : sync_subtitlename.srt
```
**Note:** Make sure you are in the same directory as `subtitlename.srt` or provide `/absolute/path/to/subtitename.srt`

> **Note:** The script and documentation is only refrenced to linux system.

> **Note:** The below code is a raw script and needs revision.If you notice any error in the code or optimize the code then feel free to post it in the comment section or collaborate to the gist.

*Thank You for using my code :)*
