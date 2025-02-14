#nombre Empleado


print("--------------------------------------")
print('*** Sistma empleados ***')
print("--------------------------------------")

empleado_nombre = str(input('Ingrese su nombre: --> '))
empleado_edad = int(input('Ingrese su edad: --> '))
empleado_salario = float(input('Ingrese su salario: --> '))
empleado_o_jefe = (input('Ingrese true si es jefe departamento: (si/No) --> '))

empleado_o_jefe = empleado_o_jefe.lower() == 'si'

print("--------------------------------------")

print(f'Usted se llama: {empleado_nombre}')
print(f'Su edad es: {empleado_edad}')
print(f'Su ingreso es: {empleado_salario:.2f}')
print(f'Usted en jefe de departamento: {empleado_o_jefe}')