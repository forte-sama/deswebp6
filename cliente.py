from osa import Client

def crear(cliente):
    print "Creacion de nuevo estudiante:"
    # obtener datos de entrada
    mat = int(raw_input("Digite su nueva matricula: "))
    nom = raw_input("Escriba su nombre: ")
    car = raw_input("Ahora escriba a que carrera pertenece: ")

    # creando nueva instancia de estudiante
    new_est = cliente.types.estudiante()
    new_est.matricula   = mat
    new_est.nombre      = nom
    new_est.carrera     = car
    new_est.asignaturas = crear_lista_materias(cliente)

    # crear estudiante en servicio
    res = cliente.service.crearEstudiante(new_est)

    # mostrar mensaje en caso de exito
    if res is not None:
        print "Se creo estudiante con matricula: " + str(res.matricula) + "!"
    return

def modificar(cliente):
    print "Edicion de un estudiante:"
    # obtener datos de entrada
    mat = int(raw_input("Digite matricula de quien desea editar: "))
    nom = raw_input("Escriba su nuevo nombre: ")
    car = raw_input("Ahora escriba a que nueva carrera pertenece: ")

    # creando nueva instancia de estudiante
    actual = cliente.types.estudiante()
    actual.nombre       = nom
    actual.matricula    = mat
    actual.carrera      = car
    actual.asignaturas  = crear_lista_materias(cliente)

    # modificando estudiante en servicio
    res = cliente.service.modificarEstudiante(actual)

    # mostrar mensaje en caso de exito
    if res is not None:
        print "Se modifico estudiante con matricula: " + str(res.matricula) + "!"
    return

def eliminar(cliente):
    print "Eliminacion de estudiante:"
    # obtener datos de entrada
    mat = int(raw_input("Digite matricula de quien desea eliminar: "))
    # realizar operacion en el servicio
    cliente.service.eliminarEstudiante(mat)
    # mostrar mensaje con resultado
    print "Se elimino estudiante con matricula: " + str(mat) + "..."
    return

def obtener(cliente):
    print "Obtener estudiante por matricula:"
    # obtener datos de entrada
    mat = int(raw_input("Digite matricula que desea ver: "))
    # tratara de obtener instancia de estudiante desde el servicio
    est = cliente.service.obtenerEstudiante(mat)

    # imprimir resultado en caso de exito/fallo
    if est is not None:
        print "Estudiante obtenido: "
        imprimir_estudiante(est)
    else:
        print "No se obtuvo estudiante"
    return

def listar(cliente):
    print "Listado de estudiantes:"
    # obtener lista desde el servicio
    lista_estudiantes = cliente.service.listarEstudiantes()

    # mostrar listado o mensaje en caso de fallo
    if lista_estudiantes is not None:
        for e in lista_estudiantes:
            imprimir_estudiante(e)
    else:
        print "No hay ningun estudiante registrado"
    return

def imprimir_estudiante(e):
    # imprimir datos basicos de un estudiante
    print str(e.matricula) + " : " + e.nombre + ", " + e.carrera + "\nAsignaturas:"

    # iterar mostrando su lista de asignatura, mensaje en caso contrario
    if e.asignaturas is not None:
        for a in e.asignaturas:
            print "\t" + a.codigo + ", " + a.nombre
    else:
        print "\tNo tiene"

    return

def crear_lista_materias(cliente):
    # aqui se guardaran las asignaturas
    lista = []

    # variable flag para texto de ayuda
    iniciado = False;

    while True:
        texto = "otra" if iniciado else "una"
        # obtener respuesta
        if raw_input("Desea registrarle " + texto + " materia? ").strip() == "si":
            iniciado = True

            # do the thing
            # nueva instancia de una asignatura, segun el servicio
            new_asg = cliente.types.asignatura()
            new_asg.codigo = raw_input("Digite el codigo de la asignatura: ")
            new_asg.nombre = raw_input("Ahora escribe su nombre: ")

            lista.append(new_asg)
        else:
            break

    return lista


# creacion de cliente del servicio web
c = Client("http://localhost:9001/ServicioEstudiante?wsdl")

# main loop del programa
while True:
    print "\n\nOpciones:"
    print "1. Crear nuevo estudiante."
    print "2. Modificar estudiante."
    print "3. Eliminar estudiante."
    print "4. Obtener estudiante usando su matricula."
    print "5. Ver lista de estudiantes."
    option = raw_input().strip()

    if option == "1":
        crear(c)
    elif option == "2":
        modificar(c)
    elif option == "3":
        eliminar(c)
    elif option == "4":
        obtener(c)
    elif option == "5":
        listar(c)
    else:
        print "\nEsa opcion no estaba en la lista..."
        option = raw_input("En serio desea salir? (si/no)\n").strip()

        if option == "si":
            break;
