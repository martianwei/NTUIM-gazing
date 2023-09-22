from collections import defaultdict

for mode in ["train"]:
	source_file = f'./data/MPSGaze_{mode}/origin_label.txt'
	target_file = f'./data/MPSGaze_{mode}/label.txt'
	count = defaultdict(int)
	with open(source_file) as source, open(target_file, "w") as target: 
		lines = source.readlines()
		isFirst = True
		labels = []
		imgs_path = ''
		
		for line in lines:
			
			line = line.rstrip()
			if line.startswith('#'):
				continue
			else:
				label = line.split(" ")
				if len(label) != 25:
					print(label)
				try:
					label = [float(l) for l in label]
					if set([-1, -1, -1, -1]).intersection(set(label)) == set([-1, -1, -1, -1]):
						continue
					count[len(label)] += 1
				except: 
					# print("error")
					continue
	print(count)
		# 		if isFirst is True:
		# 			isFirst = False
		# 		else:
		# 			if len(labels) > 0:
		# 				labels_copy = labels.copy()
		# 				proc_label_file.write(imgs_path)
		# 				proc_label_file.write('\n')
		# 				for line in labels_copy:
		# 					# print(line)
		# 					proc_label_file.write(line)
		# 					proc_label_file.write('\n')
		# 				labels.clear()
		# 		imgs_path = line
		# 		# path = txt_path.replace('label.txt', 'images/') + path
		# 	else:
		# 		if line[0] != ' ':
		# 			line_split = line.split(' ')
		# 			label = [float(x) for x in line_split]
		# 			if len(label) == 25:
		# 				labels.append(line)
		# if len(labels) > 0:
		# 	labels_copy = labels.copy()
		# 	proc_label_file.write(imgs_path)
		# 	proc_label_file.write('\n')
		# 	for line in labels_copy:
		# 		proc_label_file.write(line)
		# 		proc_label_file.write('\n')
		# 	labels.clear()
