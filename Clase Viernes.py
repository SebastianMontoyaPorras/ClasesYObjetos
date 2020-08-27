# crear la primera clases y objetos


#clasesy objetos
class latinos():
    Nombre=""
    Genero=""
    Edad=""
    persona=latinos()
    persona.Nombre=str(input("Digite su Nombre"))
    persona.Genero = str(input("Digite su Genero"))
    persona.Edad = int(input("Digite su Edad"))
    print(f"su Nombre es :{persona.Nombre},su Genero es :{persona.Genero},su Edad es :{persona.Edad}")

    class latinos():
        Nombre = ""
        Genero = ""
        Edad = ""
        def nostar(self):
            pass
        persona = latinos()
        persona.Nombre = str(input("Digite su Nombre"))
        persona.Genero = str(input("Digite su Genero"))
        persona.Edad = int(input("Digite su Edad"))
        print(f"su Nombre es :{persona.Nombre},su Genero es :{persona.Genero},su Edad es :{persona.Edad}")


#ejercicio 2 de manual logica

class Salarios():
    SueldoBase=""
    PrimeraVentaComision=""
    SegundaVentaComision=""
    TerseraVentaComision= ""
    SGeneral=Salarios()
    SGeneral.SueldoBase=int(input("Digite su SueldoBase"))
    SGeneral.PrimeraVentaComision= int(input("Digite su PrimeraVentaComision"))
    SGeneral.SegundaVentaComision= int(input("Digite su SegundaVentaComision"))
    SGeneral.TerseraVentaComision = int(input("Digite su TerseraVentaComision"))
    totalventas=PrimeraVentaComision+SegundaVentaComision+TerseraVentaComision
    Comision=totalventas*0.10
    SueldoTotal=SueldoBase+Comision
    print(f"su sueldo total con comisiones es:{SueldoTotal}")

    class Salarios():
        SueldoBase = ""
        PrimeraVentaComision = ""
        SegundaVentaComision = ""
        TerseraVentaComision = ""
        def nostar(self):
            pass
    SGeneral=Salarios()
    SGeneral.SueldoBase=int(input("Digite su SueldoBase"))
    SGeneral.PrimeraVentaComision= int(input("Digite su PrimeraVentaComision"))
    SGeneral.SegundaVentaComision= int(input("Digite su SegundaVentaComision"))
    SGeneral.TerseraVentaComision = int(input("Digite su TerseraVentaComision"))
    totalventas=PrimeraVentaComision+SegundaVentaComision+TerseraVentaComision
    Comision=totalventas*0.10
    SueldoTotal=SueldoBase+Comision
    print(f"su sueldo total con comisiones es:{SueldoTotal}")


#libreria TKINTER

#instalacion libreria

from tkinter import*

ventana=Tk()
ventana.geometry("600x500")
ventana.title("Aplicacion")

boton1=booton(ventana,text="Inicio")
boton1.grid(row=8,column=8)
boton2=booton(ventana,text="Archivos")
boton2.grid(row=8,column=1)
ventana.mainloop()