using System;
using System.Collections.Generic;

namespace biblioteca
{
    public class VehiculoTerrestre
    {
        public short cantidadRuedas;
        public short cantidadPuertas;
        public Colores color;

        public VehiculoTerrestre(short cantidad_ruedas , short cantidad_puertas, Colores colorPrincipal)
        {
            this.cantidadRuedas = cantidad_ruedas;
            this.cantidadPuertas = cantidad_puertas;
            this.color = colorPrincipal;
        }

        //aca preparamos un mensaje que se va ir modificando mientras va pasando por las clases
        // para poder modificarlo utilizamos el metodo virtual esto nos permite una modificasion en 
        // clases hijas de esta 

        public virtual string mensaje()
        {
            string mensaje = $"tipo de vehiculo terrestre\n";// le coloco el contrabarra n que tecnicamente es
            mensaje += $"cantidad de puertas: {cantidadPuertas}\n";// un salto de linea asi me queda mas 
            mensaje += $"cantidad de ruedas: {cantidadRuedas}\n";// prolijo
            mensaje += $" color del vehiculo: {color}\n ";
            return mensaje;
        }

        // YA que tecnicamente vamos a imprimir mensaje que mejor sea un metodo y ya arreglamos todo 
        public void imprimir()
        {
            Console.WriteLine(mensaje()); 
        }

    }

}
