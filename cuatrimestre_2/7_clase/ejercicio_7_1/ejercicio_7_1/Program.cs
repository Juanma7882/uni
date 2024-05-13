using formas;
namespace ejercicio7
{
    class Progam
    {
        static void Main(string[] args)
        {


            Circulo circulo = new Circulo(10);
            Console.WriteLine(circulo.Dibujar());

            Cuadrado cuadrado = new Cuadrado(32.2f);
            Console.WriteLine(cuadrado.Dibujar());

            Rectangulo rectangulo = new Rectangulo(12.2f, 10);
            Console.WriteLine(rectangulo.Dibujar());

            //1) ¿Por qué la clase Cuadrado no está obligada a implementar el método Dibujar ? ¿Las otras clases 
            //    están obligadas a hacerlo ?
            //2) ¿Por qué la clase Cuadrado no está obligada a implementar el método CalcularSuperficie ? 
            //    ¿Las otras clases están obligadas a hacerlo ?
            //3) ¿A qué implementación del método CalcularPerimetro llaman los objetos de tipo Cuadrado?
            
            //1) porque la clase cuadrado no hereda directamente a la clase abstracta figura 
            //2) por la misma razon no hereda directamente la clases cuadrado de circulo
            //3 llaman a la del padre rectangulo y el padre llama a la clase abstracta
        }
    }
}