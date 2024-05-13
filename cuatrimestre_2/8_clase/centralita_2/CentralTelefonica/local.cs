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

        //public float costollamada
        //{
        //    get
        //    {
        //        return CalcularCosto(); // Retornamos el valor calculado
        //    }
        //}
        public override float CostoLlamada
        {
            get
            {
                return CalcularCosto(); 
            }
        }

        private float CalcularCosto()
        {
            return this.costo * this.duracion; 
        }

        public override bool Equals(object obj)
        {
            if (obj.GetType() == this.GetType())
            {
                return true;
            }
            else
            {
                return false;
            }
            //if (obj == null || GetType() != obj.GetType())
            //{
            //    return false;
            //}

            //Local otraLocal = (Local)obj;
            //return this.costo == otraLocal.costo &&
            //       base.Equals(obj); // Llama a la implementación de Equals de la clase base si es necesario

        }


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

        protected override string Mostrar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine( base.Mostrar());
            sb.AppendLine($"Costo : {CalcularCosto()}");
            sb.AppendLine($"Costo llamada : {CostoLlamada}");
            //Console.WriteLine("estamos en local");
            return sb.ToString(); ;

        }

        public override string ToString()
        {
            return Mostrar();
        }
      

    }
}
