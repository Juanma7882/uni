using System.Net;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace biblioteca
{
    public class Persona
    {
        private string nombre;
        private DateTime fechaDeNacimiento;
        private int dni;

        public  Persona(string nombre, DateTime fechaDeNacimiento, int dni)
        { 
            this.nombre = nombre;
            this.fechaDeNacimiento = fechaDeNacimiento;
            this.dni = dni;

        }

        public string Nombre
        {
            get { return nombre; }
            set { nombre = value; }
        }

        public int Dni
        {
            get { return dni; }
            set { dni = value; }
        }

        public DateTime FechaDeNacimiento
        {
            get { return fechaDeNacimiento; }
            set { fechaDeNacimiento = value; }
        }


        private int CalcularEdad()
        {
            DateTime fechaActual = DateTime.Today;
            int edad = fechaActual.Year - fechaDeNacimiento.Year;
            if (fechaActual < fechaDeNacimiento.AddYears(edad))
            {
                edad--;
            }
            return edad;
        }

        public void Mostrar()
        {
            Console.WriteLine($"Nombre : {nombre}");
            Console.WriteLine($"Edad   : {CalcularEdad()}");
            Console.WriteLine($"DNI    : {dni}");
            Console.WriteLine($"Mayor de edad  : {EsMayorDeEdad()}");
            Console.WriteLine($"Fecha de Nacimiento : {FechaDeNacimiento}");

        }

        public  string EsMayorDeEdad()
        {
            int edad = CalcularEdad();
            if (edad >= 18)
            {
                return "si";
            }
            else
            {
                return "No";
            }
        }
    }
}
