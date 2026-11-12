from datetime import datetime

REPORTS = [
    {
        "id": 1,
        "title": "Suspicious emails received by the office",
        "description": "Several emails ask staff to confirm a password on a fake portal.",
        "type": "Phishing",
        "client": "Les Calanques Association",
        "city": "Toulon",
        "date": "12/10/2026 09:30",
        "status": "New",
        "priority": None,
        "note": None,
    },
    {
        "id": 2,
        "title": "Encrypted files on the file server",
        "description": "Accounting documents no longer open and a ransom note appeared.",
        "type": "Ransomware",
        "client": "Atelier Mistral",
        "city": "Marseille",
        "date": "08/10/2026 18:05",
        "status": "In progress",
        "priority": "Critical",
        "note": "Server isolated from the network, backup restore in progress.",
    },
    {
        "id": 3,
        "title": "Unusual login to the mailbox",
        "description": "An account was used from a country where the organization has no activity.",
        "type": "Account compromise",
        "client": "Bastia Fictional High School",
        "city": "Bastia",
        "date": "29/09/2026 07:45",
        "status": "Closed",
        "priority": "Medium",
        "note": "Password reset and two-factor authentication enabled.",
    },
]

ISEN_LOCATION = {"lat": 43.1208325, "lng": 5.9389323}


def find_report(report_id):
    for report in REPORTS:
        if report["id"] == report_id:
            return report
    return None


def add_report(title, description):
    report = {
        "id": max((report["id"] for report in REPORTS), default=0) + 1,
        "title": title,
        "description": description,
        "type": None,
        "client": None,
        "city": None,
        "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "status": "New",
        "priority": None,
        "note": None,
    }
    REPORTS.append(report)
    return report
