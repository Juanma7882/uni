using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using CentralTelefonica;
namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void GenrerLlamada(object sender, EventArgs e)
        {
            //MessageBox.Show("GENERAR LLAMADA");
            FrmLlamador frmLlamador = new FrmLlamador();
            frmLlamador.Show();
            this.Hide();
        }

            //MessageBox.Show("2");
        private void button2_Click(object sender, EventArgs e)
        {

            //richTextBox1.SelectionFont = new Font(richTextBox1.Font, FontStyle.Bold);
            //richTextBox1.SelectionColor = Color.Blue;
            //richTextBox1.AppendText("Texto en negrita y azul\n");

            //richTextBox1.SelectionFont = new Font(richTextBox1.Font, FontStyle.Bold | FontStyle.Italic);
            //richTextBox1.SelectionColor = Color.Red;
            //richTextBox1.AppendText("Texto en negrita cursiva y rojo\n");

            //richTextBox1.SelectionFont = new Font(richTextBox1.Font, FontStyle.Regular);
            //richTextBox1.SelectionColor = Color.Green;
            //richTextBox1.AppendText("Texto normal y verde\n");

            //// Agregar un salto de línea al final
            //richTextBox1.AppendText("\n");


        }
        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("3");
            Provincial l4 = new Provincial(Provincial.Franja.Franja_3, l2);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            MessageBox.Show("4");

        }

        private void button5_Click(object sender, EventArgs e)
        {
            MessageBox.Show("5");
            

        }

        private void button5_Click_1(object sender, EventArgs e)
        {
            MessageBox.Show("salir");
        }
    }
}
