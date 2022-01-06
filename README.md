# Dir Tree Artist

### Ever wanted to see your folders structure quickly?
![image](https://user-images.githubusercontent.com/59089164/148357706-40ed3cad-7564-44da-a520-39c8cbd77409.png)

Easily view folder structure, with parameters to sieve out what you want. Choose to exclude files from being viewed (.git, node_modules) and also specify maximum depth to prevent a huge output.

### Installation
```pip install dir-tree-artist```

### Usage
```python3 -m dir-tree-artist -f <folder to traverse> -d[optional] <maximum depth> -e[optional] <folders to exclude separated by comma>```

#### Example:
-> my_folder  
  ->[+] node_modules  
  -> README.md  
  ->[+] public  
  -> .gitignore  
  -> package-lock.json  
  -> package.json  
  ->[+] .git  
  ->[+] src   

View children of all folders within my_folder EXCLUDING .gitignore, .git, node_modules
```python3 -m dir-tree-artist -f my_folder -d 2 -e .gitignore,.git,node_modules```
