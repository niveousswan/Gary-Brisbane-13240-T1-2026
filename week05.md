# Week 5

[Return to contents](README.md)

---

### 1. Basic Learning  

In this week, I studied the RSA encryption algorithm and its related mathematical principles. I learned the basic concepts of public key cryptography, including symmetric encryption and asymmetric encryption, the roles of public keys and private keys, and then understood the specific steps of the RSA algorithm, and comprehended the source of its security.  
In my opinion, these contents form a complete knowledge system ranging from cryptographic concepts to algorithm implementation and to the mathematical basis, enabling me to have a systematic understanding of modern encryption technology.  

---

### 2. Tutorial Work  

1. RSA Key Generation  
p = 179, q = 181  
n = 179 * 181 = 32399  
φ(n) = 178 * 180 = 32040  
e = 7  
(7 * d) mod 32040 = 1  
d = 13733  
PU = {name = Haozhe, e = 7， n  32399}  

2. RSA Encryption and Decryption  
M = 123  
C = 1237^7 mod 32399 = 18184  
Ciphertext {from = Haozhe, to = Rahman, C = 18184}  
