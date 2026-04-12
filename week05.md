# Week 5

[Return to contents](README.md)

---

### 1. Basic Learning  

This week, I focused on understanding how encryption is applied in real systems, especially how different components work together to provide security.  
I started to see that cryptography is not just about individual algorithms, but also about how they are combined and used in practice. This includes things like key management, system design, and how different layers of security interact with each other.  
Overall, this week helped me move from learning individual concepts to understanding how they fit into a complete system.  

---

### 2. Tutorial Work  

1. RSA Key Generation  
p = 179, q = 181  
n = 179 * 181 = 32399  
φ(n) = 178 * 180 = 32040  
e = 7  
(7 * d) mod 32040 = 1  
d = 13733  
PU = {name = Haozhe, e = 7, n = 32399}  

2. RSA Encryption and Decryption  
M = 123  
C = 1237^7 mod 32399 = 18184  
Ciphertext {from = Haozhe, to = Rahman, C = 18184}  

---

### 3. Challenges and Problem Solving

One challenge I faced this week was understanding how different parts of a security system interact with each other. Compared to previous weeks, the content was less about calculations and more about system-level thinking.  
To address this, I tried to break the system down into smaller components and understand each part individually before looking at the overall design. This approach helped me make better sense of how everything fits together.  

---

### 4. Reflection  
Compared to previous weeks, this week felt more focused on understanding how things are used in practice rather than just learning individual concepts.  
I realised that even if an algorithm itself is secure, the way it is used can still create problems. This made me think more about how systems are designed, not just how they work.  

---

### 5. References  
Stallings, W. (2017). *Cryptography and network security: Principles and practice* (7th ed.). Pearson.  
National Institute of Standards and Technology (NIST). (2001). *Advanced Encryption Standard (AES)* (FIPS PUB 197). https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf  
