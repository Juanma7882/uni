using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace biblioteca
{
    public class Camion : VehiculoTerrestre
    {
        short cantidadMarchas;
        int pesoCarga;

        public Camion(short cantidad_marchas, int peso_carga, short cantidad_ruedas, short cantidad_puertas, Colores Colores)
            : base(cantidad_ruedas, cantidad_puertas, Colores)
        {
            this.cantidadMarchas = cantidad_marchas;
            this.pesoCarga = peso_carga;
        }

        public override string mensaje()
        {
            string mensaje = base.mensaje();
            mensaje += $"Cantidad de marchas {cantidadMarchas}\n";
            mensaje += $"peso carga {pesoCarga}\n";

            return mensaje;
        }
    }
}