from goofy_base64.base64 import Base64ToolKit

if __name__ == "__main__":
    print(Base64ToolKit.encode("Hello World33")) # SGVsbG8gV29ybGQzMw==
    print(Base64ToolKit.encode("Hello")) # SGVsbG8=
    print(Base64ToolKit.encode("Hell")) # SGVsbA==
    print(Base64ToolKit.encode("Hel")) # SGVs
    print(Base64ToolKit.encode(3.1)) # My4x