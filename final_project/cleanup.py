import os

def clean():
    for x in os.listdir("/home/student/mycode/final_project/decrypted"):
        os.remove(x)
    for y in os.listdir("/home/student/mycode/final_project/encrypted"):
        os.remove(x)
    for z in os.listdir("/home/student/mycode/final_project/plaintext_images"):
        os.remove(z)

def main():
    clean()

if __name__ == "__main__":
    main()