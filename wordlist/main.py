from unidecode import unidecode

def generate(base :str, fout):
    fout.write(base + "\n")
    for i in range(len(base)):
        if i == 0:
            s = base[0].upper()
        else:
            s = base[0:i]
            s += base[i].upper()
        s += base[i+1:]
        fout.write(s + "\n")


def process_names():
    with open("../names_processed.lst", "w") as fout:
        with open("names.lst", "r", encoding='utf-8') as fin:
            for line in fin.readlines():
                line = line.strip()
                if len(line) == 1:
                    continue
                base = line.split(" ")[0].lower()
                generate(base, fout)
                uni = unidecode(base)
                if uni != base:
                    generate(uni, fout)


if __name__ == '__main__':
    process_names()
