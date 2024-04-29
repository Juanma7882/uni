using System.Drawing;

namespace Biblioteca
{
    public class Producto
    {
        private string codigoDeBarra;
        private string marca;
        private float precio;

        public Producto(string marcaParametro, string codigoParametro, float precioParametro)
        {
            marca = marcaParametro;
            codigoDeBarra = codigoParametro;
            precio = precioParametro;
        }
        public string GetMarca()
        {
             return marca; 
        }

        public float GetPrecio()
        {
            return precio;
        }

        public string MostrarProducto(Producto P)
        {
            string mensaje = $"Marca {P.GetMarca()}\n Codigo de Barra {((string)P)} \n Precio {P.GetPrecio}";
           return mensaje;
        }

        public static explicit operator string(Producto p)
        {
            return p.codigoDeBarra;
        }

        //  operadores 
        public static bool operator ==(Producto p1, Producto p2)
        {
            if (!(p1 is null || p2 is null))
            {
                return (p1.marca) == (p2.marca) && (p1.codigoDeBarra) == (p2.codigoDeBarra);
            }
            Console.WriteLine("fue null");
            return false;
        }
        public static bool operator !=(Producto p1, Producto p2)
        {
            return !(p1 == p2);
        }

        public static bool operator ==(Producto p, string auxStr)
        {
          return p.GetMarca() == (auxStr);
        }
        public static bool operator !=(Producto p, string auxStr)
        {
            return p.GetMarca() != (auxStr);

        }


    }

}
