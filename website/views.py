from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from datetime import datetime
from . import db
from sqlalchemy import desc
from .models import Note
import json



views = Blueprint("views", __name__) 

@views.route("/", methods=['GET', 'POST', 'PUT'])
def home():
    
    notes = Note.query.all()
    
    if request.method == "POST":
        for note in notes:
            note_color = request.form.get("note_color_" + str(note.id))
            note_data = request.form.get("note_data_" + str(note.id))
            note_author = request.form.get("note_author_" + str(note.id))
            
            
            print(note_color, note_data, note_author)
            
            
            if note_author or note_color or note_data:
                note.color = note_color
                note.data = note_data
                note.user_name = note_author
                db.session.commit()
                print("Poznámka byla upravena")

            
        
    notes = Note.query.order_by(desc(Note.date)).all()
    
    return render_template("main.html", notes=notes)


@views.route("/add", methods=['GET', 'POST', 'PUT'])
def add():
    note = Note(date=datetime.now(), color="orange", user_name="", data="")

    db.session.add(note)
    db.session.commit()
    
    return redirect(url_for("views.home"))

@views.route("/delete", methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        note = json.loads(request.data)
        noteID = note['noteId']
        note = Note.query.get(int(noteID))
        

        db.session.delete(note)
        db.session.commit()
        print("Poznámka byla smazána")
            
    return jsonify({})
    