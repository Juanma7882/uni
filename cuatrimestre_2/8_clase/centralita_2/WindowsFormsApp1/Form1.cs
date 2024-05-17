using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System;
using System.Windows.Forms;
using static ClassLibrary1.centralita;
using ClassLibrary1;


namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        private Centralita c;

        public Form1()
        {
            InitializeComponent();

            c = new Centralita();

            Local l1 = new Local("Bernal", 30, "Rosario", 2.65f);
            Provincial l2 = new Provincial("Morón", Provincial.Franja.Franja_1, 21, "Bernal");
            Local l3 = new Local("Lanús", 45, "San Rafael", 1.99f);
            Provincial l4 = new Provincial(Provincial.Franja.Franja_3, l2);
            c = c + l1;
            c = c + l2;
            c = c + l3;
            c = c + l4;
        }


        private void GenrerLlamada(object sender, EventArgs e)
        {
            FrmLlamador frmLlamador = new FrmLlamador();
            //frmLlamador.ShowDialog();
            frmLlamador.Show();
            this.Hide();
        }

        
        private void button2_Click(object sender, EventArgs e)
        {
            string mensaje = $"Costo total: {c.GanaciaPorTotal}";
            FrmMostrar frmLlamador = new FrmMostrar(mensaje);
            //frmLlamador.ShowDialog();
            frmLlamador.Show();
            this.Hide();
        }


        private void button3_Click(object sender, EventArgs e)
        {
            string mensaje = $"Costo local: {c.GanaciaPorLocal}";
            FrmMostrar frmLlamador = new FrmMostrar(mensaje);
            //frmLlamador.ShowDialog();
            frmLlamador.Show();
            this.Hide();
        }


        private void button4_Click(object sender, EventArgs e)
        {
            string mensaje = $"Costo Provincial: {c.GanaciaPorProvincial}";
            FrmMostrar frmLlamador = new FrmMostrar(mensaje);
            //frmLlamador.ShowDialog();
            frmLlamador.Show();
            this.Hide();
        }


        private void Form1_Load(object sender, EventArgs e)
        {
        }


        private void button5_Click_1(object sender, EventArgs e)
        {
            this.Close();
        }

       
    }
}
