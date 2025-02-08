class Codec:
    def __init__(self):
        self.encodings = {}
        self.decodings = {}
        self.base = "http://tinyurl.com/"
        self._id = 0

    def encode(self, longUrl: str) -> str:
        encoded = f"{self.base}/{self._id}"
        self.encodings[longUrl] = encoded
        self.decodings[encoded] = longUrl
        self._id += 1
        return encoded

    def decode(self, shortUrl: str) -> str:
        return self.decodings[shortUrl]
