import os

def clean():
    decfolder = "/home/student/mycode/final_project/decrypted"
    for x in os.listdir(decfolder):
        file_path = os.path.join(decfolder, x)
        os.remove(file_path)
    
    encfolder = "/home/student/mycode/final_project/encrypted"
    for y in os.listdir(encfolder):
        file_path = os.path.join(encfolder, y)
        os.remove(file_path)

    ptxfolder = "/home/student/mycode/final_project/plaintext_images"
    for z in os.listdir(ptxfolder):
        file_path = os.path.join(ptxfolder, z)
        os.remove(file_path)

    rootdir = "/home/student/mycode/final_project"
    for f in os.listdir(rootdir):
        file_path = os.path.join(rootdir, f)
        if os.path.isfile(file_path) and (f.endswith("png") or f.endswith("jpg")):
            os.remove(file_path)

def main():
    clean()

if __name__ == "__main__":
    main()