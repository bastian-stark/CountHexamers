filename = input('Enter file name: ')

infile = open(f"{filename}")
outfile = open(f"{filename}_counts.txt", "w")
sequencelist = []
for line in infile:
    line = line.strip('\n')
    if line.startswith('A') or line.startswith('T') or line.startswith('G') or line.startswith('C'):
        sequencelist.append(line)

sequencelist.sort()
sequencecounts = {}
for line in sequencelist:
    if line not in sequencecounts:
        sequencecounts[line] = 1
    elif line in sequencecounts:
        sequencecounts[line] += 1
    else:
        print('Error')

for key in sequencecounts:
    outfile.write(str(key) + '\t' + str(sequencecounts[key]) + '\n')