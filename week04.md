# Week 4

[Return to contents](README.md)

---

### 1. Basic Learning  

In this week, I learned DES is a classical symmetric encryption algorithm. Although the security is low due to the short key, its encryption principle still has a great impact on others. I also learned AES is a commonly used symmetric encryption algorithm in modern times, because of its fast speed and high security, it is widely used in network communication and data protection.  
In my opinion, learning DES helps to understand encryption principles, but AES should be chosen for practical applications. At the same time, encryption technology must continue to strengthen to face the security challenges in the future.  

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
ECB means that each block is encrypted independently. It is simple but not secure because identical plaintext blocks produce identical ciphertext blocks.  
CBC means that each plaintext block is XORed with the previous ciphertext block before encryption. This improves security, but encryption is sequential and cannot be parallelised easily.  
CTR means that uses a counter and encrypts it to generate a keystream, which is XORed with plaintext. It is fast, allows parallel processing, and does not propagate errors between blocks.  
