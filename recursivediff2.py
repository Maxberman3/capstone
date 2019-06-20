import difflib
import pathlib
import os

buggypath='C:/Users/Maxbe/Desktop/Capstone/dspace-6.2-sate6/dspace-6.2-buggy'
cleanpath='C:/Users/Maxbe/Desktop/Capstone/dspace-6.2-sate6/dspace-6.2-fixed'
buggyfilelist=[]
cleanfilelist=[]
for root, directories, filesnames in os.walk(buggypath):
    for filename in filesnames:
        buggyfilelist.append(os.path.join(root,filename))
for root, directories, filenames in os.walk(cleanpath):
    for filename in filenames:
        cleanfilelist.append(os.path.join(root,filename))
both=zip(buggyfilelist,cleanfilelist)
diffs=[]
filepathlist=[]
for bugfilepth,cleanfilepth in both:
    # print(bugfilepth)
    # ext=pathlib.PurePosixPath(bugfilepth).suffixes
    # if len(ext)==2:
    #     ext=ext[1]
    # elif len(ext)>2:
    #     first=ext[-2]
    #     second=ext[-1]
    #     ext=''.join(first)
    #     ext=ext.join(second)
    # print(ext)
    # if ext in ['.pdf','.properties','.doc','.docx','.ico','.gif','.jpg','.png','.eot','.ttf','.woff','.zip','.psd','.min.js','..custom\redmond\images\animated-overlayg.custom\redmond\images\animated-overlayi.custom\redmond\images\animated-overlayf']:
    #     continue
    name,ext=os.path.splitext(bugfilepth)
    if ext in ['.java','.js','.jsp','.py','.xml','.html','.sh','.class']:
        if '.min' not in bugfilepth:
            bugfile=open(bugfilepth).readlines()
            cleanfile=open(cleanfilepth).readlines()
            linelist=list(difflib.unified_diff(bugfile,cleanfile))
            if len(linelist)>1:
                diffs.append(linelist)
                filepathlist.append(bugfilepth)
diffandpath=zip(filepathlist,diffs)
diffstring=''
for path,diff in diffandpath:
        diffstring+=(path+'\n')
        for line in diff:
            #print(line)
            diffstring+=line
            diffstring+='\n'
# print(diffstring)
diffile=open('diffile5.txt','w')
diffile.write(diffstring)
diffile.close()
