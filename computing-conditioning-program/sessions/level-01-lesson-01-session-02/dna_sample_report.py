"""CCP Level I — Lesson 1 — Session 2
Corrected DNA sample report script.

Focus:
- DNA sequence as a Python string
- validation before division
- direct GC count
- readable report output
"""

sample_id = "#12345"
organism = "Homo sapiens"
sequence = "ATGGCCCCGTAAATGTCGTATAGTGA"
data_source = "www.genericdatabasesite.site"

sequence_length = len(sequence)

if sequence_length <= 0:
    print("Sequence has an invalid value: length must be greater than 0.")
else:
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percent = gc_count / sequence_length * 100

    print("DNA Sample Report")
    print("-----------------")
    print(f"Sample ID: {sample_id}")
    print(f"Organism: {organism}")
    print(f"Sequence: {sequence}")
    print(f"Sequence Length: {sequence_length} bp")
    print(f"GC Count: {gc_count}")
    print(f"GC%: {gc_percent}%")
    print(f"The data were obtained through public datasets: {data_source}")
