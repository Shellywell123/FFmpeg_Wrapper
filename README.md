# FFmpeg_Wrapper

Wrapper written in python3 to make concatenating mp4 video files more user friendly :)

### How to run:
Within a directory that contains mp4 files you want to concatenate, execute the program using python3. The program will then print out the file names of all the mp4's in your current directory.
```bash
foo@bar:~$ python3 mp4_combine.py

Mp4 files in current directory:
 - fileincurrentdir1.mp4
 - fileincurrentdir2.mp4
...
 - fileincurrentdirn.mp4
```
Program will then ask you to input the name of the mp4 files from the current directory that you want to concatenate. Input the file names including the '.mp4' extension in the order you would like them concatenated, seperating each file name with a comma.
```bash
which files do you want to combine (seperate with comma):
>> fileincurrentdir1.mp4,fileincurrentdir2.mp4,...fileincurrentdirn.mp4
```
After that the program will then ask you to give a name for the combined mp4 file, which will then be saved into your current directory.
```bash
what do you want to call the combined file (dont forget .mp4):
>> combinedfile.mp4
```
The program should then make you a new mp4 file in the current diretory out of the chosen ones.