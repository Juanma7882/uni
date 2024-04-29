using System;
using System.Timers;


namespace Hola_Mundo
{
    class Program
    {
        static void Main(string[] args)
        {
            List<double> lista_numeros = new List<double>();

            Console.WriteLine("ingrese 5 numeros");
            int contador = 0;
            double maximo = 0;
            double minimo = 0;
            double acumulador = 0;
            double promedio = 0;
            while (contador < 5)
            {


                double numero_ingresado;
                if (double.TryParse(Console.ReadLine(), out numero_ingresado))
                {

                    contador += 1;
                    lista_numeros.Add(numero_ingresado);
                    Console.WriteLine($"Número ingresado: {numero_ingresado}");
                    Console.WriteLine($"Faltan {5 - contador} números por ingresar.");
                    maximo = numero_ingresado;
                    minimo = numero_ingresado;
                    acumulador += numero_ingresado;
                }
                else
                {
                    Console.WriteLine("Entrada inválida. Por favor, ingrese un número decimal o entero valido:");
                }


            }
            
            foreach (double numeros in lista_numeros)
            {
            
                    if (minimo > numeros)
                    {
                        minimo = numeros;
                    }
                    if (maximo < numeros)
                    {
                        maximo = numeros;
                    }
            }

            int longitud = lista_numeros.Count();
            if (acumulador == 0 )
            {
                Console.WriteLine("el resultado dio 0");
            }
            else
            {
                promedio = acumulador / longitud;
                Console.WriteLine($" el promedio de los numeros ingresados dio : {promedio}");

            }


            Console.WriteLine($" lista de max : {maximo}");
            Console.WriteLine($" lista de min : {minimo}");
            Console.WriteLine($" lista de numeros ingresados :");

            foreach (double numeros in lista_numeros)
            {
                Console.WriteLine($" lista de numero : {numeros}");
            }
        } 
    }
}