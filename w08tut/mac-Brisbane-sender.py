from mac import MAC

key = "0123456789012345678901234567890123456789012345678901234567890123"
message = "message to hash"

tag = MAC(key.encode()).generate(message.encode())

print("Copy this Teams message:")
print(f"AuthenticatedMessage{{from=Gary,to=Linda,message={message},tag={tag}}}")
