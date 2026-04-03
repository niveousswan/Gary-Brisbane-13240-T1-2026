# Week 2

[Return to contents](README.md)

---

### 1. Basic learning  
In this week, I learned some classical encryption methods, such as Caesar cipher, substitution cipher and Virginia cipher. I learned about the basic principles of classical cryptography and its importance in the development of cryptography.  
In my opinion, cryptography is a field that is constantly evolving and needs continuous innovation and improvement to face new problems.

---

### 2. Tutorial work

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
