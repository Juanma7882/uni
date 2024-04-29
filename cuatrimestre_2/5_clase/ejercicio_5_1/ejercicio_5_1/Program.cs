using System.Collections.Generic; 
using System;
namespace Hola_Mundo 
{
    
    class Program
    {
        static void Main(string[] args)
        {
            List<int> list = new List<int>();
            List<int> positivos = new List<int>();
            List<int> negativos = new List<int>();

            for (int vueltas = 0; vueltas < 20;)
            {
                Random numeros_random = new Random();
                int numeroAleatorio = numeros_random.Next(-100, 101);

                if (numeroAleatorio != 0)
                {
                    list.Add(numeroAleatorio);
                    vueltas++;
                }
            }

            foreach (int i in list)
            {
                Console.WriteLine(i);
                if (i > 0)
                {
                    positivos.Add(i);
                }
                else
                {
                    negativos.Add(i);
                }
            }

            negativos.Reverse();
            positivos.Sort();

            Console.WriteLine("numeros positivos");
            foreach (int i in positivos)
            {
                Console.WriteLine(i);
            }

            Console.WriteLine("numeros negativos");
            foreach (int i in negativos)
            {
                Console.WriteLine(i);
            }
        }
    }
} 
