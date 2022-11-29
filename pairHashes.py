import base64

def read_file(filename: str):
    with open(filename, "r") as fin:
        return fin.readlines()
    raise Exception(f"Failed to read file {filename}")


hashes_b64 = []
for f in ["shadow1.txt", "shadow2.txt", "shadow3.txt", "shadow4.txt"]:
    hashes_b64.extend(read_file(f))

hashes_map = {}
for h in hashes_b64:
    s = h.split(":")
    hashes_map[s[2].strip()] = s[0:2]
with open("result.txt", "r") as fin:
    hashes = fin.readlines()
with open("final.txt", "w") as fout:
    for h in hashes:
        if h[0] != "#" and h[0] != "\n":
            s = h.split(":")
            hash = s[0]
            salt = s[1]
            passw = s[2]
            hash_b64 = base64.b64encode(bytes.fromhex(hash)).decode("ascii")
            h_info = hashes_map[hash_b64]
            fout.write(f"{hash_b64}:{hash}:{salt}:{h_info[0]}:{passw}")
        else:
            fout.write(h)
