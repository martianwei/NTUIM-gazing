txt_path = './data/MPSGaze_train/origin_label.txt'
proc_path = './data/MPSGaze_train/label.txt'
origin_label_file = open(txt_path, 'r')
proc_label_file = open(proc_path, 'w')
lines = origin_label_file.readlines()
isFirst = True
labels = []
imgs_path = ''
for line in lines:
    line = line.rstrip()
    if line.startswith('#'):
        if isFirst is True:
            isFirst = False
        else:
            if len(labels) > 0:
                labels_copy = labels.copy()
                proc_label_file.write(imgs_path)
                proc_label_file.write('\n')
                for line in labels_copy:
                    # print(line)
                    proc_label_file.write(line)
                    proc_label_file.write('\n')
                labels.clear()
        imgs_path = line
        # path = txt_path.replace('label.txt', 'images/') + path
    else:
        if line[0] != ' ':
            line_split = line.split(' ')
            label = [float(x) for x in line_split]
            if len(label) == 25:
                labels.append(line)
if len(labels) > 0:
    labels_copy = labels.copy()
    proc_label_file.write(imgs_path)
    proc_label_file.write('\n')
    for line in labels_copy:
        proc_label_file.write(line)
        proc_label_file.write('\n')
    labels.clear()