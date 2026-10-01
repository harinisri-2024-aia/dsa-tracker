#Attendance marker - 0 for absent and 1 for present for N students

#Different levels of difficulties:
#- Input Validation
#- Linear Time
#- Using data as String only
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