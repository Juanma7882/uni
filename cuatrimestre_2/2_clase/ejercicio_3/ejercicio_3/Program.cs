using System;

public static class Validador
{
    public static float Calcular(float x, float y, string signo)
    {
        float calculo = 0;

        if (Validar(y))
        {
            Console.WriteLine("Número inválido");
        }
        else
        {
            switch (signo)
            {
                case "+":
                    calculo = x + y;
                    break;
                case "-":
                    calculo = x - y;
                    break;
                case "*":
                    calculo = x * y;
                    break;
                case "/":
                    calculo = x / y;
                    break;
                default:
                    Console.WriteLine("Error: Operador no válido.");
                    break;
            }
        }
        return calculo;
    }

    private static bool Validar(float y)
    {
        return y == 0;
    }
}

public class Calculadora
{
    public static void Main()
    {
        float resultado = 0;
        bool continuar = true;

        do
        {
            Console.WriteLine("Ingrese el primer número: ");
            float primer_numero = float.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese el signo de la operación entre los siguientes 4: + ; - ; * ; / ");
            string signo = Console.ReadLine();
            Console.WriteLine("Ingrese el segundo número: ");
            float segundo_numero = float.Parse(Console.ReadLine());

            resultado = Validador.Calcular(primer_numero, segundo_numero, signo);
            Console.WriteLine("El resultado es: " + resultado);

            Console.WriteLine("¿Desea realizar otra operación? (s/n)");
            string respuesta = Console.ReadLine();
            continuar = (respuesta.ToLower() == "s");
        } while (continuar);
    }
}
