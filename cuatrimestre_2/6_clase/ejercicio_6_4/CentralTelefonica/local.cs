using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CentralTelefonica
{
    public class Local: Llamada
    {
        private float costo;



        public Local(string origen, float duracion, string destino, float costo)
            : base(duracion, destino, origen)
        {
            this.costo = costo;
        }

        public Local(Llamada l, float costo) : this(l.NroOrigen, l.Duracion, l.NroDestino, costo)
        {
        }


        //public Local(string Origen, float Duracion, string Destino, float Costo):base(Duracion,Destino, Origen )
        //{
        //    this.costo = Costo;
        //}
        private float CalcularCosto()
        {
            return this.costo * this.duracion; 

        }

        public override string Mostrar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine( base.Mostrar());
            sb.AppendLine($"Costo : {CalcularCosto()}");

            string resultado = sb.ToString();

            return resultado;

        }

        public float costollamada
        {
            get
            {
                return CalcularCosto(); // Retornamos el valor calculado
            }
        }

    }
}
