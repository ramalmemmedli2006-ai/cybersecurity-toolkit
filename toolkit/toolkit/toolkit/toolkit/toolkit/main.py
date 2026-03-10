from toolkit.password_checker import run_password_checker
from toolkit.hash_cracker_demo import run_hash_cracker_demo
from toolkit.port_scanner import run_port_scanner
from toolkit.network_monitor import run_network_monitor


def print_menu() -> None:
    print("\n=== Cybersecurity Toolkit ===")
    print("1. Password Strength Checker")
    print("2. Hash Cracker Demo")
    print("3. Port Scanner")
    print("4. Network Monitor")
    print("5. Exit")


def main() -> None:
    while True:
        print_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            run_password_checker()
        elif choice == "2":
            run_hash_cracker_demo()
        elif choice == "3":
            run_port_scanner()
        elif choice == "4":
            run_network_monitor()
        elif choice == "5":
            print("Exiting Cybersecurity Toolkit.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
