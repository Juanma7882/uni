using System.Text;

namespace CentralTelefonica
{

    public abstract class Llamada
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


        public abstract float CostoLlamada{get;} //clse añadida en la parte2

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


        public Llamada(float DURACION, string N_DESTINO, string N_ORIGEN)
        {
            this.duracion = DURACION;
            this.nroDestino = N_DESTINO;
            this.nroOrigen = N_ORIGEN;
        }

        protected virtual string Mostrar()
        {
            StringBuilder sb = new StringBuilder();

            sb.AppendLine("Datos de la llamada ");
            sb.AppendLine($"Duracion : {Duracion} ");
            sb.AppendLine($"numero de origen : {NroOrigen}");
            sb.AppendLine($"Numero de destino : {NroDestino}");

            return sb.ToString(); ;
        }

        public static bool operator !=(Llamada l1, Llamada l2)
        {
            return !(l1.Equals(l2));

        }
        public static bool operator ==(Llamada l1, Llamada l2)
        {
            return l1.Equals(l2);
        }

        public float OrdenarPorDuracion(Llamada llamada1 , Llamada llamada2)
        {
            List<float> numeros = new List<float> { llamada1.Duracion, llamada2.duracion };
            numeros.Sort();
            return numeros.Last();
        }
       
    }
}
