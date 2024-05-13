using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace formas
{
    public class Cuadrado:Rectangulo
    {
        private float LongitudLado;
        public Cuadrado( float longitudLado) :base (longitudLado, longitudLado)
        {
            this.LongitudLado = longitudLado;

        }

        public override double CalcularPerimetro()
        {
            return  this.LongitudLado * 4;
        }

        public override double CalcularSuperficie()
        {
            return LongitudLado * 2;
        }

        public override string Dibujar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("Tipo: Biblioteca.Circulo");
            sb.AppendLine("Dibujando Círculo...");
            sb.AppendLine($"Área : {CalcularSuperficie().ToString("0.00")}");
            sb.AppendLine($"Perímetro: {CalcularPerimetro().ToString("0.00")}");
            sb.AppendLine("");

            string resultado = sb.ToString();
            return resultado;

        }
    }
}

