import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--folder', required=True, help='Folder to traverse.')
parser.add_argument('-d', '--depth', required=False, help='Max number of layers to traverse.')
parser.add_argument('-e', '--exclude', required=False, help='''Folders to exclude from tree. 
                                                                To exclude multiple files separate with single comma.
                                                                e.g. ./dir1,./dir2,./file1''')
args = parser.parse_args()

arg_excluded = args.exclude
fpath = args.folder
allowedLayers = args.depth
tree = ''

if allowedLayers != None and not allowedLayers.isdigit():
    parser.error('Depth must be an integer')

def getExcludedFiles(excluded):
    exclude = []
    for file in excluded.split(','):
        fullpath = os.path.normpath(os.path.join(os.getcwd(), file))
        if os.path.isdir(fullpath) or os.path.isfile(fullpath):
            exclude.append(fullpath)

        else:
            parser.error('Excluded files are invalid.')
        
    return exclude

def traverse_1(fpath, layer, excluded):
    if allowedLayers != None:
        if layer >= int(allowedLayers):
            return
    
    global tree
    
    filefullpath = os.path.normpath(os.path.join(os.getcwd(), fpath))

    if os.path.isdir(fpath) and filefullpath not in excluded:
        for filename in os.listdir(fpath):
            child_path = os.path.normpath(os.path.join(filefullpath, filename))
            
            if child_path not in excluded:
                if os.path.isfile(child_path):
                    tree += '   '*layer + '|' +'\n' + '   '*layer + '-> ' + filename + '\n'
                else:
                    tree += '   '*layer + '|' +'\n' + '   '*layer + '->[+] ' + filename + '\n'
            
            traverse_1(child_path, layer+1, excluded)

def main():
    if os.path.isdir(fpath):
        excluded = getExcludedFiles(arg_excluded) if arg_excluded != None else []
        traverse_1(fpath, 0, excluded)
        print(tree)

    else:
        parser.error('Folder to traverse is invalid.')
  
if __name__ == '__main__':
    main()