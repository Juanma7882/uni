using System;

public static class Validador
{
    public static bool ValidarRespuesta(string respuesta)
    {

        return respuesta.ToUpper() == "S";
    }
}

public class Program
{
    public static void Main()
    {
        int suma = 0;
        bool continuar = true;

        while (continuar)
        {
            Console.Write("Ingrese un número entero: ");
            int numero;
            if (int.TryParse(Console.ReadLine(), out numero))
            {
                suma += numero;
            }
            else
            {
                Console.WriteLine("Error: Debe ingresar un número entero válido.");
            }

            Console.Write("¿Desea continuar? (S/N): ");
            string respuesta = Console.ReadLine();

            // Validar respuesta usando el método ValidarRespuesta de la clase Validador
            continuar = Validador.ValidarRespuesta(respuesta);
        }

        Console.WriteLine("La suma de los números ingresados es: " + suma);
        Console.WriteLine("Programa finalizado.");
    }
}
