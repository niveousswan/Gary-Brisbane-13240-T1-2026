# Week 07 Tutorial

## TLS 1.2 DH Packet Capture Analysis

1) TLS Message Sequence Diagram

Client → Server: Client Hello (Not Encrypted)
Server → Client: Server Hello (Not Encrypted)
Server → Client: Certificate (Not Encrypted)
Server → Client: Server Key Exchange (Not Encrypted)
Server → Client: Server Hello Done (Not Encrypted)
Client → Server: Client Key Exchange (Not Encrypted)
Client → Server: Change Cipher Spec (Not Encrypted)
Client → Server: Finished (Encrypted)
Server → Client: Change Cipher Spec (Not Encrypted)
Server → Client: Finished (Encrypted)

2) Encrypted vs Not Encrypted

Not Encrypted:
- Client Hello
- Server Hello
- Certificate
- Server Key Exchange
- Server Hello Done
- Client Key Exchange
- Change Cipher Spec

Encrypted:
- Finished
- Application Data

3) DH Key Size

2048 bits

Found in:
Server Key Exchange packet

4) Client Supported DH Key Sizes

- ffdhe2048
- ffdhe3072
- ffdhe4096
- ffdhe6144
- ffdhe8192

Found in:
Client Hello packet

5) RSA Key Size

2048 bits

Found in:
Certificate packet

6) Delay Calculation

RTT = 50 ms

TCP handshake = 1 RTT
TLS handshake = 2 RTT
HTTP request/response = 1 RTT

Total = 4 RTT = 200 ms# Week 07 Tutorial
TLS 1.2 DH packet capture analysis.

