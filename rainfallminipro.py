# MINI PROJECT: Rainfall Analysis System

rainfall = [12, 24, 7, 56, 1, 10, 94]

def show_menu():
    print("\n--- RAINFALL ANALYSIS MINI PROJECT ---")
    print("1. Show all rainfall")
    print("2. Show Total Rainfall")
    print("3. Show Average Rainfall")
    print("4. Show Minimum and Maximum Rainfall")
    print("5. Show Sorted Rainfall (Ascending)")
    print("6. Add New Rainfall")
    print("7. Exit")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Rainfall data:", rainfall)

    elif choice == 2:
        total = sum(rainfall)
        print("Total Rainfall:", total)

    elif choice == 3:
        avg = sum(rainfall) / len(rainfall)
        print("Average Rainfall:", avg)

    elif choice == 4:
        print("Minimum Rainfall:", min(rainfall))
        print("Maximum Rainfall:", max(rainfall))

    elif choice == 5:
        # Basic sorting logic
        sorted_list = rainfall.copy()
        sorted_list.sort()
        print("Sorted Rainfall:", sorted_list)

    elif choice == 6:
        new_rain = int(input("Enter new rainfall: "))
        rainfall.append(new_rain)
        print("Added successfully!")

    elif choice == 7:
        print("Project Closed. Thank you!")
        break

    else:
        print("Wrong choice!")
