import math

sample_id = "#12345"
organism = "H. Sapiens"
sequence = "ATGGCCCCGTAAATGTCGTATAGTGA" # formerly seq
sequence_length = len(sequence) # formely sequence_length
gc_percent = ((sequence.count("G") + sequence.count("C"))) / sequence_length * 100 # formerly gc_100
gc_count = sequence_length * gc_percent / 100
data_source = "www.genericdatabasesite.site"
if sequence_length <= 0:
	print(f'Sequence has an invalid value')
elif gc_percent <= 0 or gc_percent > 100 or math.isnan(gc_percent):
	print(f'GC% has an invalid value.')
elif gc_percent == None:
	print(f'GC% had no value.')
else:
	print(f"DNA Sample Report")
	print(f"-----------------")
	print(f"Sample ID: {sample_id}")
	print(f"Organism: {organism}")
	print(f"Sequence: {sequence[0]}") 
	print(f"Sequence Length: {sequence_length}")
	print(f"GC%: {gc_percent}%")
	print(f"Estimated GC Count: {gc_count}") 
	print(f'The data were obtained through public datasets: {(data_source)}')
