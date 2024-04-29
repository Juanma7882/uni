using biblioteca_4_1;


namespace hello
{
    public class calculadora
    {
        static void Main(string[] args)
        {
            
            Sumador sumador = new Sumador();
            Console.WriteLine(sumador.sumar(30 ,50));// utilizamos sumar suma automaticamente 
            Console.WriteLine(sumador.sumar("HOLA" , "TODOS"));//dependiendo el tipo


            Sumador sumador1 = new Sumador(5);
            Sumador sumador2 = new Sumador(10);
            long sumaTotal = sumador1 + sumador2; // Esto utilizará la sobrecarga del operador + 
            Console.WriteLine($"La suma total es: {sumaTotal}");

            int a = 1   // si lo instaciamos asi y tratamos de comparar no va funcionar
            Sumador sumador3 = new Sumador(15);
            Sumador sumador4 = new Sumador(10);
            bool comparcion = sumador3 | sumador4; // Esto utilizará la sobrecarga del operador ==
            Console.WriteLine($"La comparcion  es: {comparcion}");


        }
    }
}