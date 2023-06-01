import os


def filePathExists(file_path):
    """
    Funkcija koja vraca True ili False, ovisno o tome je li 'file_path' postoji ili ne
    """
    exists = os.path.exists(file_path)
    return exists


def openFilePathForReading(file_path):
    """
    Funkcija za otvaranje konekcije prema datoteci navedenoj u 'file_path' varijabli.
    Konekcija prema datoteci ce biti otvorena za citanje
    """
    if not filePathExists(file_path):
        return f"Datoteka {file_path} ne postoji"

    try:
        file_reader = open(file_path, "r")
        return file_reader
    except Exception as e:
        return f"Dogodila se greska prilikom pokusaja otvaranja {file_path} datoteke za citanje"


def openFilePathForWriting(file_path):
    """
    Funkcija za otvaranje konekcije prema datoteci navedenoj u 'file_path' varijabli.
    Konekcija prema datoteci ce biti otvorena za pisanje
    """
    try:
        file_writer = open(file_path, "w")
        return file_writer
    except Exception as e:
        return f"Dogodila se greska prilikom pokusaja otvaranja {file_path} datoteke za pisanje"


def writeToFilePathOpenClose(file_path, content):
    """
    Funkcija za pisanje u datoteku navedenu u 'file_path' varijabli
    Sadrzaj zapisa se nalazi u varijabli 'content'
    """
    try:
        with open(file_path, "w") as file_writer:
            file_writer.write(content)
    except Exception as e:
        return f"Dogodila se greska prilikom pokusaja pisanja u {file_path} datoteku"


def writeLineWithFileWriter(file_writer, line_content):
    """
    Funkcija za pisanje pomocu konekcije navedene u 'file_writer' varijabli
    Sadrzaj zapise se nalazi u varijabli 'line_content'
    """
    try:
        line_content += "\n"
        file_writer.write(line_content)
    except Exception as e:
        return f"Dogodila se greska prilikom pokusaja pisanja linije pomocu {file_writer} konekcije"


def readFromFilePathOpenClose(file_path):
    """
    Funkcija za citanje iz datoteke navedene u 'file_path' varijabli
    """
    if not filePathExists(file_path):
        return f"Datoteka {file_path} ne postoji"

    try:
        with open(file_path, "r") as file_reader:
            return file_reader.read()

    except Exception as e:
        return f"Dogodila se greska prilikom pokusaja cintanja iz {file_path} datoteke"


def readLineWithFileReader(file_reader):
    """
    Funkcija za citanje linije iz konekcije navedene u 'file_reader' varijabli
    """
    try:
        line = file_reader.readline()
        line = line.rstrip("\n")
        return line

    except Exception as e:
        return f"Dogodila se greska prilikom pokusaja citanja linije pomocu 'file_reader' konekcije"


def closeFileConnection(file_connection):
    """
    Funkcija za zatvaranje konekcije prema datoteci.
    """
    file_connection.close()
