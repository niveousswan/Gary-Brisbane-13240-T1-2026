from mac import MAC

key = "0123456789012345678901234567890123456789012345678901234567890123"

print("Paste the Teams message details below.")
rx_message = input("Message: ")
rx_tag = input("Tag: ")

verified = MAC(key.encode()).verify(rx_message.encode(), rx_tag)

print("Verified?", verified)

if verified:
    print("Message authenticated successfully.")
else:
    print("Verification failed. Message or tag may have been changed.")
