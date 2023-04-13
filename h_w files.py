# объединение файлов (вариант_1)

file_for_writing = []
sum_line = {}
with open('1.txt', 'rt', encoding='utf-8') as f_1:
    sum_line_1 = {}
    file_1_oneline = []
    counting_1 = 0
    for line in f_1.readlines():
        file_1_oneline.append(line)
        counting_1 += 1
    sum_line[counting_1] = file_1_oneline

with open('2.txt', 'rt', encoding='utf-8') as f_2:
    sum_line_2 = {}
    file_2_oneline = []
    counting_2 = 0
    for line in f_2.readlines():
        file_2_oneline.append(line)
        counting_2 += 1
    sum_line[counting_2] = file_2_oneline

with open('3.txt', 'rt', encoding='utf-8') as f_3:
    sum_line_3 = {}
    file_3_oneline = []
    counting_3 = 0
    for line in f_3.readlines():
        file_3_oneline.append(line)
        counting_3 += 1
    sum_line[counting_3] = file_3_oneline

sorted_keys = sorted(sum_line.keys())
sorted_sum_line = {}
for i in sorted_keys:
    sorted_sum_line[i] = sum_line[i]

for line in sorted_sum_line.values():
    file_for_writing += line
print(file_for_writing)

# если ВЫ не создавали в директории файл для записи
with open('file_finish.txt', 'x') as f:
    f.writelines(file_for_writing)
# если ВАМИ уже создан  итоговый файл, не обращайте внимание на ошибку
with open('file_finish.txt', 'w') as f:
    f.writelines(file_for_writing)