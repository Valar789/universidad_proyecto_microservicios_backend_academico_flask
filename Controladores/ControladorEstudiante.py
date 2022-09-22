from Modelos.Estudiante import Estudiante
from Repositorios.RepositorioEstudiante import RepositorioEstudiente

class ControladorEstudiante():
    def __init__(self):
        #print("Creando ControladorEstudiante")
        self.repositorioEstudiante = RepositorioEstudiente()

    # Funcion que trae la lista de todos los estudiantes con sus atributos
    def index(self):
        """
        print("Listar todos los estudiantes")
        unEstudiante = {
            "_id": "abc123",
            "cedula": "123",
            "nombre": "Eduar",
            "apellido": "Mendez"
        }
        return [unEstudiante]"""
        return self.repositorioEstudiante.findAll()

    # Funcion para crear un objeto de estudiante
    def create(self, infoEstudiante):
        """ print("Crear un estudiante")
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__"""
        nuevoEstudiante = Estudiante(infoEstudiante)
        return self.repositorioEstudiante.save(nuevoEstudiante)

    # Funcion para mostrar un objeto según su identificador
    def show(self, id):
        """print("Mostrando un estudiante con id ", id)
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Eduar",
            "apellido": "Mendez"
        }
        return elEstudiante"""
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__

    # Funcion para actualizar la informacion de un estudiante
    def update(self, id, infoEstudiante):
        """print("Actualizando estudiante con el id ", id)
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__"""
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula = infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)

    # Funcion para eliminar un estudiante
    def delete(self, id):
        """print("Eliminando estudiante con el id ", id)
        return {"deleted_count": 1}"""
        return self.repositorioEstudiante.delete(id)

