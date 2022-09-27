import numpy as np

file = np.loadtxt("in.txt", delimiter=",", dtype=str)
marks = file[:, 1:4]
usn = file[:, 4]
marks_float = marks.astype(float)
avg_marks = marks_float.mean(axis=1)
max_avg = np.amax(avg_marks)
res = {usn[i]: avg_marks[i] for i in range(len(usn))}
with open("out.txt", "w") as output:
    for usn, avg in res.items():
        output.write(usn + "  " + str("{:.2f}".format(avg)))
        output.write("\n")
print("Max average= " + str("{:.2f}".format(max_avg)))
