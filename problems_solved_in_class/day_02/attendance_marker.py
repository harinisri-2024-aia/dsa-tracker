attendance = [1, 1, 0, 1, 0, 1, 1, 0]

absent = 0

for i in range(len(attendance)):
    if attendance[i] == 0:
        absent += 1

total = len(attendance)
present = total - absent

percentage = (present / total) * 100

print("Absent:", absent)
print("Out of:", total)
print("Attendance Percentage:", percentage)