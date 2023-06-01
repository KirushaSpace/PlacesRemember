from datetime import date
from typing import List
from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import Note
from .schemas import NoteCreate, NoteRead


api = NinjaAPI()


@api.post("/notes", tags=['Заметки'])
def create_note(request, payload: NoteCreate):
    data = payload.dict()
    note = Note.objects.create(**data)
    return {"id": note.id}


@api.get("/notes/{note_id}", response=NoteRead, tags=['Заметки'])
def get_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    return note


@api.get("/notes", response=List[NoteRead], tags=['Заметки'])
def list_notes(request):
    notes = Note.objects.all()
    return notes


@api.delete("/notes/{note_id}", tags=['Заметки'])
def delete_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return {"success": True}