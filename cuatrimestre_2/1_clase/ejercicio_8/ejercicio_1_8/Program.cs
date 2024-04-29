using System;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Hola_Mundo
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Console.WriteLine("Hello World!");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int numero))
            {
                Console.WriteLine("");
                Console.WriteLine("");
                for (int fila = 1; fila <= numero; fila++)
                {

                    string patron = new string('*', fila); 
                    Console.WriteLine(patron); 
                }
            }
        }
    }
}