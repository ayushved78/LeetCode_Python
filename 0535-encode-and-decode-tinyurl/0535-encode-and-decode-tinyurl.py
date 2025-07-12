import hashlib
class Codec:
    def __init__(self):
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_object = hashlib.sha256(longUrl.encode())
        full_hash = hash_object.hexdigest()
        
        length = 6
        code = full_hash[:length]

        while code  in self.code_to_url and self.code_to_url[code] != longUrl:
            lenght += 1
            code = full_hash[:length]
        
        self.code_to_url[code] = longUrl
        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))