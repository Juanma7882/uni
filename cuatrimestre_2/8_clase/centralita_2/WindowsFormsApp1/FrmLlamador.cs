using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class FrmLlamador : Form
    {
        bool bandera_destino = false;
        bool bandera_origen = false;

        public FrmLlamador()
        {
            InitializeComponent();
        }


        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }
        private void panel1_Paint(object sender, EventArgs e)
        {

        }

        private void btn_numeral_1(object sender, EventArgs e)
        {
            if (bandera_destino )
            {
                if (textBox1.Text == "Nro Destino")
                {
                    textBox1.Text = "";  
                }
                textBox1.Text += 1;  
            }
            else if (bandera_origen)
            {
                if (textBox2.Text == "Nro Origen")
                {
                    textBox2.Text = "";
                }
                textBox2.Text += 1;
            }

        }

        private void btn_numeral_2(object sender, EventArgs e)
        {
            //textBox1.Text += 2;
        }

        private void btn_numeral_3(object sender, EventArgs e)
        {
            //textBox1.Text += 3;

        }

        private void btn_numeral_4(object sender, EventArgs e)
        {
            //textBox1.Text += 4;
        }

        private void btn_numeral_5(object sender, EventArgs e)
        {
            //textBox1.Text += 5;

        }

        private void btn_numeral_6(object sender, EventArgs e)
        {
            //textBox1.Text += 6;

        }
        private void btn_numeral_7(object sender, EventArgs e)
        {
            //textBox1.Text += 7;

        }

        private void btn_numeral_8(object sender, EventArgs e)
        {
            //textBox1.Text += 8;

        }

        private void btn_numeral_9(object sender, EventArgs e)
        {
            //textBox1.Text += 9;

        }

        private void btn_numeral_punto(object sender, EventArgs e)
        {
            //textBox1.Text += ".";

        }

        private void btn_numeral_0(object sender, EventArgs e)
        {
            //textBox1.Text += 0;
        }

        private void btn_numeral_numeral(object sender, EventArgs e)
        {
            //textBox1.Text += "#";
        }

        private void textBox_NroDestino(object sender, EventArgs e)
        {
            textBox1.Text = "15";
            bandera_destino = true;
            bandera_origen = false;
        }

        private void textBox_NroOrigen(object sender, EventArgs e)
        {
            textBox2.Text = "6";
            bandera_origen = true;
            bandera_destino = false;

        }

        private void llamar(object sender, EventArgs e)
        {

        }
        private void limpiar(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";


        }

        private void salir(object sender, EventArgs e)
        {

        }

       
    }
}
