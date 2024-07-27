import argparse
import hashlib

def check_md5_hash(password, mode, hash_substr):
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    
    if mode == 'f' and md5_hash[:len(hash_substr)] == hash_substr:
        return True
    elif mode == 'l' and md5_hash[-len(hash_substr):] == hash_substr:
        return True
    
    return False

def main():
    parser = argparse.ArgumentParser(description="MD5 Hash Check Utility")
    parser.add_argument('-w', '--wordlist', required=True, help='Wordlist file containing passwords')
    parser.add_argument('-f', '--first', metavar='HASH', help='Check for MD5 hash with first characters')
    parser.add_argument('-l', '--last', metavar='HASH', help='Check for MD5 hash with last characters')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')

    args = parser.parse_args()

    if not (args.first or args.last):
        parser.error('At least one of -f or -l must be provided')

    try:
        with open(args.wordlist, 'rb') as file:
            file_content = file.read()

        passwords = file_content.decode('utf-8', errors='ignore').splitlines()

        for password in passwords:
            if args.first and check_md5_hash(password, 'f', args.first):
                print(f"[+] Password '{password}' matches MD5 hash with first {len(args.first)} characters '{args.first}'")
            elif args.last and check_md5_hash(password, 'l', args.last):
                print(f"[+] Password '{password}' matches MD5 hash with last {len(args.last)} characters '{args.last}'")
            elif args.verbose:
                print(f"[-] Password '{password}' does not match criteria")

    except FileNotFoundError:
        print(f"Error: File '{args.wordlist}' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()