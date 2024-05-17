using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static ClassLibrary1.centralita;
using ClassLibrary1;

namespace WindowsFormsApp1
{
    public partial class FrmMostrar : Form
    {
        public FrmMostrar(string mensajecosto)
        {
            InitializeComponent();

            richTextBox1.Text = $"{mensajecosto} ";
            richTextBox1.ReadOnly = true;

            richTextBox1.GotFocus += RichTextBox1_GotFocus;
            richTextBox1.Cursor = Cursors.Arrow;
             
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
        }

        private void regresar_Click(object sender, EventArgs e)
        {
            Application.OpenForms["Form1"].Show();
            this.Close();
        }

        private void RichTextBox1_GotFocus(object sender, EventArgs e)
        {
            this.ActiveControl = null;
        }

        private void RichTextBox1_Click(object sender, EventArgs e)
        {
            this.ActiveControl = null;
        }

        private void FrmMostrar_Load(object sender, EventArgs e)
        {

        }
    }
}
