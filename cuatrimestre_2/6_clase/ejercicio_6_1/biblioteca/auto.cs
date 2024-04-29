using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace biblioteca
{
    public class Auto : VehiculoTerrestre
    {
        short cantidadMarchas; 
        int cantidadPasajeros;

        public Auto(short cantidad_ruedas, short cantidad_puertas, short cantidadMarchas, int cantidadPasajeros , Colores colores) 
            : base(cantidad_ruedas, cantidad_puertas , colores)
        {
            this.cantidadMarchas = cantidadMarchas;
            this.cantidadPasajeros = cantidadPasajeros;
        }
        public override string mensaje()
        {
            string mensaje = base.mensaje();
            mensaje += $"Cantidad de marchas {cantidadMarchas}\n";
            mensaje += $"Cantidad de Pasajeros {cantidadPasajeros}\n";

            return mensaje;
        }

    }
}
