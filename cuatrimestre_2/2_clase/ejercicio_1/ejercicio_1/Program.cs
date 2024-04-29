using System.Drawing;

public static class Validar
{
    public static int Minimo = -100;
    public static int Maximo = 100;
    
        
    public static bool Validar_numero(int valor, int min = -100, int max = 100)
    {
        if (min == -100) min = Minimo; // Usar Minimo predefinido si no se proporciona min
        if (max == 100) max = Maximo; // Usar Maximo predefinido si no se proporciona max
        //Console.WriteLine($"valor maximo {max}");
        //Console.WriteLine($"valor minimo {min}");

        return valor >= min && valor <= max;

    }
    public static int Numero_minimo(List<int> valores)

    {
        int minimo = valores[0]; // Inicializamos minimo con el primer elemento de la lista

        for (int i = 1; i < valores.Count; i++)
        {
            if (valores[i] < minimo)
            {
                minimo = valores[i];
            }
        }

        return minimo;
    }

        
    public static int Numero_maximo(List<int> valores)
    {
        int maximo = valores[0]; // Inicializamos minimo con el primer elemento de la lista

        for (int i = 1; i < valores.Count; i++)
        {
            if (valores[i] > maximo)
            {
                maximo = valores[i];
            }
        }

        return maximo;

    }

    public static float promedio(List<int> valores)
    {
        float promedio = 0;
        int tamano = valores.Count;
        float suma = 0;
        for (int i = 0; i < tamano; i++)
        {
            suma += valores[i];
        }
        promedio = suma / tamano;
        return promedio;
    }
}


    class Validador
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Ingresar un número maximo:");
            int.TryParse(Console.ReadLine(), out var valor_maximo);

            Console.WriteLine("Ingresar un número minimo:");
            int.TryParse(Console.ReadLine(), out var valor_minimo);

            int vueltas = 10;
            List<int> list = new List<int>();
            while (vueltas > 0)
            {

                Console.WriteLine("Ingresar un número a validar:");
                if (int.TryParse(Console.ReadLine(), out int numero))
                {
                    if (Validar.Validar_numero(numero, valor_minimo, valor_maximo))
                    {
                        vueltas = vueltas - 1;
                        list.Add(numero);
                        Console.WriteLine($"El número ingresado está dentro del rango. {vueltas}/10 ");
                    }
                    else
                    {
                        Console.WriteLine("El número ingresado está fuera del rango.");
                    }
                }
                else
                {
                    Console.WriteLine("Error: Ingrese un número válido.");
                }
            }

            Console.WriteLine($"NUMERO MAXIMO | {Validar.Numero_maximo(list)}");
            Console.WriteLine($"NUMERO MINIMO | {Validar.Numero_minimo(list)}");
            Console.WriteLine($"PROMEDIO      | {Validar.promedio(list)}");

        }
}

