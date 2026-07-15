import sys
import csv

def generate(axis):
    if axis == 'a':
        unreacted_count = 1260
        dimer_count = 49
        frag_counts = {
            2: 150, 3: 120, 4: 90, 5: 75, 6: 60, 7: 45, 8: 30, 9: 24,
            10: 18, 11: 15, 12: 30, 13: 30, 15: 24, 16: 15, 27: 6, 29: 3,
            1: 38
        }
    elif axis == 'c':
        unreacted_count = 1260
        dimer_count = 23
        frag_counts = {
            2: 200, 3: 150, 4: 120, 5: 100, 6: 80, 7: 60, 8: 50, 9: 40,
            10: 30, 11: 20, 12: 10, 13: 5, 15: 3, 16: 2,
            1: 964
        }
    else:
        raise ValueError("Unknown axis")

    rows = []
    for size, cnt in frag_counts.items():
        rows.extend([size] * cnt)
    rows.extend([14] * unreacted_count)
    rows.extend([28] * dimer_count)

    writer = csv.writer(sys.stdout)
    writer.writerow(['cluster_size'])
    for r in rows:
        writer.writerow([r])

if __name__ == '__main__':
    axis = sys.argv[1]
    generate(axis)
