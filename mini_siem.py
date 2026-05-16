import tkinter as tk


with open("security_logs.txt", "r") as file:

    logs = file.readlines()


failed_logins = {}

alerts = []


window = tk.Tk()

window.title("Mini SIEM Dashboard")

window.geometry("900x850")

window.configure(bg="#1e1e1e")


title_label = tk.Label(
    window,
    text="MINI SIEM DASHBOARD",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)

title_label.pack(pady=20)


logs_label = tk.Label(
    window,
    text="LIVE SECURITY LOGS",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="white"
)

logs_label.pack()


logs_text = tk.Text(
    window,
    height=20,
    width=100,
    bg="black",
    fg="#00ff00",
    insertbackground="white"
)

logs_text.pack(pady=10)


alerts_label = tk.Label(
    window,
    text="SECURITY ALERTS",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="red"
)

alerts_label.pack()


alerts_text = tk.Text(
    window,
    height=8,
    width=100,
    bg="black",
    fg="red",
    insertbackground="white"
)

alerts_text.pack(pady=10)


info_count = 0
warning_count = 0
error_count = 0


for log in logs:

    log = log.strip()

    logs_text.insert(tk.END, log + "\n")


    if "[INFO]" in log:

        info_count += 1

        print(f"INFO LOG: {log}")


    elif "[WARNING]" in log:

        warning_count += 1

        ip = log.split()[-1]


        if ip not in failed_logins:

            failed_logins[ip] = 1

        else:

            failed_logins[ip] += 1


        print(f"WARNING LOG: {log}")


    elif "[ERROR]" in log:

        error_count += 1

        print(f"ERROR LOG: {log}")


print("\nFAILED LOGIN SUMMARY")


for ip, count in failed_logins.items():

    print(f"{ip} -> {count} failed attempts")


    if count >= 3:

        alert = f"ALERT: Possible brute-force attack from {ip}"

        print(alert)

        alerts.append(alert)

        alerts_text.insert(tk.END, alert + "\n")


with open("alerts.txt", "w") as file:

    for alert in alerts:

        file.write(alert + "\n")


print("\nAlerts saved to alerts.txt")


stats_label = tk.Label(
    window,
    text="SECURITY STATISTICS",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)

stats_label.pack(pady=20)


stats_text = tk.Text(
    window,
    height=6,
    width=50,
    bg="black",
    fg="white",
    insertbackground="white"
)

stats_text.pack(pady=10)


stats_text.insert(
    tk.END,
    f"INFO Logs: {info_count}\ns"
)

stats_text.insert(
    tk.END,
    f"WARNING Logs: {warning_count}\n"
)

stats_text.insert(
    tk.END,
    f"ERROR Logs: {error_count}\n"
)

stats_text.insert(
    tk.END,
    f"Total Alerts: {len(alerts)}\n"
)


window.mainloop()