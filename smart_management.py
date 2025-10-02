import pandas as pd
import matplotlib.pyplot as plt
import os

# File to store data
file_name = "data.csv"

# Create file if not exists
if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["ID", "Name", "Department", "Score"])
    df.to_csv(file_name, index=False)
else:
    df = pd.read_csv(file_name)

# Functions
def save_data():
    df.to_csv(file_name, index=False)

def add_record():
    global df
    ID = input("Enter ID: ")
    Name = input("Enter Name: ")
    Department = input("Enter Department: ")
    Score = float(input("Enter Score (0-100): "))
    df = pd.concat([df, pd.DataFrame([[ID, Name, Department, Score]], columns=df.columns)], ignore_index=True)
    save_data()
    print("Record added!\n")

def view_records():
    print("\nAll Records:")
    print(df)

def update_record():
    global df
    ID = input("Enter ID to update: ")
    if ID in df["ID"].values:
        idx = df[df["ID"]==ID].index[0]
        df.at[idx, "Name"] = input("Enter new Name: ")
        df.at[idx, "Department"] = input("Enter new Department: ")
        df.at[idx, "Score"] = float(input("Enter new Score (0-100): "))
        save_data()
        print("Record updated!\n")
    else:
        print("ID not found!\n")

def delete_record():
    global df
    ID = input("Enter ID to delete: ")
    if ID in df["ID"].values:
        df = df[df["ID"] != ID]
        save_data()
        print("Record deleted!\n")
    else:
        print("ID not found!\n")

def search_record():
    key = input("Enter Name or ID to search: ")
    result = df[(df["ID"]==key) | (df["Name"].str.contains(key, case=False))]
    if not result.empty:
        print(result)
    else:
        print("No matching record found.\n")

def analyze_data():
    if df.empty:
        print("No data to analyze!\n")
        return
    print("\n--- Analytics ---")
    print("Average Score:", df["Score"].mean())
    print("Top Performer:")
    print(df.loc[df["Score"].idxmax()])
    print("Lowest Score:")
    print(df.loc[df["Score"].idxmin()])

    # Visualization
    df.groupby("Department")["Score"].mean().plot(kind='bar', color='skyblue', title="Average Score by Department")
    plt.ylabel("Average Score")
    plt.show()

# Menu Loop
while True:
    print("\n--- Smart Management System ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Search Record")
    print("6. Analyze Data")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice=="1":
        add_record()
    elif choice=="2":
        view_records()
    elif choice=="3":
        update_record()
    elif choice=="4":
        delete_record()
    elif choice=="5":
        search_record()
    elif choice=="6":
        analyze_data()
    elif choice=="7":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")