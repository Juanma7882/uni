using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Biblioteca
{
    public class Estante
    {
        private Producto[] productos;
        private int ubicacionEstante;

        // Constructor que recibe la capacidad del estante
        public Estante(int capacidad)
        {
            productos = new Producto[capacidad]; 
         
        }


        public  Estante(int capacidad , int ubicacion):this (capacidad)
        {
            ubicacionEstante = ubicacion;
            
        }
        public Producto[] GetProductos()
        {
            return productos;
        }

        public static string MostrarEstante(Estante e)
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine($"Estante ubicacion: {e.ubicacionEstante} \n");

            for (int i = 0; i < e.productos.Length; i++)
            {
                if(!Object.ReferenceEquals(e.productos[i], null))
                {
                    // Crear una instancia de Producto
                    Producto productoActual = e.productos[i];

                    // Llamar al método MostrarProducto desde la instancia
                    sb.AppendLine(productoActual.MostrarProducto(productoActual));
                    sb.AppendLine("----------------------");
                }
            }

            return sb.ToString();
        }


        public static bool operator ==(Estante e, Producto p)
        {
            for (int i = 0; i < e.productos.Length; i++)
            {
                if (e.productos[i] == p)
                {
                    return true;
                }
            }
            return false;
        }

        public static bool operator !=(Estante e, Producto p)
        {
           return !(e == p);
        }
        public static bool operator +(Estante e, Producto p)
        {

            if (e != p)
            {
                for (int i = 0; i < e.productos.Length; i++)
                {
                    if (e.productos[i] is null)
                    {
                        e.productos[i] = p;
                        return true;

                    }
                }
            }

            return false;
        }
        public static Estante operator -(Estante e, Producto p)
        {
            for (int i = 0; i < e.productos.Length; i++)
            {
                if (e == p)
                {
                    e.productos[i] = null;
                    break;
                }
            }
            return e;

        }
    }
}
