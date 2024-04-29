namespace biblioteca_4_1
{
    public class Sumador
    {
        private int cantidad_sumas;

        public Sumador()
        {
            this.cantidad_sumas = 0;
        }


        public Sumador(int cantidad_sumas)
        {
            this.cantidad_sumas = cantidad_sumas;
        }
        
        public static explicit operator int(Sumador s)
        {
            return s.cantidad_sumas;
        }

        public static long operator +(Sumador s1 , Sumador s2)
        {
            return s1.cantidad_sumas + s2.cantidad_sumas;
        }

        public static bool operator | (Sumador s1, Sumador s2)
        {
            bool result = false;
            if (s1.cantidad_sumas == s2.cantidad_sumas)
            {
                result = true;
            }
            return result;
        }
        public string sumar(string a , string b)
        {
            this.cantidad_sumas++;
            return a + b;
        }

        public long sumar(long a, long b)
        {
            this.cantidad_sumas++;
            return a + b;
        }


       

    }
}
