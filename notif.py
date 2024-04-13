from win10toast import ToastNotifier

# Créer un objet ToastNotifier
toaster = ToastNotifier()

# Afficher une notification
toaster.show_toast("Titre de la notification", "Contenu de la notification", duration=10)
