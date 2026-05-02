from pyscript import document, display
import numpy as np

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

plt.figure(num=None)
plt.plot([0, 1], [0, 1])
plt.close()

days = []
absences = []

def displaying(e):
    day = document.getElementById('dayInput').value
    absence = int(document.getElementById('absenceInput').value)
    
    days.append(day)
    absences.append(absence)
    
    converted_absences = np.array(absences)

    plt.clf()

    plt.plot(days, converted_absences, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid()

    plt.show()