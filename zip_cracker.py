import zipfile

def crack_zip(zip_file, wordlist):
    try:
        with zipfile.ZipFile(zip_file) as zf:
            with open(wordlist, 'r', encoding='utf-8') as f:
                for word in f:
                    password = word.strip().encode('utf-8')
                    try:
                        zf.extractall(pwd=password)
                        print(f"[+] Password Found: {password.decode()}")
                        return
                    except:
                        print(f"[-] Tried: {password.decode()}")
                        continue
        print("[-] Password not found in wordlist.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    zip_path = input("Enter path to zip file: ")
    wordlist_path = input("Enter path to wordlist: ")
    crack_zip(zip_path, wordlist_path)
