import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--folder', required=True, help='Folder to traverse.')
parser.add_argument('-e', '--exclude', required=False, help='''Folders to exclude from tree. 
                                                                To exclude multiple files separate with single comma.
                                                                e.g. ./dir1,./dir2,./file1''')
args = parser.parse_args()

arg_excluded = args.exclude
fpath = args.folder
tree = ''

def getExcludedFiles(excluded):
    exclude = []
    for file in excluded.split(','):
        fullpath = os.path.normpath(os.path.join(os.getcwd(), file))
        if os.path.isdir(fullpath):
            exclude.append(fullpath)

        else:
            parser.error('Excluded files are invalid.')
        
    return exclude

def traverse_1(fpath, layer, excluded):
    global tree
    filefullpath = os.path.normpath(os.path.join(os.getcwd(), fpath))

    if os.path.isdir(fpath) and filefullpath not in excluded:
        for filename in os.listdir(fpath):
            child_path = os.path.normpath(os.path.join(filefullpath, filename))
            
            if child_path not in excluded:
                tree += '   '*layer + '|' +'\n' + '   '*layer + '-> ' + filename + '\n'
            
            traverse_1(child_path, layer+1, excluded)
    
if os.path.isdir(fpath):
    excluded = getExcludedFiles(arg_excluded) if arg_excluded != None else []
    traverse_1(fpath, 0, excluded)
    print(tree)

else:
    parser.error('Folder to traverse is invalid.')