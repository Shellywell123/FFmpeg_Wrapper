# FFmpeg_Wrapper

Wrapper written in python3 to make concatenating mp4 video files more user friendly :)

### How to run:
```bash
foo@bar:~$ python3 mp4_combine.py

Mp4 files in current directory:
 - fileincurrentdir1.mp4
 - fileincurrentdir2.mp4
...
 - fileincurrentdirn.mp4
```
```bash
which files do you want to combine (seperate with comma):
>> fileincurrentdir1.mp4,fileincurrentdir1.mp4,...fileincurrentdirn.mp4
```
```bash
what do you want to call the combined file (dont foget .mp4):
>> combinedfile.mp4
```