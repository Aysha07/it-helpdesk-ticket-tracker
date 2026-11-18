import csv
import datetime

tickets = []
CSV_FILE = "it_support_tickets.csv"


def load_tickets():
    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tickets.append(row)
    except FileNotFoundError:
        pass


def save_tickets():
    with open(CSV_FILE, "w", newline="") as file:
        fieldnames = ["Ticket_ID", "Date", "Employee", "Department", "Issue", "Priority", "Status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tickets)


def create_ticket():
    print("\n--- CREATE NEW IT SUPPORT TICKET ---")
    emp_name = input("Employee Name: ").strip() or "Staff"
    dept = input("Department (e.g., HR, Sales, Accounts): ").strip() or "General"
    issue = input("Describe IT Issue (e.g., Wi-Fi issue, Printer jam): ").strip() or "System Issue"

    print("Priority: 1. High | 2. Medium | 3. Low")
    p_choice = input("Choose Priority (1/2/3): ").strip()
    priority = {"1": "High", "2": "Medium", "3": "Low"}.get(p_choice, "Medium")

    ticket_id = f"IT-{1001 + len(tickets)}"
    date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    ticket = {
        "Ticket_ID": ticket_id,
        "Date": date_now,
        "Employee": emp_name,
        "Department": dept,
        "Issue": issue,
        "Priority": priority,
        "Status": "Open"
    }
    tickets.append(ticket)
    save_tickets()
    print(f"\nTicket Created Successfully! Ticket ID: {ticket_id}")


def view_tickets():
    print("\n================ ALL IT SUPPORT TICKETS ================")
    if not tickets:
        print("No tickets found.")
        return

    for t in tickets:
        print(f"[{t['Ticket_ID']}] {t['Employee']} ({t['Department']}) | Issue: {t['Issue']} | Priority: {t['Priority']} | Status: {t['Status']}")
    print("========================================================\n")


def resolve_ticket():
    view_tickets()
    if not tickets:
        return

    tid = input("Enter Ticket ID to mark as Resolved (e.g., IT-1001): ").strip().upper()
    for t in tickets:
        if t["Ticket_ID"] == tid:
            t["Status"] = "Resolved"
            save_tickets()
            print(f"\nTicket {tid} has been marked as RESOLVED and updated in CSV!")
            return
    print("Ticket ID not found.")


def main():
    load_tickets()
    while True:
        print("\n--- DUBAI OFFICE IT HELPDESK SYSTEM ---")
        print("1. Create New Support Ticket")
        print("2. View All Tickets")
        print("3. Resolve / Close a Ticket")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            resolve_ticket()
        elif choice == "4":
            print("Exiting IT Helpdesk System. All records saved to 'it_support_tickets.csv'.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
