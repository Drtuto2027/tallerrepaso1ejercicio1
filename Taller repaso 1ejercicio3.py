from asyncio import streams


class Pacientes ():
      def __init__(self,nombre,edad,sexo,presion):
        self.nombre=nombre
        self.edad=edad 
        self.sexo=sexo
        self.presion=presion
        
        def getNombre(self):
          return self.nombre
      
        def getEdad(self):
          return self.edad
       
        def getSexo(self):
          return self.sexo
        
        def getPresion(self):
          return self.presion
      
      
        def setNombre(self,nombre):
              self.nombre=nombre
    
    
        def setEdad(self,edad):
            self.edad=edad
            
            
        def setSexo(self,sexo):
            self.sexo=sexo
            
        def setPresion(self,presion):
            self.presion=presion
            
def  cantidadPacientessPresionMayor140(pacientes):
         contador = 0
         for paciente in paciente:
            if paciente.getPresion() >=140 and paciente.getEdad()>=50:
                  acumulado += paciente.getPrecion()
            print('el total de pacientes con la precion mayor a 140 y mayores de 50 años es de: ',acumulado)
            

def calcularPacientesPresionRagoNormal(pacientes):
    cantidad=0
    for paciente in paciente:
        if 90 <= paciente.getPresion() <= 120 and paciente.getEdad()<30:
            cantidad +1
            print('el total de pacientes con la precion entre el rago 90-120 y mayores de 50 años es de: ',cantidad)
            
    
def calcularPromedioPresionSuperior130(paciente):
        acumulado = 0
        cantidad = 0
        for paciente in paciente:
            if paciente.getPrecion() >=130:
             acumulado += paciente.getPrecion()
            cantidad += 1
        if cantidad == 0:
            print('No hay pacientes con la presion superiro a 130 ')
        else:
            promedio = acumulado / cantidad
            print('El promedio de pacientes con la presion superiroa 130 es de : ', promedio)

def cantidaPacientesEdadMayo60Años(paciente):
     cantidad=0
     for paciente in paciente:
         if paciente.getEdad()>=60 and paciente.getPresion()<=90:
          cantidad += 1
         print('la cantidad de pacientes con edad mayor a 60 años y con presion menor a 90 es de : ',cantidad)

class Main():
          def main():    
            Pacientes=[]
            for i in range(20): 
                  nombre= input('por favor ingrese el nombre del empleado:')
                  edad= int(input('por favor ingrese la edad del empleado: '))
                  sexo= input('por favor ingrese el sexo del paciente ')
                  Presion= int(input('por favor ingrese la presion arterial del paciente: '))
                  print ('Se guardo de manera exitosa la informacion del Paciente')
                  Paciente = Pacientes (nombre,edad,sexo,Presion)
                  Pacientes.append(Paciente)
        
            cantidadPacientessPresionMayor140(Pacientes)
            calcularPacientesPresionRagoNormal(Pacientes)
            calcularPromedioPresionSuperior130(Pacientes)  
            cantidaPacientesEdadMayo60Años(Pacientes)

if __name__ == "__main__":
    Main.main()                 