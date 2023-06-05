from datetime import date
from typing import List
from ninja import NinjaAPI, Schema, Router
from django.shortcuts import get_object_or_404
from .models import Note
from .schemas import NoteCreate, NoteRead
from django.contrib.auth.models import User


router = Router()


@router.post("/notes", tags=['Заметки'])
def create_note(request, payload: NoteCreate):
    user = User.objects.get(id=payload.user)
    data = payload.dict()
    data['user'] = user
    note = Note.objects.create(**data)
    return {"message": "create successful"}


@router.get("/notes/{note_id}", response=NoteRead, tags=['Заметки'])
def get_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    return note


@router.get("/notes", response=List[NoteRead], tags=['Заметки'])
def list_notes(request):
    notes = Note.objects.all()
    return notes


@router.delete("/notes/{note_id}", tags=['Заметки'])
def delete_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return {"message": "delete successful"}