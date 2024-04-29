using System; // El ; indica el fin de la declaración

// 'namespace' define el tipo de bloque. 'Hola_Mundo' es un nombre o identificador para ese bloque. 

using biblioteca;

namespace hello_word
{
    class Programa
    {
        static void Main(string[] args)
        {
            Console.WriteLine("nombre");
            string nombre = Console.ReadLine();

            Console.WriteLine("dni");
            int dni = int.Parse(Console.ReadLine());
            
            Console.WriteLine("Ingrese su fecha de nacimiento (formato dd/MM/yyyy):");
            DateTime fechaNacimiento;
            if (DateTime.TryParseExact(Console.ReadLine(), "dd/MM/yyyy", null, System.Globalization.DateTimeStyles.None, out fechaNacimiento))
            {
                Persona persona = new Persona(nombre, fechaNacimiento, dni); // Crear una instancia de Persona

                Console.WriteLine("Datos ingresados:");
                persona.Mostrar(); // Llamar al método Mostrar de la instancia persona
            }

           
        }
    }
}
