using System;

namespace biblioteca_1
{
    public class Cuenta
    {
        private string Titular;
        private double Cantidad;

        public Cuenta(string nombreTitular, double cantidadInicial)
        {
            Titular = nombreTitular;
            Cantidad = cantidadInicial;
        }

        public string MostrarNombre
        {
            get { return Titular; }
        }

        public double MostrarSaldo
        {
            get { return Cantidad; }
        }

        public void MostrarDatosCuenta()
        {
            Console.WriteLine($"Titular: {MostrarNombre}");
            Console.WriteLine($"Saldo: {MostrarSaldo}");
        }

        public void Ingresar(float cantidad)
        {
            if (cantidad > 0)
            {
                Cantidad += cantidad;
                Console.WriteLine($"Se ha ingresado {cantidad} a la cuenta.");
            }
            else
            {
                Console.WriteLine("La cantidad a ingresar debe ser mayor que cero.");
            }
        }

        public void Retirar(float cantidad)
        {
            if (cantidad < 0 )
            {
                Cantidad += cantidad;
                Console.WriteLine($"Se ha retirado {cantidad} de la cuenta.");
            }
            else
            {
                Console.WriteLine("No se puede retirar la cantidad especificada.");
            }
        }
    }
}
