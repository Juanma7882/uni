using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

//public protected internal protected internal private protected private



namespace biblioteca
{
    public class Moto : VehiculoTerrestre
    {
        short cilindrada;

        public Moto(short cilindrada, short cantidadRuedas, short cantidadPuertas, Colores colorPrincipal)
            : base(cantidadRuedas, cantidadPuertas, colorPrincipal)
        {
            this.cilindrada = cilindrada;
        }
        public override string mensaje()
        {
            string mensaje = base.mensaje(); // Llama al método base para obtener el mensaje base
            mensaje += $"cilindrada de la moto: {cilindrada}\n";
            return mensaje;
        }
    }
}
