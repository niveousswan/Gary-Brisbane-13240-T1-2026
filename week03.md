# Week 3

[Return to contents](README.md)

---

### 1. Basic learning  

In this week, I learned the basic workings of symmetric and asymmetric encryption, and then I learned some types of attacks against encryption systems, such as brute force and man-in-the-middle attacks. These made me understand the importance of proper and rigorous management of keys and algorithms, which should ensure the confidentiality and integrity of data.  
In my opinion, have a hybrid encryption system is a more reasonable protection design. It needs to go through strict inspection and testing to ensure its security, only continuous optimization of the encryption system can maintain its balance and safe.  

---

### 2. Tutorial work  

2.1 Information Known by Attacker - What is the difference between KPA, CPA and CCA? Theoretical (and practical) attacks on ciphers are often classified by what is assumed to be known by the attacker for the attack to be successful. Consider these three classifications, and try to list what is known and not known but the attacker before the attack starts.
KPA: In a known plaintext attack, the attacker has access to some plaintexts and their corresponding ciphertexts. However, they do not know the key. The goal is to use this information to recover the key or decrypt other messages.  
CPA: In a chosen plaintext attack, the attacker can choose arbitrary plaintexts and obtain their corresponding ciphertexts. This gives the attacker more control compared to KPA, making it easier to analyze the encryption algorithm.  
CCA: In a chosen ciphertext attack, the attacker can choose ciphertexts and obtain their corresponding plaintexts. This is the strongest model, as it allows the attacker to test how the system decrypts data.  

2.2 Modes of Operation - Why are modes of operation needed?
Modes of operation are needed because block ciphers like AES can only encrypt fixed-size blocks (e.g., 128 bits). In real-world applications, data is usually longer than one block. Modes of operation allow block ciphers to securely encrypt large amounts of data.  
They also provide additional security features such as randomness (using IVs), error handling, and protection against patterns in the plaintext. Without modes of operation, encrypting multiple blocks directly would lead to security weaknesses, such as identical plaintext blocks producing identical ciphertext blocks.  

2.3 Attack on AES-128 - Assume you have discovered a vulnerability in AES-128 such that an attack is 1,000,000 times faster than a brute force attack. You have access to $10,000,000 of equipment. How long would it take to break AES-128 with your attack
Even at extremely high speeds, this would still take an astronomically long time, far longer than the age of the universe. Therefore, AES-128 remains secure even under this improved attack.
