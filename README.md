# IT Helpdesk Ticket & Asset Tracker

A Python command-line IT support ticketing tool built for office IT departments. It allows IT engineers to log employee technical issues, assign priority levels, update ticket statuses to Resolved, and automatically export all records to an Excel-compatible CSV database.

#Key Features
*Ticket Logging & Auto-ID:** Automatically generates unique ticket IDs (e.g., IT-1001) with timestamps, department names, and priority tags (High, Medium, Low).
*Status Management:** Allows IT support staff to track open issues and mark them as Resolved.
*Persistent CSV Database:** Automatically saves and updates all ticket records in `it_support_tickets.csv` for daily reporting in Microsoft Excel.

#Technologies Used
 Python 3 (Dictionaries, Lists, Functions, `csv` module, `datetime` module)

#Sample Output
```text
--- DUBAI OFFICE IT HELPDESK SYSTEM ---
1. Create New Support Ticket
2. View All Tickets
3. Resolve / Close a Ticket
4. Exit
Select an option (1-4): 1

--- CREATE NEW IT SUPPORT TICKET ---
Employee Name: aysha
Department (e.g., HR, Sales, Accounts): sales
Describe IT Issue (e.g., Wi-Fi issue, Printer jam): outlook not sync
Priority: 1. High | 2. Medium | 3. Low
Choose Priority (1/2/3): 1

Ticket Created Successfully! Ticket ID: IT-1001

--- DUBAI OFFICE IT HELPDESK SYSTEM ---
1. Create New Support Ticket
2. View All Tickets
3. Resolve / Close a Ticket
4. Exit
Select an option (1-4): 1

--- CREATE NEW IT SUPPORT TICKET ---
Employee Name: alisha
Department (e.g., HR, Sales, Accounts): hr
Describe IT Issue (e.g., Wi-Fi issue, Printer jam): printer jam
Priority: 1. High | 2. Medium | 3. Low
Choose Priority (1/2/3): 2

Ticket Created Successfully! Ticket ID: IT-1002

--- DUBAI OFFICE IT HELPDESK SYSTEM ---
1. Create New Support Ticket
2. View All Tickets
3. Resolve / Close a Ticket
4. Exit
Select an option (1-4): 2

================ ALL IT SUPPORT TICKETS ================
[IT-1001] aysha (sales) | Issue: outlook not sync | Priority: High | Status: Open
[IT-1002] alisha (hr) | Issue: printer jam | Priority: Medium | Status: Open
========================================================


--- DUBAI OFFICE IT HELPDESK SYSTEM ---
1. Create New Support Ticket
2. View All Tickets
3. Resolve / Close a Ticket
4. Exit
Select an option (1-4): 3

================ ALL IT SUPPORT TICKETS ================
[IT-1001] aysha (sales) | Issue: outlook not sync | Priority: High | Status: Open
[IT-1002] alisha (hr) | Issue: printer jam | Priority: Medium | Status: Open
========================================================

Enter Ticket ID to mark as Resolved (e.g., IT-1001): it-1001

Ticket IT-1001 has been marked as RESOLVED and updated in CSV!

--- DUBAI OFFICE IT HELPDESK SYSTEM ---
1. Create New Support Ticket
2. View All Tickets
3. Resolve / Close a Ticket
4. Exit
Select an option (1-4): 4
Exiting IT Helpdesk System. All records saved to 'it_support_tickets.csv'.
PS C:\Users\mjays\OneDrive\Desktop\it-helpdesk-ticket-tracker> ss
```

#How to Run
1. Download `helpdesk_tracker.py`.
2. Open your terminal or Command Prompt in the project folder and run:
   ```bash
   python helpdesk_tracker.py
   ```