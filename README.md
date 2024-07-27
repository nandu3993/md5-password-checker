# MD5 Hash Check Utility

This is a simple Python utility for checking passwords against specific MD5 hash patterns using a wordlist. The tool supports matching either the beginning or the end of an MD5 hash with a specified substring.

## Features

- **Wordlist-based password checking**: Test multiple passwords at once from a wordlist file.
- **MD5 hash substring matching**: Check if an MD5 hash of a password starts or ends with a specific substring.
- **Verbose mode**: Display passwords that do not match the criteria.
- **Error handling**: Gracefully handles file reading errors and other exceptions.

## Installation

To use this utility, you need to have Python installed on your system. The script doesn't require any external Python libraries beyond the standard library.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/md5-hash-check-utility.git
   cd md5-hash-check-utility


python md5_hash_check.py -w <wordlist.txt> [-f <start_hash>] [-l <end_hash>] [-v]
