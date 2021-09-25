# Cipher Decrypter PT-BR

Script to decrypt Caesar's and Vinegere's cipher using a brazilian portuguese wordlist.

## How to use

### Caesar cipher
```bash
$ python app.py
Welcome to THE decrypter!                                                                                                                     [54/268]
Chose one of the available decrypter module to use.                                                                                                   
1 - Caesar                                                                                                                                            
2 - Vinegere                                                                                                                                          
1                                                                                                                                                     
Enter the file to decrypt(full path): /path/to/secret.txt                                                        
Shift -> Key                                                                                                                                          
0 -> TFDSFUP                                                                                                                                          
1 -> SECRETO                                                                                                                                          
2 -> RDBQDSN                                                                                                                                          
3 -> QCAPCRM                                                                                                                                          
4 -> PBZOBQL                                                                                                                                          
5 -> OAYNAPK                                                                                                                                          
6 -> NZXMZOJ                                                                                                                                          
7 -> MYWLYNI                                                                                                                                          
8 -> LXVKXMH                                                                                                                                          
9 -> KWUJWLG                                                                                                                                          
10 -> JVTIVKF                                                                                                                                         
11 -> IUSHUJE                                                                                                                                         
12 -> HTRGTID                                                                                                                                         
13 -> GSQFSHC                                                                                                                                         
14 -> FRPERGB                                                                                                                                         
15 -> EQODQFA                                                                                                                                         
16 -> DPNCPEZ                                                                                                                                         
17 -> COMBODY                                                                                                                                         
18 -> BNLANCX                                                                                                                                         
19 -> AMKZMBW                                                                                                                                         
20 -> ZLJYLAV                                                                                                                                         
21 -> YKIXKZU                                                                                                                                         
22 -> XJHWJYT                                                                                                                                         
23 -> WIGVIXS                                                                                                                                         
24 -> VHFUHWR                                                                                                                                         
25 -> UGETGVQ                                                                                                                                         
Found right shift to decrypt!                                                                                                                         
TFDSFUP is SECRETO using the shift 1.
```

### Vigenère cipher
```bash
Welcome to THE decrypter!
Chose one of the available decrypter module to use.
1 - Caesar
2 - Vinegere
2
The ciphertext to be decrypted: ciabiry
FOUND PLAINTEXT: KEYKEYK -> SECRETO
Brute force attempts can be found at ./src/vinegere.log
```

## License
[MIT](https://choosealicense.com/licenses/mit/)