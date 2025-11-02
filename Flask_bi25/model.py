from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv

db = SQLAlchemy()

class Attendance(db.Model):
    __tablename__ = 'attendance'  # Explicit table name

    id = db.Column(db.Integer, primary_key=True)
    imie = db.Column(db.String(128), nullable=False)
    nazwisko = db.Column(db.String(128), nullable=False)
    numer_albumu = db.Column(db.String(64), nullable=False)
    uwagi = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    os_id = db.Column(db.String(32))
    nr_albumu = db.Column(db.String(32))
    nr_karty_bibl = db.Column(db.String(32))
    nazwisko = db.Column(db.String(128))
    imie = db.Column(db.String(128))
    imie2 = db.Column(db.String(128))
    email = db.Column(db.String(128))
    termin1_ocena = db.Column(db.String(32))
    termin1_komentarz_pryw = db.Column(db.String(256))
    termin1_komentarz_pub = db.Column(db.String(256))
    termin1_data_uzyskania = db.Column(db.String(32))
    termin2_ocena = db.Column(db.String(32))
    termin2_komentarz_pryw = db.Column(db.String(256))
    termin2_komentarz_pub = db.Column(db.String(256))
    termin2_data_uzyskania = db.Column(db.String(32))    
      

def upload_students_csv(csv_path):
    """
    Reads studenci.csv and uploads its content to the students table.
    Skips header row; uses SQLAlchemy bulk_insert for efficiency.
    """
    with open(csv_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        students = []
        for row in reader:
            student = Student(
                os_id=row["os_id"],
                nr_albumu=row["nr_albumu"],
                nr_karty_bibl=row["nr_karty_bibl"],
                nazwisko=row["nazwisko"],
                imie=row["imie"],
                imie2=row["imie2"],
                email=row["email"],
                termin1_ocena=row["termin1_ocena"],
                termin1_komentarz_pryw=row["termin1_komentarz_pryw"],
                termin1_komentarz_pub=row["termin1_komentarz_pub"],
                termin1_data_uzyskania=row["termin1_data_uzyskania"],
                termin2_ocena=row["termin2_ocena"],
                termin2_komentarz_pryw=row["termin2_komentarz_pryw"],
                termin2_komentarz_pub=row["termin2_komentarz_pub"],
                termin2_data_uzyskania=row["termin2_data_uzyskania"]
            )
            students.append(student)
        db.session.bulk_save_objects(students)
        db.session.commit()    
    
    