using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace concesionaria
{
    public class Persona
    {
        private string Nombre;
        private string Apellido;
        private int Dni;
        private string Usuario;
        private string Contrasena;

        public Persona(string NOMBRE, string APELLIDO, int DNI, string USUARIO, string CONTRASENA)
        {
            this.Nombre = NOMBRE;
            this.Apellido = APELLIDO;
            this.Dni = DNI;
            this.Usuario = USUARIO;
            this.Contrasena = CONTRASENA;
        }

        protected virtual string Mostrar()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine($" Apellido: {Usuario} \n");
            sb.AppendLine($" Nombre: {Nombre} \n");
            sb.AppendLine($" Apellido: {Apellido} \n");
            sb.AppendLine($" Dni: {Dni} \n");
            return sb.ToString(); ;
        }

        public override string ToString()
        {
            return Mostrar();
        }


    }
}
