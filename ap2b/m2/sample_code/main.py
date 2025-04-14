"""
Module untuk pembacaan json dan print ke terminal
"""
import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print("nama saya adalah", data["nama"])
print("NPM saya adalah", data["npm"])
print("Saya dari kelas", data["kelas"])
print("Jurusan saya adalah", data["jurusan"])
