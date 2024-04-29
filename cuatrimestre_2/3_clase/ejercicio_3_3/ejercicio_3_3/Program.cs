using biblioteca;


namespace hello
{
    class Escuela
    {
        static void Main(string[] strings)
        {
            string Nombre = "pedro";
            string Apellido = "Mauricio";
            string Legajo = "desconosido";

            Estudiante Estudiante = new Estudiante(Nombre , Apellido ,Legajo);
            Estudiante.SetNotaPrimerParcial(6);
            Estudiante.SetNotaSegundoParcial(6);
            Console.WriteLine(Estudiante.mostrar());

            string Nombre2 = "Pantera";
            string Apellido2 = "Negra";
            string Legajo2 = "desconosido";

            Estudiante Estudiante_2 = new Estudiante(Nombre2, Apellido2, Legajo2);
            Estudiante.SetNotaPrimerParcial(2);
            Estudiante.SetNotaSegundoParcial(2);
            Console.WriteLine(Estudiante.mostrar());

            string Nombre3 = "Pikachu";
            string Apellido3 = "ash";
            string Legajo3 = "desconosido";

            Estudiante Estudiante_3 = new Estudiante(Nombre3, Apellido3, Legajo3);
            Estudiante.SetNotaPrimerParcial(3);
            Estudiante.SetNotaSegundoParcial(6);
            Console.WriteLine(Estudiante.mostrar());
        }
    }
}