# FFmpeg_Wrapper

Wrapper written in python3 written to make concatenating video files mre user friendly :)

### How to run:
```bash
foo@bar:~$ python3 mp4_combine.py
Mp4 files in current directory:
 - fileincurrentdir1.mp4
 - fileincurrentdir2.mp4
...
 - fileincurrentdirn.mp4
which files do you want to combine (seperate with comma):
```
```bash
fileincurrentdir1.mp4,fileincurrentdir1.mp4,...fileincurrentdirn.mp4
```
what do you want to call the combined file (dont foget .mp4):
```bash
combinedfile.mp4
```