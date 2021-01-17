import argparse
from web_script import search


def dumb(symtoms, diagnoses):
    print(f"{symtoms}{diagnoses}")
    

    return [[1, "shelden.tech", 5], [2, "google.com", 10]]


#print(search(["anemia", "weakness"], ["Celiac Disease", "Lupus", "ALS"]))
print("anemia, weakness".split(','))