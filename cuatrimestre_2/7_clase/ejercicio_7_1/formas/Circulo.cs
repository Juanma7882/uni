using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace formas
{
    public class Circulo : Figura
    {
        private float radio;

        public Circulo(float Radio)
        {
            this.radio = Radio;
        }

        public override double CalcularPerimetro()
        {
            return Math.PI * this.radio * 2;
        }

        public override double CalcularSuperficie()
        {
            return Math.PI + Math.Pow(this.radio, 2);
        }

        public override string Dibujar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("Tipo: Biblioteca.circulo");
            sb.AppendLine("Dibujando circulo...");
            sb.AppendLine($"Área : {CalcularSuperficie().ToString("0.00")}");
            sb.AppendLine($"Perímetro: {CalcularPerimetro().ToString("0.00")}");

            string resultado = sb.ToString();
            return resultado;
        }
    }
}
