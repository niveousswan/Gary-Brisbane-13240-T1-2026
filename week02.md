# Week 2

[Return to contents](README.md)

---

### 1. Basic learning  
In this week, I learned some classical encryption methods, such as Caesar cipher, substitution cipher and Virginia cipher. I learned about the basic principles of classical cryptography and its importance in the development of cryptography.  
In my opinion, cryptography is a field that is constantly evolving and needs continuous innovation and improvement to face new problems.

---

### 2. Tutorial work

2.1 Caesar Decrypt  
Using Caesar cipher with key 15, decrypt "pjhigpaxp".  
<img width="367" height="602" alt="图片" src="https://github.com/user-attachments/assets/184ae2c8-c928-42d1-8cc8-8e99da079a39" />

2.2 Rows/Columns Decrypt  
Using Rows/Columns with key 164325, decrypt "cieaexshxettrbxass".  
Decrypting the ciphertext "cieaexshxettrbxass" using the Rows/Columns transposition cipher with key 164325 gives the plaintext "caesaristhebestxxx". The final xxx are padding characters.

2.3 One Time Pad Brute Force  
Consider a One Time Pad that uses hexadecimal (base-16) digits, as opposed to English letters. A computer system can decrypt this One Time Pad at a rate of 1010 messages per second. In theory, what is the worst case time to apply a brute force attack on this One Time Pad when a message is 300 characters?  
A hexadecimal One Time Pad has 16 possible values for each character. For a message of 300 characters, the number of possible keys is 16^300.  
If a computer can test 10^10 messages per second, then the worst case brute force time is: 16^300 / 10^10 ≈ 1.72 × 10^351 seconds  
This is approximately: 5.46 × 10^343 years  
Therefore, in theory, brute forcing this One Time Pad is computationally infeasible.  
