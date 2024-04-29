using System;
using System.Collections.Generic;
using System.Linq;
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

        public float GananciaPorLocal
        {
            get
            {
                float ganancia = 0;

                foreach (var llamada in listaDeLLamadas)
                {
                    if (llamada is Local)
                    {
                        //porque se llama de esta forma ?????????????
                        Local local = (Local)llamada;
                        ganancia += local.costollamada;
                    }
                }
                return ganancia;
            }
        }

        public float GananciaPorProvincial
        {
            get
            {
                float ganancia = 0;

                foreach (var llamada in listaDeLLamadas)
                {
                    if (llamada is Provincial)
                    {
                        Provincial provincia = (Provincial)llamada;
                        ganancia += provincia.costollamada;
                    }
                }
                return ganancia;
            }
        }

        public float GananciaPorTotal
        {
            get { return this.GananciaPorProvincial + this.GananciaPorLocal; }
        }


        //no pude hacer desaparecer el verde
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
            
            this.razonSocial = nombreEmpresa;
        }

        private float CalcularGanancia(TipoLlamada tipo)
        {
            //if (tipo == TipoLlamada.Local)
            //{
            //    return this.GananciaPorLocal;
            //}
            //if (tipo == TipoLlamada.Provincial)
            //{
            //    return this.GananciaPorProvincial;
            //}
            //else
            //{
            //    return this.GananciaPorTotal;
            //}

            switch (tipo) 
            {
                case TipoLlamada.Local:
                    return this.GananciaPorLocal;
                case TipoLlamada.Provincial:
                    return this.GananciaPorProvincial;
                default:
                    return this.GananciaPorTotal;

                //cualquiera de los 2 esta bien 

                //case TipoLlamada.Todas:
                //    return this.GananciaPorTotal;


            }


        }

        public string Mostrar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine($"Razon social: {this.razonSocial}");
            sb.AppendLine($"Ganancia Total: {this.GananciaPorTotal}");
            sb.AppendLine($"Ganancia Local: {this.GananciaPorLocal}");
            sb.AppendLine($"Ganancia Provincial: {this.GananciaPorProvincial}");

            foreach (var llamada in listaDeLLamadas)
            {
                sb.AppendLine($"Ganancia Detalle llamadas: {llamada.Duracion}");
                sb.AppendLine($"Ganancia Detalle llamadas: {llamada.NroDestino}");
                sb.AppendLine($"Ganancia Detalle llamadas: {llamada.NroOrigen}");
            }
            return sb.ToString();
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
    }
}
