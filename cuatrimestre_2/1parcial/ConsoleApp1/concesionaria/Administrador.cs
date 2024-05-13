using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace concesionaria
{
    public class Administrador:Persona
    {
        public Administrador(string NOMBRE, string APELLIDO, int DNI, string USUARIO, string CONTRASENA):base(NOMBRE,APELLIDO,DNI,USUARIO,CONTRASENA)
        {
        
        }

        protected override string Mostrar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine(base.Mostrar());
            sb.AppendLine($"colocar texto a la clase admi");
            return sb.ToString(); ;

        }

        public override string ToString()
        {
            return Mostrar();
        }

    }
}
