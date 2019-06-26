import os

cleanpath='C:/Users/Maxbe/Desktop/Capstone/wireshark-1.2-fixed'
filecount,validfiles,linecount=0,0,0
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
for root, directories, filesnames in os.walk(cleanpath):
    for filename in filesnames:
        filecount+=1
        fullpath=os.path.join(root,filename)
        name,ext=os.path.splitext(filename)
        if ext in ['.py','.h','.c','.cpp','.xml','.html','.sh']:
            validfiles+=1
            linecount+=file_len(fullpath)
print('The number of files in the codebase is '+str(filecount))
print('The number of valid files in the codebase is '+str(validfiles))
print('The number of lines in the code is '+str(linecount))
