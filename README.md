# assemblyScript
__NOTE: THIS IS A TRANSPILER NOT A COMPIELR__  
This is meant to be a simple language based off NASM assembly   
I will write this language in python to make things easier for myself  
This language is meant to be higher level than assembly and lower than c/c++ so that it transpiles directly into NASM assembly  
usage `python3 src/main.py -f <input file> -o <output file>` which will transpile into nasm assembly  
  
TODO:  
- [x] ~Add comments~
- [ ] Add multiline comments
- [ ] Add `move(<source>, <destination>)` command  
- [ ] Add `sysinfo(<number of bits>, <cpu type>)`
- [ ] Add `bits(<number of bits>)` and `cpu(<cpu type>)` commands
- [ ] Fix workflow file so that it actually generates binaries and doesn't error out
- [ ] Add to this TODO list
