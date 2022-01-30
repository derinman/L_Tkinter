for i in images:
#     if i.startswith('.'):
#         continue

#     if i not in no:
#         value = int(i[1:-4])
#         if value == 1 or value > 10:
#             value = value_map[value]
#         filename = filename_map[i[0:1]] + str(value) + ".png"
#         os.system(f"convert {i} -resize 80x111\> {filename}")