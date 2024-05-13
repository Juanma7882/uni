
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using static CentralTelefonica.Llamada;


namespace CentralTelefonica
{

    public class Centralita 
    {
        private List<Llamada> listaDeLLamadas;
        protected string razonSocial;
        
        public List<Llamada> Llamadas
        {
            get { return listaDeLLamadas; }
        }


        public float GanaciaPorLocal
        {
            get
            {
                return CalcularGanancia(TipoLlamada.Local);
            }
        }
        public float GanaciaPorProvincial
        {
            get
            {
                return CalcularGanancia(TipoLlamada.Provincial);
            }
        }
        public float GanaciaPorTotal
        {
            get
            {
                return CalcularGanancia(TipoLlamada.Todas);
            }
        }
        
        private void AgregarLlamada(Llamada nuevaLlamada)
        {
            listaDeLLamadas.Add(nuevaLlamada);
            //Console.WriteLine(nuevaLlamada);
        }

        private float CalcularGanancia(TipoLlamada tipo)
        {
            ///Estas son variables q declaro en cero donde voy a acumular las ganancias
            float gananciaLocal = 0;
            float gananciaProvincial = 0;

            ///Recorro la lista de llamadas

            foreach (var llamada in listaDeLLamadas)
            {
                ///Si es una llamada de tipo local
                if (llamada is Local)
                {
                    ///Lo sumo a la variable GananciaLocal 
                    gananciaLocal += ((Local)llamada).CostoLlamada;
                }

                ///Si es una llamada de tipo provincial
                if (llamada is Provincial)
                {
                    ///Lo sumo a la variable GananciaProvincial
                    gananciaProvincial += ((Provincial)llamada).CostoLlamada;
                }

            }

            ///Después de que recorro la lista de llamadas uso el parámetro "tipo" para verificar el tipo de llamada
            ///Y retorno el valor que le corresponda 

            if (tipo == TipoLlamada.Local)
            {
                return gananciaLocal;
            }

            else if (tipo == TipoLlamada.Provincial)
            {
                return gananciaProvincial;
            }

            else
            {
                ///Si me pide la ganancia total retorno la suma entre las ganancias de los dos tipos de llamada
                return gananciaLocal + gananciaProvincial;
            }
        }

        public Centralita()
        {
            this.listaDeLLamadas = new List<Llamada>();
        }

        public Centralita(string nombreEmpresa) : this()
        {
            if (nombreEmpresa is null)
            {
                nombreEmpresa = "el nombre es nulo";
            }
            else
            {
                this.razonSocial = nombreEmpresa;
            }
        }

        private string Mostrar()
            {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine($"Razon social: {this.razonSocial}");
            sb.AppendLine($"Ganancia Total: {GanaciaPorTotal}");
            sb.AppendLine($"Ganancia Local: {GanaciaPorLocal}");
            sb.AppendLine($"Ganancia Provincial: {GanaciaPorProvincial}");

            foreach (var llamada in listaDeLLamadas)
            {
                sb.AppendLine($"Detalle de la llamada:");
                sb.AppendLine($"Duración: {llamada.Duracion}");
                sb.AppendLine($"Número de Destino: {llamada.NroDestino}");
                sb.AppendLine($"Número de Origen: {llamada.NroOrigen}");
            }
            //Console.WriteLine( sb.ToString() );
            return sb.ToString();
        }

        public static bool operator !=(Centralita c, Llamada llamada) 
        {
            foreach (Llamada l in c.Llamadas)
            {
                if (l == llamada)
                {
                    return !(true); 
                }
            }
            return !(false);  // Si no se encuentra la llamada, retornamos false
        }

        public static Centralita operator +(Centralita c, Llamada nuevaLlamada)
        {
            if (c != nuevaLlamada)
            {
                c.AgregarLlamada(nuevaLlamada);
                //Console.WriteLine("Llamada agregada correctamente.");
                //Console.WriteLine(nuevaLlamada);
            }
            else
            {
                //Console.WriteLine("La llamada ya existe en la lista, no se agregó.");
            }
            return c;
        }

        public static bool operator ==(Centralita c, Llamada llamada)
        {
            foreach (Llamada l in c.Llamadas)
            {
                if (l == llamada)
                {
                    return true;  // Si la llamada ya existe en la lista, retornamos true
                }
            }
            return false;  // Si no se encuentra la llamada, retornamos false
        }


        public void OrdenarLlamadas()
        {
            //SearchOption fija que no sea nullo 
            if (listaDeLLamadas is not null)
            {
                //ordenamos como lo pedia el ejeercicio
                listaDeLLamadas.Sort((llamada1, llamada2) => llamada1.Duracion.CompareTo(llamada2.Duracion));
            }
        }

        public new string ToString()
        {
            return Mostrar();
        }

    }

}