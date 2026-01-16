import tkinter as tk
import csv
import datetime
import os

filename = 'event_log.csv'
headers = ['Timestamp', 'Event type']

file_exists = os.path.exists(filename)

def save_data():
    event = entry1.get()

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    data_row = [timestamp, event]

    with open("event_log.csv", mode="a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        if not file_exists:
            csv_writer.writerow(headers)

        csv_writer.writerow(data_row)

window = tk.Tk()
window.geometry("200x100")

entry1_label = tk.Label(text="Event type:")
entry1 = tk.Entry(bg="white", fg="black")
btn = tk.Button(
    text="Add event",
    command=save_data
)
entry1_label.pack()
entry1.pack()
btn.pack()
window.mainloop()