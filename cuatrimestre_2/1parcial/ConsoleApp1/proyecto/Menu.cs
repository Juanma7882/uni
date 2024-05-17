using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace proyecto
{
    public partial class Menu : Form
    {
        public Menu()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void perfil_Click(object sender, EventArgs e)
        {
            Login login = new Login();
            login.ShowDialog();
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Login login = new Login();
            login.ShowDialog();
            this.Close();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            admEmpleados admEmpleados = new admEmpleados();
            admEmpleados.ShowDialog();
            this.Close();
        }
    }
}
