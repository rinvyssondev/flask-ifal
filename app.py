from flask import Flask, request, jsonify
from swagger_config import swagger_config, swagger_template
from utils import read_csv, write_csv, get_next_id
from utils import validar_campos_obrigatorios
from flasgger import Swagger, swag_from
import os

app = Flask(__name__)

swagger = Swagger(app, config=swagger_config, template=swagger_template)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "docs")

@swag_from(os.path.join(DOCS_DIR, "alunos/listar_alunos.yml"))
@app.route("/alunos", methods=["GET"])
def listar_alunos():
    try:
        alunos = read_csv("alunos.csv")
        return jsonify(alunos)
    except FileNotFoundError:
        return jsonify({"error": "Arquivo de alunos não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "alunos/criar_aluno.yml"))
@app.route("/alunos", methods=["POST"])
def criar_aluno():    
    try:
        data = request.get_json()
        
        campos_obrigatorios = ["nome", "email", "data_nascimento"]
        valido, erro = validar_campos_obrigatorios(data, campos_obrigatorios)
        
        if not valido:
            return jsonify({"error": erro}), 400
        
        next_id = get_next_id("alunos.csv")
        
        aluno = {
            "id": str(next_id),
            "nome": data["nome"],
            "email": data["email"],
            "data_nascimento": data["data_nascimento"],
        }

        write_csv(
            "alunos.csv",
            aluno,
            ["id", "nome", "email", "data_nascimento"]
        )
        return jsonify({"message": "Aluno cadastrado com sucesso!", "data": aluno}), 201
        
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "professores/listar_professores.yml"))
@app.route("/professores", methods=["GET"])
def listar_professores():    
    try:
        return jsonify(read_csv("professores.csv"))
    except FileNotFoundError:
        return jsonify({"error": "Arquivo de professores não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "professores/criar_professor.yml"))
@app.route("/professores", methods=["POST"])
def criar_professor():   
    try:
        data = request.get_json()
        
        campos_obrigatorios = ["nome", "email"]
        valido, erro = validar_campos_obrigatorios(data, campos_obrigatorios)
        
        if not valido:
            return jsonify({"error": erro}), 400
        
        next_id = get_next_id("professores.csv")
        
        professor = {
            "id": str(next_id),
            "nome": data["nome"],
            "email": data["email"],
        }

        write_csv(
            "professores.csv",
            professor,
            ["id", "nome", "email"]
        )
        return jsonify({"message": "Professor cadastrado!", "data": professor}), 201
        
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "cursos/listar_cursos.yml"))
@app.route("/cursos", methods=["GET"])
def listar_cursos():    
    try:
        return jsonify(read_csv("cursos.csv"))
    except FileNotFoundError:
        return jsonify({"error": "Arquivo de cursos não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "cursos/criar_curso.yml"))
@app.route("/cursos", methods=["POST"])
def criar_curso():    
    try:
        data = request.get_json()
        
        campos_obrigatorios = ["nome", "descricao", "carga_horaria", "professor_id"]
        valido, erro = validar_campos_obrigatorios(data, campos_obrigatorios)
        
        if not valido:
            return jsonify({"error": erro}), 400
        
        next_id = get_next_id("cursos.csv", "curso_id")
        
        curso = {
            "curso_id": str(next_id),
            "nome": data["nome"],
            "descricao": data["descricao"],
            "carga_horaria": data["carga_horaria"],
            "professor_id": data["professor_id"],
        }

        write_csv(
            "cursos.csv",
            curso,
            ["curso_id", "nome", "descricao", "carga_horaria", "professor_id"]
        )

        return jsonify({"message": "Curso criado!", "data": curso}), 201
        
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "matriculas/listar_matriculas.yml"))
@app.route("/matriculas", methods=["GET"])
def listar_matriculas():    
    try:
        return jsonify(read_csv("matriculas.csv"))
    except FileNotFoundError:
        return jsonify({"error": "Arquivo de matrículas não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "matriculas/criar_matricula.yml"))
@app.route("/matriculas", methods=["POST"])
def criar_matricula():    
    try:
        data = request.get_json()
        
        campos_obrigatorios = ["aluno_id", "curso_id", "status"]
        valido, erro = validar_campos_obrigatorios(data, campos_obrigatorios)
        
        if not valido:
            return jsonify({"error": erro}), 400
        
        next_id = get_next_id("matriculas.csv")
        
        matricula = {
            "id": str(next_id),
            "aluno_id": data["aluno_id"],
            "curso_id": data["curso_id"],
            "status": data["status"],
        }

        write_csv(
            "matriculas.csv",
            matricula,
            ["id", "aluno_id", "curso_id", "status"]
        )

        return jsonify({"message": "Matrícula criada!", "data": matricula}), 201
        
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "avaliacoes/listar_avaliacoes.yml"))
@app.route("/avaliacoes", methods=["GET"])
def listar_avaliacoes():    
    try:
        return jsonify(read_csv("avaliacoes.csv"))
    except FileNotFoundError:
        return jsonify({"error": "Arquivo de avaliações não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "avaliacoes/criar_avaliacao.yml"))
@app.route("/avaliacoes", methods=["POST"])
def criar_avaliacao():    
    try:
        data = request.get_json()
        
        campos_obrigatorios = ["curso_id", "titulo", "nota_maxima"]
        valido, erro = validar_campos_obrigatorios(data, campos_obrigatorios)
        
        if not valido:
            return jsonify({"error": erro}), 400
        
        next_id = get_next_id("avaliacoes.csv")
        
        avaliacao = {
            "id": str(next_id),
            "curso_id": data["curso_id"],
            "titulo": data["titulo"],
            "nota_maxima": data["nota_maxima"],
        }

        write_csv(
            "avaliacoes.csv",
            avaliacao,
            ["id", "curso_id", "titulo", "nota_maxima"]
        )

        return jsonify({"message": "Avaliação cadastrada!", "data": avaliacao}), 201
        
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "resultados/listar_resultados.yml"))
@app.route("/resultados", methods=["GET"])
def listar_resultados():    
    try:
        return jsonify(read_csv("resultados.csv"))
    except FileNotFoundError:
        return jsonify({"error": "Arquivo de resultados não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@swag_from(os.path.join(DOCS_DIR, "resultados/criar_resultado.yml"))
@app.route("/resultados", methods=["POST"])
def criar_resultado():    
    try:
        data = request.get_json()
        
        campos_obrigatorios = ["aluno_id", "avaliacao_id", "nota", "data_aplicacao"]
        valido, erro = validar_campos_obrigatorios(data, campos_obrigatorios)
        
        if not valido:
            return jsonify({"error": erro}), 400
        
        next_id = get_next_id("resultados.csv")
        
        resultado = {
            "id": str(next_id),
            "aluno_id": data["aluno_id"],
            "avaliacao_id": data["avaliacao_id"],
            "nota": data["nota"],
            "data_aplicacao": data["data_aplicacao"],
        }

        write_csv(
            "resultados.csv",
            resultado,
            ["id", "aluno_id", "avaliacao_id", "nota", "data_aplicacao"]
        )

        return jsonify({"message": "Resultado registrado!", "data": resultado}), 201
        
    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
