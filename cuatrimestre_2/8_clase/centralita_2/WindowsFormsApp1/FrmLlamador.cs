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
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using System.Text.RegularExpressions;



namespace WindowsFormsApp1
{
    public partial class FrmLlamador : Form
    {
        bool bandera_destino = false;
        bool bandera_origen = false;

        public FrmLlamador()
        {
            InitializeComponent();

            cmbFranja.DataSource = Enum.GetValues(typeof(Llamada.TipoLlamada));
            // Asignar el evento SelectedIndexChanged
            cmbFranja.SelectedIndexChanged += comboBox1_SelectedIndexChanged;
        }


        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }


        private void panel1_Paint(object sender, EventArgs e)
        {

        }


        private void btn_numeral_1(object sender, EventArgs e)
        {

            if (bandera_destino)
            {
                if (textBox1.Text == "Nro Destino")
                {
                    textBox1.Text = "1";
                }
                else
                {
                    textBox1.Text += "1";
                }
            }
            if (bandera_origen)
            {
                if (textBox2.Text == "Nro Origen")
                {
                    textBox2.Text = "1";
                }
                else
                {
                    textBox2.Text += "1";
                }
            }

        }


        private void btn_numeral_2(object sender, EventArgs e)
        {
            textBox1.Text += 2;
        }


        private void btn_numeral_3(object sender, EventArgs e)
        {
            textBox1.Text += 3;
        }


        private void btn_numeral_4(object sender, EventArgs e)
        {
            textBox1.Text += 4;
        }


        private void btn_numeral_5(object sender, EventArgs e)
        {
            textBox1.Text += 5;
        }


        private void btn_numeral_6(object sender, EventArgs e)
        {
            textBox1.Text += 6;
        }


        private void btn_numeral_7(object sender, EventArgs e)
        {
            textBox1.Text += 7;
        }


        private void btn_numeral_8(object sender, EventArgs e)
        {
            textBox1.Text += 8;
        }


        private void btn_numeral_9(object sender, EventArgs e)
        {
            textBox1.Text += 9;
        }


        private void btn_numeral_punto(object sender, EventArgs e)
        {
            textBox1.Text += ".";
        }


        private void btn_numeral_0(object sender, EventArgs e)
        {
            textBox1.Text += 0;
        }


        private void btn_numeral_numeral(object sender, EventArgs e)
        {
            textBox1.Text += "#";
        }

        private bool validarnumeral(string validar)
        {
            string pattern = @"^#";
            Regex regex = new Regex(pattern);
            if (regex.IsMatch(validar))
            {
                return true;
            }
            return false;

        }


        private void textBox_NroDestino(object sender, EventArgs e)
        {

            bandera_destino = true;
            bandera_origen = false;
            
            if (validarnumeral(textBox1.Text))
            {
                cmbFranja.Enabled = false;
            }
            else
            {
                cmbFranja.Enabled = true;
            }
        }


        private void textBox_NroOrigen(object sender, EventArgs e)
        {
            if (textBox2.Focused)
            {
                bandera_destino = true;
                bandera_origen = false;
            }
            else
            {
            }
        }

        private float NumeroRandom(float rango1, float rango2)
        {
            Random r = new Random();
            double randomValue = r.NextDouble(); 

            float result = (float)(rango1 + randomValue * (rango2 - rango1));
            return result;
        }


        private void llamar(object sender, EventArgs e)
        {

            if (validarnumeral(textBox1.Text))
            {
                Provincial llamada2 = new Provincial($"{textBox1}", Provincial.Franja.Franja_1, NumeroRandom(1,50), $"{textBox2}");
                string mensaje = $"costo llamada provincial : {llamada2.CostoLlamada}";
                FrmMostrar frmLlamador = new FrmMostrar(mensaje);
                frmLlamador.Show();
                this.Hide();

            }
            else
            {
                if (Enum.TryParse(cmbFranja.SelectedValue.ToString(), out Llamada.TipoLlamada tipoLlamada))
                {
                    switch (tipoLlamada)
                    {
                        case Llamada.TipoLlamada.Local:
                            Local l1 = new Local($"{textBox1}", NumeroRandom(1, 50), $"{textBox2}", NumeroRandom(05 , 06));
                            string mensaje1 = $"costo llamada local : {l1.CostoLlamada}";
                            FrmMostrar frmLlamador1 = new FrmMostrar(mensaje1);
                            frmLlamador1.Show();
                            this.Hide();
                            break;

                        case Llamada.TipoLlamada.Provincial:
                            Provincial llamada2 = new Provincial($"{textBox1}", Provincial.Franja.Franja_1, NumeroRandom(1, 50), $"{textBox2}");
                            string mensaje = $"costo llamada provincial : {llamada2.CostoLlamada}";
                            FrmMostrar frmLlamador = new FrmMostrar(mensaje);
                            frmLlamador.Show();
                            this.Hide();
                            break;
                        default:
                            Local l3 = new Local($"{textBox1}", NumeroRandom(1, 50), $"{textBox2}", NumeroRandom(05, 06));
                            Provincial llamada3 = new Provincial($"{textBox1}", Provincial.Franja.Franja_1, NumeroRandom(1, 50), $"{textBox2}");
                            float costoTotal = l3.CostoLlamada + llamada3.CostoLlamada;
                            string mensaje3 = $"costo llamada total : {costoTotal}";
                            FrmMostrar frmLlamador3 = new FrmMostrar(mensaje3);
                            frmLlamador3.Show();
                            this.Hide();
                            break;
                    }
                }
            }
             
        }


        private void limpiar(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
        }
    
        private void salir(object sender, EventArgs e)
        {
            //llamda
            //InitializeComponent();
            //Environment.Exit(0);
            //form1.show();

            //Form1 form1 = new Form1();
            //form1.Show();

            Application.OpenForms["Form1"].Show();

            //this.Hide();
            this.Close();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
           
            
        }
    }
}
