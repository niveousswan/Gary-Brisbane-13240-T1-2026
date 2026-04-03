# Week 2

[Return to contents](README.md)

---

### 1. Basic Learning  
This week, I explored some classical encryption methods such as the Caesar cipher, substitution cipher, and Vigenère cipher. These examples helped me understand how early encryption systems were designed and used.  
From this, I started to see that cryptography is always changing. As technology develops, new problems appear, so encryption methods also need to be updated and improved.  

---

### 2. Tutorial Work  

2.1 Caesar Decrypt - Using Caesar cipher with key 15, decrypt "pjhigpaxp".  
<img width="367" height="602" alt="图片" src="https://github.com/user-attachments/assets/184ae2c8-c928-42d1-8cc8-8e99da079a39" />  
The image above shows my manual decryption process using the shifted alphabet. I shifted each letter backward by 15 positions to obtain the plaintext.

2.2 Rows/Columns Decrypt - Using Rows/Columns with key 164325, decrypt "cieaexshxettrbxass".  
I decrypted the ciphertext "cieaexshxettrbxass" using the key 164325. The result is "caesaristhebestxxx".The final "xxx" are padding characters added to complete the encryption grid.  
This method rearranges the positions of characters rather than changing the characters themselves, which makes it different from substitution ciphers.  

2.3 One Time Pad Brute Force - Consider a One Time Pad that uses hexadecimal (base-16) digits, as opposed to English letters. A computer system can decrypt this One Time Pad at a rate of 1010 messages per second. In theory, what is the worst case time to apply a brute force attack on this One Time Pad when a message is 300 characters?  
For a One-Time Pad using hexadecimal digits (base 16), each character has 16 possible values.  
For a message of 300 characters: Number of possible keys = 16³⁰⁰  
If a computer can test 10¹⁰ keys per second: Worst-case time = 16³⁰⁰ / 10¹⁰ ≈ 1.72 × 10³⁵¹ seconds  
This shows that brute force attacks on a properly implemented One-Time Pad are computationally infeasible.  

---

### 3. Challenges and Problem Solving

Ciphers such as Caesar and substitution are easy to learn, but they are not strong in terms of security. They can usually be cracked by looking at patterns in the letters, such as frequency.  
On the other hand, the One-Time Pad is theoretically impossible to break if it is used correctly, since it relies on a completely random key of the same length as the message. The main problem is that it is not practical, because distributing and storing the key securely is very challenging.  

---

### 4. Reflection

This week helped me understand the strengths and weaknesses of different encryption methods. While classical ciphers are useful for learning, they are not secure in real-world applications.
I also realised that strong security often comes with practical challenges, such as key management in the One-Time Pad.  

---

### 5. References

Stallings, W. (2017). Cryptography and network security: Principles and practice (7th ed.). Pearson.  
GeeksforGeeks. (n.d.). Cryptography introduction. https://www.geeksforgeeks.org/cryptography-introduction/  
