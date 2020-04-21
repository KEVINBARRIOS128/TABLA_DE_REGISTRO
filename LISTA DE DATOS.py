listaAlumnos = []
listaCursos = []
listaAsignados = []


def ingresaralumno(carne, nombre, seccion):
    listaAlumnos.append([carne, nombre, seccion])
    print("Alumno Ingresado Exitosamente")


def ingresarcurso(nombrecurso):
    listaCursos.append(nombrecurso)
    print("Curso Ingresado Exitosamente")


def buscaralumno(carne):
    posicion = 0
    encontrado = False
    for alumno in listaAlumnos:
        if alumno[0] == carne:
            encontrado = True
            break
        else:
            posicion = posicion + 1

    if not encontrado:
        posicion = -1

    return posicion


def buscarcurso(nombrecurso):
    posicion = 0
    encontrado = False
    for curso in listaCursos:
        if curso == nombrecurso:
            encontrado = True
            break
        else:
            posicion = posicion + 1

    if not encontrado:
        posicion = -1

    return posicion

def buscar_registro(carne):
    posicion = 0
    encontrado = False
    for registro in listaAsignados:
        if registro[0][0] == carne:
            encontrado = True
            break
        else:
            posicion += 1

    if not encontrado:
        posicion = -1

    return posicion


def mostrarcursos():
    for cursos in listaCursos:
        print(cursos)


def asignarcurso():
    #for alumno in listaAlumnos: #chivo para tabular
        #print("{:2} {:2} {:2} ".format(alumno[0], alumno[1], alumno[2]))

    carne = input("Ingrese el carne del alumno: ")
    posicionAlumno = buscaralumno(carne)
    if posicionAlumno != -1:
        mostrarcursos()
        nombreCurso = input("Ingrese el curso a asignar: ")
        posicionCurso = buscarcurso(nombreCurso)
        if posicionCurso != -1:
            listaAsignados.append([listaAlumnos[posicionAlumno], listaCursos[posicionCurso]])

        else:
            print("CURSO NO ENCONTRADO!!!!")
    else:
        print("ALUMNO NO ENCONTRADO!!!!")

def ver_registros():
    Carne = "Carne"
    Nombre = "Nombre"
    Seccion = "Seccion"
    Curso = "Curso"
    Nota = "Nota"
    print("{:10} {:10} {:10} {:10} {:10} ".format(Carne, Nombre, Seccion, Curso,Nota))
    for registro in listaAsignados:
        print("{:10} {:10} {:10} {:10} {:2}".format(registro[0][0], registro[0][1], registro[0][2], registro[1], registro[2]))
        #print(registro)

def asignarnota():
    #ver_registros()
    carne = input("ingrese el carne del alumno: ")
    posicionregistro = buscar_registro(carne)

    if posicionregistro != -1:
        nota = int(input("Ingrese La Nota: "))
        listaAsignados[posicionregistro].append(nota)
        print("NOTA INGRESADA EXITOSAMENTE!!!")


def switch(opcion):
    if opcion == 1:
        carne = input("Ingrese el carne del Alumno: ")
        nombre = input("Ingrese el nombre del Alumno: ")
        seccion = input("Ingrese la seccion: ")
        ingresaralumno(carne, nombre, seccion)
    elif opcion == 2:
        curso = input("Ingrese el nombre del Curso: ")
        ingresarcurso(curso)
    elif opcion == 3:
        asignarcurso()
    elif opcion == 4:
        asignarnota()
    elif opcion == 5:
        ver_registros()
    else:
        print("******OPCION INVALIDA******\n")


while True:
    opcion = int(input("Seleccione Una Opcion \n"
                       "1. Ingresar Alumno \n"
                       "2. Ingresar Curso \n"
                       "3, Asignar Curso \n"
                       "4. Asignar Nota \n"
                       "5. Ver Registros \n"
                       "Opcion: "))
    switch(opcion)