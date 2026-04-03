# Week 4

[Return to contents](README.md)

---

### 1. Basic Learning  

This week, I focused on understanding symmetric encryption algorithms, especially DES and AES. I found that DES is an older algorithm with a relatively short key, which makes it less secure today. However, it is still useful for learning the basic ideas behind encryption.  
I also learned that AES is widely used in modern systems because it provides stronger security and better performance. From this comparison, I realised that older algorithms like DES are important for understanding concepts, but in real-world applications, AES is usually the better choice.  
In my opinion, encryption methods need to keep improving as new security risks appear, so choosing the right algorithm is very important in practice.  

---

### 2. Tutorial Work  

2.1 Exclusive OR - Calculate (by hand) the exclusive OR of 010100 and 111001.  
<img width="969" height="723" alt="图片" src="https://github.com/user-attachments/assets/5876cab5-21b2-4796-b771-6d755287aa25" />  

2.2 SBC in CBC Mod - Encrypt P1 using SBC in CBC mode with K1 and IV1. What is the ciphertext, C1?  
A = 10101, B = 01011  
P1 = 10101 01011 10101  
K1 = 011, IV1 = 00110  
P1₁ = 10101, P1₂ = 01011, P1₃ = 10101  
C1₁ = E(10101 ⊕ 00110) = E(10011) = 11100  
C1₂ = E(01011 ⊕ 11100) = E(10111) = 00001  
C1₃ = E(10101 ⊕ 00001) = E(10100) = 11111  
C1 = 11100 00001 11111  

2.3 SBC in CTR Mod - Encrypt P1 using SBC in CTR mode with K1 and IV1. What is the ciphertext, C2?  
K1 = 011, IV1 = 00110  
C2₁ = 10101 ⊕ E(00110) = 10101 ⊕ 10011 = 00110  
C2₂ = 01011 ⊕ E(00111) = 01011 ⊕ 00010 = 01001  
C2₃ = 10101 ⊕ E(01000) = 10101 ⊕ 01010 = 11111  
C2 = 00110 01001 11111  

2.4 Compare Modes of Operation  
ECB encrypts each block independently, which makes it simple but not secure, because identical plaintext blocks will produce identical ciphertext blocks.  
CBC improves security by XORing each plaintext block with the previous ciphertext block. However, it must be processed sequentially, which makes it less efficient for parallel operations.  
CTR mode uses a counter to generate a keystream, which is XORed with the plaintext. It is faster and supports parallel processing, and errors in one block do not affect others.  
From this comparison, I found that CTR mode is generally more flexible and efficient, while CBC provides stronger chaining between blocks.  
