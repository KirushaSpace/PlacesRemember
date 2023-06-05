from ninja import ModelSchema
from .models import Note


class NoteCreate(ModelSchema):
    class Config:
        model = Note
        model_fields = ['user', 'title', 'text', 'lat', 'lon']


class NoteRead(ModelSchema):
    class Config:
        model = Note
        model_fields = ['user', 'id', 'title', 'text', 'lat', 'lon', 'created']


