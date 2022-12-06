with open("day06.txt", 'r') as file:
    content = file.read()

def detect_marker(buffer, sequence_size):
    for i in range(len(buffer)):
        current = buffer[i:i+sequence_size]
        
        if len(set(current)) == sequence_size:
            return i + sequence_size
    return -1
            
#pt 1
result = detect_marker(content, 4)
print("first marker: ", result)

#pt 2
result2 = detect_marker(content, 14)
print("second marker: ", result2)
