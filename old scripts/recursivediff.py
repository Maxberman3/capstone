import difflib
import pathlib
import os

buggypath='C:/Users/Maxbe/Desktop/Capstone/dspace-6.2-sate6/dspace-6.2-buggy'
cleanpath='C:/Users/Maxbe/Desktop/Capstone/dspace-6.2-sate6/dspace-6.2-fixed'
buggyfilelist=[]
cleanfilelist=[]
for root, directories, filesnames in os.walk(buggypath):
    # for directory in directories:
    #     print(os.path.join(root,directory))
    for filename in filesnames:
        buggyfilelist.append(os.path.join(root,filename))
for root, directories, filenames in os.walk(cleanpath):
    # for name in d_names:
    #     cleantree.write(name+"\n")
    #     print(name)
    for filename in filenames:
        cleanfilelist.append(os.path.join(root,filename))
both=zip(buggyfilelist,cleanfilelist)
diffs=[]
filepathlist=[]
for bugfilepth,cleanfilepth in both:
    name,ext=os.path.splitext(bugfilepth)
    if ext in ['.py','.h','.c','.cpp','.xml','.html','.sh','.java','.class']:
        # print(bugfilepth)
        # if bugfilepth == 'C:/Users/Maxbe/Desktop/Capstone/sqlite-3.21-sate6/sqlite-3.21-buggy\ext\misc\spellfix.c':
        #     continue
        bugfile=open(bugfilepth).readlines()
        cleanfile=open(cleanfilepth).readlines()
        linelist=list(difflib.unified_diff(bugfile,cleanfile))
        if len(linelist)>1:
            diffs.append(linelist)
            filepathlist.append(bugfilepth)
        #diffs.append(difflib.unified_diff(bugfile,cleanfile))
        #filepathlist.append(bugfilepth)
diffandpath=zip(filepathlist,diffs)
diffstring=''
for path,diff in diffandpath:
        diffstring+=(path+'\n')
        for line in diff:
            #print(line)
            diffstring+=line
            diffstring+='\n'
# print(diffstring)
diffile=open('diffile4.txt','w')
diffile.write(diffstring)
diffile.close()
