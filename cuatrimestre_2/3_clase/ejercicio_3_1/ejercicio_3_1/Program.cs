using System;
using biblioteca_1;

public class Calculadora
{
    public static void Main()
    {
        
        string nombreTitular = "pantera";
        float saldoInicial = 10.0f;
        Cuenta cuenta = new Cuenta(nombreTitular, saldoInicial);
        cuenta.MostrarDatosCuenta();  // Mostrar los datos de la cuenta

        cuenta.Ingresar(100); //  ingreso de 100 unidades
        cuenta.MostrarDatosCuenta();
        
        //(esto esta mal deberias ATENCION nesesita modicar para implementar en otro lado)
        cuenta.Retirar(-50);   //  retiro de 50 unidades
        cuenta.MostrarDatosCuenta();


    }
}
