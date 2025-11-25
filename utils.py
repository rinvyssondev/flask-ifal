import csv
import os

DATA_PATH = "data"

def get_next_id(filename, id_field="id"):
    registros = read_csv(filename)
    
    if not registros:
        return 1
    
    max_id = 0
    for registro in registros:
        try:
            current_id = int(registro.get(id_field, 0))
            if current_id > max_id:
                max_id = current_id
        except (ValueError, TypeError):
            continue
    
    return max_id + 1

def read_csv(filename):
    path = os.path.join(DATA_PATH, filename)

    if not os.path.exists(path):
        return []

    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(filename, data, fieldnames):
    path = os.path.join(DATA_PATH, filename)

    write_header = not os.path.exists(path)

    with open(path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if write_header:
            writer.writeheader()

        writer.writerow(data)

def validar_campos_obrigatorios(data, campos_obrigatorios):
    if not data:
        return False, "Dados não fornecidos"
    
    campos_faltando = []
    for campo in campos_obrigatorios:
        if campo not in data or data[campo] is None or str(data[campo]).strip() == "":
            campos_faltando.append(campo)
    
    if campos_faltando:
        return False, f"Campos obrigatórios faltando: {', '.join(campos_faltando)}"
    
    return True, ""
