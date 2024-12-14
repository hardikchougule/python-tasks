import requests

def fetch_api_data():
    print("Welcome to the API Fetcher")
    while True:
        print("\nMenu:")
        print("1. Fetch data from an API")
        print("2. Exit")

        try:
            choice = int(input("Enter your choice (1-2): "))
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
            continue

        if choice == 1:
            url = input("Enter API URL: ").strip()
            try:
                response = requests.get(url, timeout=5)  
                if response.status_code == 200:
                    try:
                        data = response.json() 
                        print("\nAPI Response:")
                        print(data)
                    except ValueError:
                        print("The response is not valid JSON.")
                else:
                    print(f"Error: Received status code {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
        elif choice == 2:
            print("Thank you for using the API Fetcher. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    fetch_api_data()
    
# links for testing
# https://jsonplaceholder.typicode.com/posts/1

# https://jsonplaceholder.typicode.com/posts

# https://jsonplaceholder.typicode.com/users/1