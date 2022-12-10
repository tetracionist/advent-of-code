import os, string
day = os.path.basename(__file__).split('.')[0]
read_file = f"{os.path.dirname(os.path.dirname(__file__))}\inputs\{day}.txt"

f = open(read_file, "r")
data = f.read()
f.close()

test_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

# a marker is four characters that are different
def findMarker(signal, marker_length):
   for i in range(len(signal)-(marker_length-1)):
    marker =  signal[i:i+marker_length]
    if len(set(marker)) == marker_length:
        return i+marker_length

print("Position of first marker:", findMarker(data, 14))