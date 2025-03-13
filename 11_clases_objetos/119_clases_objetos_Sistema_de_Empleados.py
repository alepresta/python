print('****************** CLASES Y OBJETOS ******************* ')
print('****************  SISTEMA EMPLEADOS  ****************** ')


class Empleados:
    cantidad_empleados = 0  # Contador de empleados (atributo de clase)

    def __init__(self, nombre, departamento):
        self.nombre = nombre  # Nombre del empleado
        self.departamento = departamento  # Departamento del empleado
        Empleados.cantidad_empleados += 1  # Incrementa el contador de empleados

    @classmethod
    def obtener_total_empleados(cls):
        return cls.cantidad_empleados  # Retorna el total de empleados


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la empresa
        self.empleados = []  # Lista para almacenar empleados

    def contratar_empleado(self, nombre, departamento):
        nuevo_empleado = Empleados(nombre, departamento)  # Crea un nuevo empleado
        self.empleados.append(nuevo_empleado)  # Agrega el empleado a la lista
        print(f'Empleado {nombre} contratado en el departamento {departamento}.')

    def obtener_numero_empleados_por_departamento(self, departamento):
        # Cuenta cuántos empleados hay en un departamento específico
        count = sum(1 for emp in self.empleados if emp.departamento == departamento)
        return count


if __name__ == '__main__':
    # Crear una empresa
    empresa = Empresa(nombre='TechCorp')

    # Contratar empleados
    empresa.contratar_empleado(nombre='Alejo', departamento='QA')
    empresa.contratar_empleado(nombre='María', departamento='Desarrollo')
    empresa.contratar_empleado(nombre='Carlos', departamento='QA')
    empresa.contratar_empleado(nombre='Laura', departamento='Ventas')

    # Obtener el número total de empleados
    print(f'Cantidad total de empleados: {Empleados.obtener_total_empleados()}')

    # Obtener el número de empleados por departamento
    print(f'Empleados en QA: {empresa.obtener_numero_empleados_por_departamento("QA")}')
    print(f'Empleados en Desarrollo: {empresa.obtener_numero_empleados_por_departamento("Desarrollo")}')
    print(f'Empleados en Ventas: {empresa.obtener_numero_empleados_por_departamento("Ventas")}')