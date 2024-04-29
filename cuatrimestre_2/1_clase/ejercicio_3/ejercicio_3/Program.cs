//Ejercicio I03 - Los primos
//Consigna
//Mostrar por pantalla todos los números primos que haya hasta el número que ingrese el usuario por consola.
//Validar que el dato ingresado por el usuario sea un número.
//Volver a pedir el dato hasta que sea válido o el usuario ingrese "salir".
//Si ingresa "salir", cerrar la consola.
//Al finalizar, preguntar al usuario si desea volver a operar. Si la respuesta es afirmativa, iterar. 
//De lo contrario, cerrar la consola.

using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        while (true)
        {
            Console.WriteLine("Ingrese un número mayor a 1 para determinar si es primo:");
            string input = Console.ReadLine();
            List<int> listaPrimos = new List<int>(); // Lista para almacenar los números primos encontrados

            if (int.TryParse(input, out int numero) && numero > 1)
            {
                // Cambio en el bucle for para que se ejecute solo hasta el número ingresado
                for (int numeros = 2; numeros <= numero; numeros++)
                {
                    bool esPrimo = true;

                    for (int i = 2; i <= Math.Sqrt(numeros); i++)
                    {
                        if (numeros % i == 0)
                        {
                            esPrimo = false;
                            break; // Salir del bucle si encuentra un divisor
                        }
                    }

                    if (esPrimo)
                    {
                        listaPrimos.Add(numeros); // Agregar número primo a la lista
                        Console.WriteLine($"Guardando primo: {numeros}");
                    }
                }

                Console.WriteLine("Números primos encontrados:");
                foreach (int primo in listaPrimos)
                {
                    Console.WriteLine(primo);
                }
            }
            else
            {
                Console.WriteLine("Ingrese un número válido mayor a 1.");
            }
        }
    }
}
