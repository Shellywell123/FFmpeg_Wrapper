import os
import readline 

##########################################################################

def set_tab_complete_options(options):
    """
    allows user to tab complete inputs
    """

    readline.parse_and_bind("tab: complete")

    def complete(text,state):
        if text:
            results = [s for s in options if s and s.startswith(text)]
        else: 
            results = results[:]

        return results[state]

    readline.set_completer(complete)

##########################################################################

print('Mp4 files in current directory:')
files = [f for f in os.listdir('.') if os.path.isfile(f)]

tab_list = []
for f in files:
    if (f[-4:]=='.mp4') or (f[-4:]=='.MP4'):
        print(' - '+f)
        tab_list.append(f)

set_tab_complete_options(tab_list)
videos = input('which files do you want to combine (seperate with comma):\n')
comb_flie_name = input('what do you want to call the combined file (dont forget .mp4):\n')

n = len(videos.split(','))

current_dir = os.getcwd()
current_dir = current_dir.replace(' ','\ ')+'/'

filesinfo = ''
for m in range(0,n):
    filesinfo = filesinfo +' -i '+current_dir+ videos.split(',')[m]
   
final_os_command = 'ffmpeg {} -filter_complex concat=n={}:v=1:a=1 -f MOV -y {}'.format(filesinfo,n,comb_flie_name)
os.system(final_os_command)