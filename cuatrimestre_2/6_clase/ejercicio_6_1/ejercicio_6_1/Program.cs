using biblioteca;

namespace poo
{
    class YoPuedo
    {
        public static void Main(String[] args)
        {
            Moto miMoto = new Moto(150, 2, 2, Colores.Rojo);
            string mensajeMoto = miMoto.mensaje();
            Console.WriteLine(mensajeMoto);

            Camion camion = new Camion(4 , 100 , 4 , 4 , Colores.Gris);
            string mensajecamion = camion.mensaje();
            Console.WriteLine(mensajecamion);

            Auto auto = new Auto(4, 4, 5, 6, Colores.Azul);
            string mensajeauto = auto.mensaje();
            Console.Write(mensajeauto);
        }

    }
}
