import pandas as pd

def present_marked(id):

    # Load the attendance sheet
    df = pd.read_excel("attendance.xlsx",engine='openpyxl')

    # Mark the attendance for the given ID
    df.loc[df['ID'] == id, 'Attendance'] = 'Present'

    # Save the updated attendance sheet
    df.to_excel("attendance.xlsx", index=False)


def daa(name, roll):
    # Load the attendance sheet
    df = pd.read_excel("attendance.xlsx", engine='openpyxl')

    # Append a new row with the provided name and roll number
    new_row = {'Name': name, 'ID': roll}
    df = df.append(new_row, ignore_index=True)

    # Save the updated attendance sheet
    df.to_excel("attendance.xlsx", index=False)


