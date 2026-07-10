import math

sample_id = "#12345"
organism = "H. Sapiens"
seq = ["ATGGCCCCGTAAATGTCGTATAGTGA"]
seq_count = len(seq[0])
gc_100 = ((seq[0].count("G") + seq[0].count("C"))) / seq_count * 100
gc_count_estimate = seq_count * gc_100 / 100
data_source = "www.genericdatabasesite.site"

if gc_100 <= 0 or gc_100 > 100 or math.isnan(gc_100):
    print(f'GC% has an invalid value.')
elif gc_100 == None:
    print(f'GC% had no value.')
else:
    print(f"Sample ID: {sample_id}")
    print(f"Organism: {organism}")
    print(f"Sequence: {seq[0]}")
    print(f"Sequence Length: {seq_count}")
    print(f"GC%: {gc_100}%")
    print(f"Estimated GC Count: {gc_count_estimate}")
    print(f'The data were obtained through public datasets: {data_source}')
