import tkinter as tk
import time

def update_time():
    # Παίρνουμε την ώρα σε μορφή Ώρα:Λεπτά:Δευτερόλεπτα
    current_time = time.strftime('%H:%M:%S')
    
    # Αλλάζουμε το κείμενο της ετικέτας με τη νέα ώρα
    clock_label.config(text=current_time)
    
    #Λέμε στο πρόγραμμα να ξανατρέξει αυτή τη συνάρτηση σε 1000 χιλιοστά του δευτερολέπτου
    clock_label.after(1000, update_time)

# Βασικό παράθυρο
root = tk.Tk()
root.title("Ψηφιακό Ρολόι")
root.geometry("350x150")
root.configure(bg="black")
root.resizable(False, False)

# Δημιουργία της ετικέτας που θα δείχνει την ώρα
clock_label = tk.Label(root, font=('Arial', 60, 'bold'), bg='black', fg='#00FF00')

# Τοποθετούμε τους αριθμούς στο κέντρο του παραθύρου
clock_label.pack(expand=True)

# Καλούμε τη συνάρτηση για πρώτη φορά για να ξεκινήσει το ρολόι
update_time()

root.mainloop()