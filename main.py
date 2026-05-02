from pyscript import document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
    
takenuser = {
    "Ancheta, Arthur Eugene Maximus Adarna": ("Sapphire", "Math"),
    "Asuncion, Miguelito Alonso Brigoli": ("Sapphire", "Homeroom"),
    "Battung, John Lorenzo Quisumbing": ("Sapphire", "Math"),
    "Buenvenida, Victor Emmanuel Bernardino": ("Sapphire", "PE"),
    "Casul, McKayla Analisse Gabor": ("Sapphire", "Lunch Time"),
    "Catapang, Athena La Verne Sarabia": ("Sapphire", "SS"),
    "Chua, Cade Rylie Rivera": ("Sapphire", "Science"),
    "Eusebio, Zyan Riley Tancinco": ("Sapphire", "English"),
    "Evangelio, Princess Radhika Zayn Divino": ("Sapphire", "Marching Band"),
    "Fado, Marianna Reinne Fabie": ("Sapphire", "Marching Band"),
    "Fermocil, Kleiser Ferida": ("Sapphire", "PE"),
    "Fernando, Curt Joshua Nicolas": ("Sapphire", "PE"),
    "Francia, Ethan Raphael Juanga": ("Sapphire", "Math"),
    "Jimenez, Sophia San Buenaventura": ("Sapphire", "Science"),
    "Mabilog, Javier Antonio Villadolid": ("Sapphire", "Math"),
    "Mactal, Al Chrian Abueme": ("Sapphire", "LeBron James"),
    "Magday, Constance Soleil Gustilo": ("Sapphire", "SS"),
    "Moya, Yanna Clarisse Obial": ("Sapphire", "PE"),
    "Mutia, Francheska Zoe Abesamis": ("Sapphire", "VE"),
    "Nazareno, Luis Gabriel IV Villarico": ("Sapphire", "ICT"),
    "Romero, Jose Inigo Abalajon": ("Sapphire", "SS"),
    "Santos, Kyler": ("Sapphire", "Math"),
    "Sarao, Jaedin Hailey Balberan": ("Sapphire", "SS"),
    "Sy, Briana Gabrielle Calaranan": ("Sapphire", "Math"),
    "Sy, Charlotte Anne Estrada": ("Sapphire", "PE"),
    "Udono, Jared Daniel Maulas": ("Sapphire", "English"),
    "Vida, Mary Kristine Claire Parra": ("Sapphire", "Math")
}


def ShowClassmates(event):
    classmates = ""
    for username, (section, fav_subject) in takenuser.items():
        classmates += f"{username}: \nSection: {section} \nFavorite Subject: {fav_subject}\n"
    document.getElementById("classmate-list").innerText = classmates

def AddClassmate(event):

    username = document.getElementById("username").value.strip()
    section = document.getElementById("section").value.strip()
    fav_subject = document.getElementById("subject").value.strip()

    if username and section and fav_subject:
        takenuser[username] = (section, fav_subject)
        document.getElementById("signed").innerText = f"{username} added as a classmate!"
        document.getElementById("username").value = ""
        document.getElementById("section").value = ""
        document.getElementById("subject").value = ""
    elif username in takenuser:
        document.getElementById("signed").innerText = "This classmate already exists."
    else:
         document.getElementById("signed").innerText = "Please fill in all fields."
