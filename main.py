import os

while True:

    print("\n========== AI Financial Analysis Platform ==========")
    print("1. Data Collection")
    print("2. Data Preprocessing")
    print("3. Database Setup")
    print("4. Train ML Models")
    print("5. Run API")
    print("6. Run Dashboard")
    print("7. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        os.system("python data_collection/stock_downloader.py")

    elif choice == "2":
        os.system("python preprocessing/spark_preprocessor.py")

    elif choice == "3":
        os.system("python sql_interface/database_manager.py")

    elif choice == "4":
        os.system("python forecasting/train_gbt_forecaster.py")

    elif choice == "5":
        os.system("python -m uvicorn api.app:app --reload")

    elif choice == "6":
        os.system("python -m streamlit run dashboard/app.py")

    elif choice == "7":
        break

    else:
        print("Invalid choice")