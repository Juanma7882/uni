using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace formas
{
    public class Rectangulo:Figura
    {
        private float alto;
        private float ancho;
        public Rectangulo(float Ancho,float Alto)
        {
            this.ancho = Ancho;
            this.alto = Alto;
        }

        public override double CalcularPerimetro()
        {
            return 2 * (ancho + alto);
        }

        public override double CalcularSuperficie()
        {
           return this.ancho * this.alto;
        }
       

        public override string Dibujar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("Tipo: Biblioteca.Rectangulo");
            sb.AppendLine("Dibujando Rectangulo...");
            sb.AppendLine($"Área : {CalcularSuperficie().ToString("0.00")}");
            sb.AppendLine($"Perímetro: {CalcularPerimetro().ToString("0.00")}");
            sb.AppendLine("");

            string resultado = sb.ToString();
            return resultado;
        }
    }
}

