# RSA Decryptor 

## How it works ? :
- First, you need to factorize `n` and get the two primes `p` and `q` 
- now, you know `p, q, n, e` all you need is to calculate `d`
- then use this `d` to decrypt cypher 
- `PlainText = cypher^d mod n`   
- [Python Solution](RSA.py)
