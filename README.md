# Dir Tree Artist

### Intro
![image](https://user-images.githubusercontent.com/59089164/148357706-40ed3cad-7564-44da-a520-39c8cbd77409.png)

Easily view folder structure, with parameters to sieve out what you want. Choose to exclude files from being viewed (.git, node_modules) and also specify maximum depth to prevent a huge output.

### Installation
```pip install dir-tree-artist```

### Usage
```python3 -m dir-tree-artist -f FOLDER_TO_TRAVERSE -d[optional] MAX_DEPTH -e[optional] EXCLUDED1,EXCLUDED2...```

### Example:
-> my_folder  
&nbsp;&nbsp;&nbsp;->[+] node_modules  
&nbsp;&nbsp;&nbsp;-> README.md  
&nbsp;&nbsp;&nbsp;->[+] public  
&nbsp;&nbsp;&nbsp;-> .gitignore  
&nbsp;&nbsp;&nbsp;-> package-lock.json  
&nbsp;&nbsp;&nbsp;-> package.json  
&nbsp;&nbsp;&nbsp;->[+] .git  
&nbsp;&nbsp;&nbsp;->[+] src   

View children of all folders within my_folder EXCLUDING .gitignore, .git, node_modules   
```python3 -m dir-tree-artist -f my_folder -d 2 -e .gitignore,.git,node_modules```
