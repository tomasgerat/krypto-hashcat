import base64

FILES=["shadow1.txt", "shadow2.txt", "shadow3.txt", "shadow4.txt"]
with open("HASHES.txt", "w") as fout:
    for file in FILES:
        with open(file, "r") as fin:
            for line in fin.readlines():
                line = line.strip()
                #grondzak:RC5r8Stb:l9nZ4EoL7EiLb1TkRWm91w==
                parts = line.split(":")

                coded_string = '''Q5YACgA...'''
                plain = base64.b64decode(parts[2]).hex()
                plainSalt = base64.b64decode(parts[1]).hex()
                plainSalt = parts[1]
                fout.write(f"{plain}:{plainSalt}\n")
