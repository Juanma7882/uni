using System.Text;

namespace CentralTelefonica
{
    public  class Llamada
    {
        public enum TipoLlamada
        {
            Local,
            Provincial,
            Todas
        }


        protected float duracion;
        protected string nroDestino;
        protected string nroOrigen;

        public Llamada(float DURACION, string N_DESTINO, string N_ORIGEN)
        {
            this.duracion = DURACION;
            this.nroDestino = N_DESTINO;
            this.nroOrigen = N_ORIGEN;
        }


         public virtual string Mostrar()
        {
            StringBuilder sb = new StringBuilder();

            sb.AppendLine("Datos de la llamada ");
            sb.AppendLine($"Duracion : {duracion} ");
            sb.AppendLine($"numero de origen : {nroOrigen}");
            sb.AppendLine($"Numero de destino : {nroDestino}");

            string resultado = sb.ToString();
            return resultado;
        }


        public float Duracion
        {
            get { return duracion; }
        }

        public string NroDestino
        {
            get { return nroDestino; }
        }

        public string NroOrigen
        {
            get { return nroOrigen; }
        }


        public float OrdenarPorDuracion(Llamada llamada1 , Llamada llamada2)
        {
            List<float> numeros = new List<float> { llamada1.Duracion, llamada2.duracion };
            numeros.Sort();
            return numeros.Last();

        }
       

    }
}
