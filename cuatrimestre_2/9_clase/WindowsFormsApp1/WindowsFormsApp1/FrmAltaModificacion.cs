using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WindowsFormsApp1
{
    public partial class FrmAltaModificacion : Form
    {
        public FrmAltaModificacion(string titulo, string contenidoTextBox, string textoBotonConfirmar)
        {
            InitializeComponent();
            Text = titulo;
            txtObjeto.Text = contenidoTextBox;
            btnConfirmar.Text = textoBotonConfirmar;
        }

        public string Objeto
        {
            get
            {
                return txtObjeto.Text;
            }
        }


        private void Confirmar()
        {
            if (string.IsNullOrWhiteSpace(txtObjeto.Text))
            {
                MessageBox.Show("El texto no puede estar vacío", "Validación", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                DialogResult = DialogResult.OK;
                Close();
            }
        }

        private void Cancelar()
        {
            DialogResult = DialogResult.Cancel;
            Close();
        }

        private void txtObjeto_KeyPress(object sender, KeyPressEventArgs e)
        {
            //if (e.KeyChar == (char)Keys.Enter)
            if (e.KeyChar == (char)13)
            {
                Confirmar();
            }
            else if (e.KeyChar == (char)Keys.Escape)
            {
                Cancelar();
            }
        }


        private void btnConfirmar_Click(object sender, EventArgs e)
        {
            Confirmar();
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            Cancelar();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (txtObjeto.Text.Length > 5)
            {
                txtObjeto.Text = txtObjeto.Text.Substring(0, 5);
                txtObjeto.SelectionStart = txtObjeto.Text.Length;
            }
        }


    }
}
