from pathlib import Path
file_path = Path(input("Enter .fasta file path: ").strip())
sequence = ""
sequence_count = 0
nucleotides = {"A", "T", "C", "G", "N"} 

with open(file_path, "r") as fasta_file:
    for line in fasta_file:
    	if line.startswith(">"):
	    	continue
line = line.strip().upper()
if not set(line) <= nucleotides:
   	print(f"Invalid values in {line}")
else:
   	sequence += line
   	sequence_count += 1
print(f"Number of lines: {sequence_count}")
print(f"Full sequence length: {len(sequence)} bases")
print(sequence)
