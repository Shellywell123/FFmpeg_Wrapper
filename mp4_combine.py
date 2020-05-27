import os

print('Mp4 files in current directory:')
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if (f[-4:]=='.mp4') or (f[-4:]=='.MP4'):
        print(' - '+f)

videos = input('which files do you want to combine (seperate with comma):\n')
comb_flie_name = input('what do you want to call the combined file (dont foget .mp4):\n')

n = len(videos.split(','))

current_dir = os.getcwd()
current_dir = current_dir.replace(' ','\ ')+'/'

filesinfo = ''
for m in range(0,n):
    filesinfo = filesinfo +' -i '+current_dir+ videos.split(',')[m]
   
final_os_command = 'ffmpeg {} -filter_complex concat=n={}:v=1:a=1 -f MOV -y {}'.format(filesinfo,n,comb_flie_name)
os.system(final_os_command)