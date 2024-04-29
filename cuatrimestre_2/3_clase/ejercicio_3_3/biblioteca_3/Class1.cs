namespace biblioteca
{
    public class Estudiante
    {
        private string nombre;
        private string apellido;
        private string legajo;
        private int notaprimerparcial;
        private int notasegundoparcial;

        public Estudiante(string Nombre, string Apellido, string Legajo)
        {
            this.nombre = Nombre;
            this.apellido = Apellido;
            this.legajo = Legajo;
        }

        public void SetNotaPrimerParcial(int nota)
        {
           notaprimerparcial = nota; 

        }

        public void SetNotaSegundoParcial(int nota)
        {
            notasegundoparcial = nota; 

        }

        private float Promedio()
        {
            float promedio = (notaprimerparcial + notasegundoparcial) / 2.0f;
            return promedio;
        }

        public double calcularNotaFinal()
        {
        float nota;
           if (notaprimerparcial >= 4 && notasegundoparcial >=4)
            {
                Random random = new Random();
                nota = random.Next(6, 11);
                return nota;
            }
            nota = -1;
            return nota;
        }
        
        public string mostrar()
        {
            double nota_final = calcularNotaFinal();

            string mensaje;
            mensaje = $"Nombre   : {nombre}\n" +
                      $"apellido : {apellido}\n" +
                      $"Nota primer parcial  : {notaprimerparcial}\n" +
                      $"Nota segundo parcial : {notasegundoparcial}\n" +
                      $"Nota promedio   : {Promedio()}\n" +
                      $"Nota final: {(nota_final == -1 ? "Alumno desaprobado" : nota_final.ToString())}\n";
            return mensaje;
        }
        
    }
}
