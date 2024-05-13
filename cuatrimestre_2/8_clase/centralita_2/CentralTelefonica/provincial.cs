using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CentralTelefonica

{
    //enum  
   
    public class Provincial : Llamada
    {
        public enum Franja
        {
            Franja_1 = 99,
            Franja_2 = 125,
            Franja_3 = 66
        }

        protected Franja franjaHoraria;


        //properties  
        public override float CostoLlamada
        {
            get
            {
                return CalcularCosto();
            }
        }

        //Methods 

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

        public bool Equals(object obj)
        {
            if (obj.GetType() == this.GetType())
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        protected override string Mostrar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine(base.Mostrar());
            sb.AppendLine($"Costo llamada: {CostoLlamada}");
            sb.AppendLine($"franja Horaria : {franjaHoraria}");
            //Console.WriteLine("estamos en provincial");
            return sb.ToString(); ;
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
            
        public override string ToString()
        {
            return Mostrar();
        }    

    }

}
