using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // utilizo un bucle para iterar hasya que el usuario lo desee  
        var diccionario = new Dictionary<string, int>();
        while (true)
        {
            Console.WriteLine("Ingrese una frase (escriba 'salir' para finalizar):");
            string entrada = Console.ReadLine();

            entrada = entrada.ToLower();

            string[] palabras = entrada.Split(' ', StringSplitOptions.RemoveEmptyEntries);

            if (palabras.Contains("salir") || palabras.Contains("exit"))
            {
                break;
            }

            // Contar las palabras
            foreach (string palabra in palabras)
            {
                if (diccionario.ContainsKey(palabra))
                {
                    diccionario[palabra]++;
                }
                else
                {
                    diccionario[palabra] = 1;
                }
            }
        }

        //Console.WriteLine("Conteo de palabras:");
        //foreach (var ClaveValor in diccionario)
        //{
        //    Console.WriteLine($"Palabra: '{ClaveValor.Key}', Cantidad: {ClaveValor.Value}");
        //}


        var top3 = diccionario.OrderByDescending(x => x.Value).Take(3);
        Console.WriteLine("\nTop 3 de palabras más usadas:");
        foreach (var kvp in top3)
        {
            Console.WriteLine($"Palabra: '{kvp.Key}', Cantidad: {kvp.Value}");
        }


    }
}
