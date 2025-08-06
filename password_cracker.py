import hashlib

def crack_hash(hash_to_crack, algorithm, wordlist_file):
    try:
        with open(wordlist_file, 'r', encoding='utf-8') as f:
            for word in f:
                word = word.strip()
                hashed_word = hashlib.new(algorithm)
                hashed_word.update(word.encode('utf-8'))
                if hashed_word.hexdigest() == hash_to_crack:
                    print(f"[+] Password Found: {word}")
                    return
        print("[-] Password not found in wordlist.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    hash_input = input("Enter the hash to crack: ")
    algo = input("Hash algorithm (md5/sha1/sha256): ").lower()
    wordlist_path = input("Enter wordlist file path: ")
    crack_hash(hash_input, algo, wordlist_path)
