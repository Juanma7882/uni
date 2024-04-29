using System;
using static System.Runtime.InteropServices.JavaScript.JSType;
using System;

namespace Hola_Mundo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Ingrese un número:");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int numero))
            {
                int maximoAsteriscos = 2 * numero - 1; // Máximo de asteriscos en la última fila
                int vacio = maximoAsteriscos / 2; // Cantidad de espacios en blanco para centrar

                for (int fila = 1; fila <= numero; fila++)
                {
                    string espacios = new string(' ', vacio);
                    string patron = new string('*', 2 * fila - 1); // Patrón de asteriscos
                    Console.WriteLine(espacios + patron);
                    vacio--; // Reducir espacios en blanco para las siguientes filas
                }
            }
            else
            {
                Console.WriteLine("Número inválido.");
            }
        }
    }
}