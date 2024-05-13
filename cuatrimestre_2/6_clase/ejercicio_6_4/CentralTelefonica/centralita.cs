
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


        //public float GananciaPorLocal
        //{
        //    get
        //    {
        //        return CalcularGanancia(TipoLlamada.Local);
        //    }
        //}

        //public float GananciaPorLocal { get => CalcularGanancia(TipoLlamada.Local); }
        //public float GananciaPorLocal { get { return CalcularGanancia(TipoLlamada.Local); } }

        //public float GananciaPorLocal
        //{
        //    get
        //    {
        //        float ganancia = 0;

        //        foreach (var llamada in listaDeLLamadas)
        //        {
        //            if (llamada is Local)
        //            {
        //                //porque se llama de esta forma ?????????????
        //                Local local = (Local)llamada;
        //                ganancia += local.costollamada;
        //            }
        //        }
        //        return ganancia;
        //    }
        //}

        //public float GananciaPorProvincial
        //{
        //    get
        //    {
        //        float ganancia = 0;

        //        foreach (var llamada in listaDeLLamadas)
        //        {
        //            if (llamada is Provincial)
        //            {
        //                Provincial provincia = (Provincial)llamada;
        //                ganancia += provincia.costollamada;
        //            }
        //        }
        //        return ganancia;
        //    }
        //}



        //public float GananciaPorTotal
        //{
        //    get { return this.GananciaPorProvincial + this.GananciaPorLocal; }
        //}


        ////no pude hacer desaparecer el verde
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

        //private float CalcularGanancia(TipoLlamada tipo)
        //{
        //    //if (tipo == TipoLlamada.Local)
        //    //{
        //    //    return this.GananciaPorLocal;
        //    //}
        //    //if (tipo == TipoLlamada.Provincial)
        //    //{
        //    //    return this.GananciaPorProvincial;
        //    //}
        //    //else
        //    //{
        //    //    return this.GananciaPorTotal;
        //    //}

        //    switch (tipo)
        //    {
        //        case TipoLlamada.Local:
        //            return  this.GananciaPorLocal;
        //        case TipoLlamada.Provincial:
        //            return this.GananciaPorProvincial;
        //        default:
        //            return this.GananciaPorTotal;

        //            //cualquiera de los 2 esta bien 

        //            //case TipoLlamada.Todas:
        //            //    return this.GananciaPorTotal;
        //    }

        //}
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
                    gananciaLocal += ((Local)llamada).costollamada;
                }

                ///Si es una llamada de tipo provincial
                if (llamada is Provincial)
                {
                    ///Lo sumo a la variable GananciaProvincial
                    gananciaProvincial += ((Provincial)llamada).costollamada;
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


        public string Mostrar()
            {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine($"Razon social: {this.razonSocial}");
            sb.AppendLine($"Ganancia Total: {GanaciaPorTotal}");
            sb.AppendLine($"Ganancia Local: {GanaciaPorLocal}");
            sb.AppendLine($"Ganancia Provincial: {GanaciaPorProvincial}");

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