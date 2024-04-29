




//Ingresar un número y mostrar el cuadrado y el cubo del mismo. Se debe validar que el número sea mayor que cero,
//caso contrario, mostrar el mensaje: "ERROR. ¡Reingresar número!".
class Program
{
    static void Main(string[] args)
    {
        bool bandera = true;
        while (bandera)
        {
            Console.WriteLine("Ingrese un número para saber cuál es su cuadrado");
            string input = Console.ReadLine();
            {
                int cuadrado = numero * numero;
                int cubo = numero * numero * numero;
                Console.WriteLine($"El número ingresado es              | {numero}");
                Console.WriteLine($"El cuadrado del número ingresado es | {cuadrado}");
                Console.WriteLine($"El cubo del número ingresado es     | {cubo}");
            }
            else
            {
                Console.WriteLine("Ingrese un valor válido");
                continue; // Vuelve al inicio del bucle para pedir otro número
            }

            Console.WriteLine("Si desea continuar presione cualquier tecla, si desea salir presione 0");
            string inputContinuar = Console.ReadLine();

            if (int.TryParse(inputContinuar, out int opcion) && opcion == 0)
            {
                bandera = false; // Sale del bucle y termina el programa
            }
           
             
        }
    }
}


