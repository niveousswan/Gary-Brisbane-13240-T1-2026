# Week 3

[Return to contents](README.md)

---

### 1. Basic Learning  

In this week, I learned the basic workings of symmetric and asymmetric encryption, and then I learned some types of attacks against encryption systems, such as brute force and man-in-the-middle attacks. These made me understand the importance of proper and rigorous management of keys and algorithms, which should ensure the confidentiality and integrity of data.  
In my opinion, hybrid encryption systems provide a more practical and secure design, as they combine the efficiency of symmetric encryption with the security of asymmetric encryption.

---

### 2. Tutorial Work  

2.1 Information Known by Attacker - What is the difference between KPA, CPA and CCA? Theoretical (and practical) attacks on ciphers are often classified by what is assumed to be known by the attacker for the attack to be successful. Consider these three classifications, and try to list what is known and not known but the attacker before the attack starts.  
KPA: In a known plaintext attack, the attacker has access to some plaintexts and their corresponding ciphertexts. However, they do not know the key. The goal is to use this information to recover the key or decrypt other messages.  
CPA: In a chosen plaintext attack, the attacker can choose arbitrary plaintexts and obtain their corresponding ciphertexts. This gives the attacker more control compared to KPA, making it easier to analyze the encryption algorithm.  
CCA: In a chosen ciphertext attack, the attacker can choose ciphertexts and obtain their corresponding plaintexts. This is the strongest model, as it allows the attacker to test how the system decrypts data.  

2.2 Modes of Operation - Why are modes of operation needed?  
Modes of operation are needed because block ciphers like AES can only encrypt fixed-size blocks (e.g., 128 bits). In real-world applications, data is usually longer than one block. Modes of operation allow block ciphers to securely encrypt large amounts of data.  
They also provide additional security features such as randomness (using IVs), error handling, and protection against patterns in the plaintext. Without modes of operation, encrypting multiple blocks directly would lead to security weaknesses, such as identical plaintext blocks producing identical ciphertext blocks.  

2.3 Brute Force of AES using Your Computer - Based on the OpenSSL speed tests, estimate how much it would cost you to perform a brute force attack on AES if you could buy as many computers the same as yours as you need. You will need to know or estimate the cost of your computer. As well as cost and time, what other practical limitations are there for such a brute force attack?  
To estimate the cost of a brute force attack on AES-128, I first used OpenSSL speed tests on my computer with the following command "openssl speed -evp aes-128-ecb". It measures how many AES encryption operations my computer can perform per second for different block sizes.  
<img width="803" height="305" alt="图片" src="https://github.com/user-attachments/assets/270459fe-5e5c-4341-ac97-539b08e92cd9" />  
Even if I could buy a very large number of identical computers, the total cost and time would still be so large that a brute force attack on AES-128 is not practical.  
In practice, brute force attacks on AES are also limited by:  
Hardware cost – building enough machines is extremely expensive  
Energy consumption – the electricity required would be enormous  
Physical limits – processing speed cannot increase indefinitely  
Time constraints – even with parallel systems, the time required is unrealistic  

---

### 3. Security Thinking  

Modern cryptography is designed to be secure against different types of attacks such as KPA, CPA, and CCA. Among these, CCA is considered the strongest attack model, so many modern encryption schemes aim to be secure against it.  
This shows that security is not only about strong algorithms, but also about how attackers interact with the system.  

---

### 4. References  

Stallings, W. (2017). *Cryptography and network security: Principles and practice* (7th ed.). Pearson.  
OpenSSL. (n.d.). OpenSSL command line tools documentation. https://www.openssl.org/docs/manmaster/man1/openssl-speed.html  
National Institute of Standards and Technology (NIST). (2001). *Advanced Encryption Standard (AES)* (FIPS PUB 197). https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf  
