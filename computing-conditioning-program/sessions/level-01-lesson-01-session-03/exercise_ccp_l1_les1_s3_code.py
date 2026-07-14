import math

sample_id = "#12345"
organism = "H. Sapiens"
sequence = "ATGGCCCCGTAAATGTCGTATAGTGA"
sequence_length = len(sequence)
if sequence_length <= 0:
	print(f'Sequence has an invalid value')
else:
	gc_count = sequence.count("G") + sequence.count("C")
	gc_percent = gc_count / sequence_length * 100
if gc_percent <= 0 or gc_percent > 100 or math.isnan(gc_percent):
	print(f'GC% has an invalid value.')
elif gc_percent == None:
	print(f'GC% had no value.')
else:
	data_source = "www.genericdatabasesite.site"
	print(f"DNA Sample Report")
	print(f"-----------------")
	print(f"Sample ID: {sample_id}")
	print(f"Organism: {organism}")
	print(f"Sequence: {sequence}") 
	print(f"Sequence Length: {sequence_length}")
	print(f"GC%: {gc_percent}%")
	print(f"GC Count: {gc_count}") 
	print(f'The data were obtained through public datasets: {(data_source)}')

