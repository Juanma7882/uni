using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CentralTelefonica

{
    public class Provincial : Llamada
    {
        protected Franja franjaHoraria;
        public enum Franja
        {
            Franja_1 = 99,
            Franja_2 = 125,
            Franja_3 = 66
        }

        //public Franja franjaHoraria;
        //public Provincial(Franja miFranja, Llamada llamada) : base(0, "", "")
        //{
        //    this.FranjaHoraria = miFranja;
        //}

        public Provincial(Franja miFranja, Llamada llamada)
            : this(llamada.NroOrigen, miFranja, llamada.Duracion, llamada.NroDestino)
        {
        }

        public Provincial(string origen, Franja miFranja, float duracion, string destino) : base(duracion, destino, origen)
        {
            this.franjaHoraria = miFranja;
        }

        private float CalcularCosto()
        {
            float precio;
            switch (this.franjaHoraria)
            {
                case Franja.Franja_1:
                    precio = 0.99f;
                    break;
                case Franja.Franja_2:
                    precio = 1.25f;
                    break;
                case Franja.Franja_3:
                    precio = 0.66f;
                    break;
                default:
                    throw new InvalidOperationException("Franja horaria no válida");
            }

            float costo = precio * base.duracion;
            return costo;
        }

        public float costollamada
        {
            get
            {
                return CalcularCosto(); // Retornamos el valor calculado
            }
        }

        public override string Mostrar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine(base.Mostrar());
            sb.AppendLine($"Costo : {costollamada}");
            sb.AppendLine($"franja Horaria : {franjaHoraria}");


            string resultado = sb.ToString();

            return resultado;

        }


    }

}
