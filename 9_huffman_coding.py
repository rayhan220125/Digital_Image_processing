from PIL import Image
from collections import Counter
import heapq

img = Image.open("input.jpg").convert("L")

# Get pixel values
pixels = list(img.getdata())

# Frequency of pixels
freq = Counter(pixels)

# Create Huffman tree
heap = [[f, [p, ""]] for p, f in freq.items()]
heapq.heapify(heap)

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    for x in a[1:]:
        x[1] = "0" + x[1]

    for x in b[1:]:
        x[1] = "1" + x[1]

    heapq.heappush(heap, [a[0] + b[0]] + a[1:] + b[1:])

# Huffman codes
codes = dict(heap[0][1:])

# Encode image
encoded = "".join(codes[p] for p in pixels)

print("Image Size:", img.size)
print("Original Bits:", len(pixels) * 8)
print("Compressed Bits:", len(encoded))
print("Compression Ratio:", round((len(pixels) * 8) / len(encoded), 2))

print("\nHuffman Codes:")
print(codes)