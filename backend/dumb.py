import argparse


def dumb(symtoms, diagnoses):
    print(f"{symtoms}{diagnoses}")
    for x in range(100):
        print(x)
    

    return list(range(100))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search articles.")
    parser.add_argument("symtoms", help="Patient's symtoms.")
    parser.add_argument("diagnoses", help="Diagnosis guesses.")
    args = parser.parse_args()
    dumb(args.symtoms, args.diagnoses)