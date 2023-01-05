import csv

# with open('data.csv','r') as csv_file:
#     data_reader_o=csv.reader(csv_file)
# #
#     for line in data_reader:
#         print(line)

with open('data.csv', 'w') as w_csv_file:
    data_reader = csv.writer(w_csv_file, delimiter='-')

    for line in data_reader:
        data_reader.writerow(line)
    # print(rows)

# data =  [["Omkar", "Tavase", "Developer", "Arrk"],["Chetana", "Rera", "Developer", "Arrk"]]
# with open('data.csv', 'w') as w_csv_file:
#     #data_write=csv.writer(w_csv_file, delimeter='-')
#     for row in data:
#         for x in row:
#             w_csv_file.write(str(x)+',')
#         w_csv_file.write('n')

# for line in data_write:
#     print(line)
