# CCP Level I — Lesson 1 — Session 1 Submission

## M1 — Pseudocode

```text
SET SAMPLE_ID = "#12345"
SET ORGANISM_NAME = "H. Sapiens"
SET SEQ = ATGGCCCCGTAAATGTCGTATAGTGA
SEQ_COUNT = COUNT(SEQ)
SET GC_100 = (COUNT C + COUNT G) / SEQ_COUNT
PRINT SAMPLE_ID
PRINT ORGANISM_NAME
PRINT SEQ
PRINT SEQ_COUNT
PRINT GC_100
PRINT explanatory text and biological caution
END
```

## M2 — Python Skeleton

```python
sample_id = "#12345"
organism = "H. Sapiens"
seq = ["ATGGCCCCGTAAATGTCGTATAGTGA"]
seq_count = len(seq[0])
gc_100 = ((seq[0].count("G") + seq[0].count("C"))) / seq_count * 100
data_source = "www.genericdatabasesite.site"
print(sample_id)
print(organism)
print(seq)
print(seq_count)
print(gc_100)
print(data_source)
```

## M3 — Updated Script with GC Count

```python
sample_id = "#12345"
organism = "H. Sapiens"
seq = ["ATGGCCCCGTAAATGTCGTATAGTGA"]
seq_count = len(seq[0])
gc_100 = ((seq[0].count("G") + seq[0].count("C"))) / seq_count * 100
gc_count_estimate = seq_count * gc_100 / 100
data_source = "www.genericdatabasesite.site"
print(f"Sample ID: {sample_id}")
print(f"Organism: {organism}")
print(f"Sequence: {seq[0]}")
print(f"Sequence Length: {seq_count}")
print(f"GC%: {gc_100}%")
print(f"Estimated GC Count: {gc_count_estimate}")
print(f"Data source: {data_source}")
print(f"The data were obtained through public datasets: {data_source}")
```

## M4 — CLI + Git Attempt

```cmd
cd ~/mnt/disk_drive/script_parent_folder/script_folder/script.py
python script.py
git status
git add script.py
git commit -m "This is my first learning script. Please be kind with me"
```

## R2 — Error Interpretation

The `sampleID` is not an assigned value. That causes a `NameError`.

## S1 — Validation Pseudocode

Attempted validation around GC% values and missing values.

## S2 — Python Conditional Preview

```python
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
```

## S3 — Project Architecture

```text
Project_File/
├── scripts/
│   └── script1.py
├── results/
│   └── Results.csv
├── notes/
└── README.md
```

## Blank / Not Attempted

R1, R3, R4, A1, A2 were left blank in this session.
