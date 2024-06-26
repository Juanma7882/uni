﻿//using System;
//using System.Collections.Generic;
//using System.ComponentModel;
//using System.Data;
//using System.Drawing;
//using System.IO;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;
//using System.Windows.Forms;
//using System.Xml.Serialization;
//using static System.Windows.Forms.VisualStyles.VisualStyleElement;
//using static System.Windows.Forms.VisualStyles.VisualStyleElement.ToolBar;


//namespace WindowsFormsApp1
//{
//    public partial class FrmListaSuper : Form
//    {
//        private static string rutaArchivo;
//        private List<string> listaSupermercado;



//        static FrmListaSuper()
//        {
//            //string rutaApplicationData = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
//            const string nombreArchivo = "archivosuper.xml";
//            //const string nombreArchivo = "archivosuper.json";
//            string rutaApplicationData = "..";



//            rutaArchivo = Path.Combine(rutaApplicationData, nombreArchivo);
//        }


//        public FrmListaSuper()
//        {
//            InitializeComponent();
//            listaSupermercado = new List<string>();
//        }

//        private void FrmListaSuper_Load(object sender, EventArgs e)
//        {
//            ConfigurarTooltips();
//            CargarListaAlmacenada();
//            RefrescarLista();
//        }


//        private void ConfigurarTooltips()
//        {
//            System.Windows.Forms.ToolTip toolTipAgregar = new System.Windows.Forms.ToolTip();
//            toolTipAgregar.SetToolTip(btnAgregar, "Agregar");

//            System.Windows.Forms.ToolTip toolTipEliminar = new System.Windows.Forms.ToolTip();
//            toolTipEliminar.SetToolTip(btnEliminar, "Eliminar");

//            System.Windows.Forms.ToolTip toolTipModificar = new System.Windows.Forms.ToolTip();
//            toolTipModificar.SetToolTip(btnModificar, "Modificar");
//        }

//        private void RefrescarLista()
//        {
//            lstObjetos.DataSource = null;
//            lstObjetos.DataSource = listaSupermercado;
//        }


//        private void CargarListaAlmacenada()
//        {
//            if (File.Exists(rutaArchivo))
//            {
//                using (StreamReader streamReader = new StreamReader(rutaArchivo))
//                {
//                    try
//                    {
//                        XmlSerializer xmlSerializer = new XmlSerializer(listaSupermercado.GetType());
//                        listaSupermercado = xmlSerializer.Deserialize(streamReader) as List<string>;
//                    }
//                    catch (Exception ex)
//                    {
//                        MostrarMensajeDeError(ex);
//                    }
//                }
//            }
//        }


//        private void btnAgregar_Click(object sender, EventArgs e)
//        {
//            AgregarElemento();
//        }

//        private void btnEliminar_Click(object sender, EventArgs e)
//        {
//            EliminarElemento();
//        }

//        private void btnModificar_Click(object sender, EventArgs e)
//        {
//            ModificarElemento();
//        }

//        private void lstObjetos_SelectedIndexChanged(object sender, EventArgs e)
//        {

//        }
//        private void lstObjetos_KeyPress(object sender, KeyPressEventArgs e)
//        {
//            if (e.KeyChar == '+')
//            {
//                AgregarElemento();
//            }
//            else if (e.KeyChar == '-')
//            {
//                EliminarElemento();
//            }
//            else if (e.KeyChar == 'M' || e.KeyChar == 'm')
//            {
//                ModificarElemento();
//            }
//        }

//        private void AgregarElemento()
//        {
//            FrmAltaModificacion frmAltaModificacion = new FrmAltaModificacion("Agregar objeto", string.Empty, "Agregar");
//            frmAltaModificacion.ShowDialog();

//            if (frmAltaModificacion.DialogResult == DialogResult.OK)
//            {
//                listaSupermercado.Add(frmAltaModificacion.Objeto);
//                AlmacenarCambios();
//                RefrescarLista();
//            }
//        }


//        private void ModificarElemento()
//        {
//            string objetoSeleccionado = lstObjetos.SelectedItem as string;

//            if (objetoSeleccionado != null)
//            {
//                FrmAltaModificacion frmAltaModificacion = new FrmAltaModificacion("Modificar objeto", objetoSeleccionado, "Agregar");
//                frmAltaModificacion.ShowDialog();

//                if (frmAltaModificacion.DialogResult == DialogResult.OK)
//                {
//                    int indice = listaSupermercado.IndexOf(objetoSeleccionado);
//                    listaSupermercado[indice] = frmAltaModificacion.Objeto;
//                    AlmacenarCambios();
//                    RefrescarLista();
//                }
//            }
//            else
//            {
//                MessageBox.Show("Debe seleccionar un elemento de la lista.", "Información", MessageBoxButtons.OK, MessageBoxIcon.Information);
//            }
//        }


//        private void EliminarElemento()
//        {
//            string objetoSeleccionado = lstObjetos.SelectedItem as string;

//            if (objetoSeleccionado != null)
//            {
//                listaSupermercado.Remove(objetoSeleccionado);
//                AlmacenarCambios();
//                RefrescarLista();
//            }
//            else
//            {
//                MessageBox.Show("Debe seleccionar un elemento de la lista.", "Información", MessageBoxButtons.OK, MessageBoxIcon.Information);
//            }
//        }

//        private void AlmacenarCambios()
//        {
//            using (StreamWriter streamWriter = new StreamWriter(rutaArchivo))
//            {
//                try
//                {
//                    XmlSerializer xmlSerializer = new XmlSerializer(listaSupermercado.GetType());
//                    xmlSerializer.Serialize(streamWriter, listaSupermercado);
//                }
//                catch (Exception ex)
//                {
//                    MostrarMensajeDeError(ex);
//                }
//            }
//        }

//        private void MostrarMensajeDeError(Exception ex)
//        {
//            StringBuilder stringBuilder = new StringBuilder();
//            stringBuilder.AppendLine(ex.Message);
//            stringBuilder.AppendLine();
//            stringBuilder.AppendLine(ex.StackTrace);

//            MessageBox.Show(stringBuilder.ToString(), "ERROR", MessageBoxButtons.OK, MessageBoxIcon.Error);
//        }


//    }
//}




using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class FrmListaSuper : Form
    {
        private static string rutaArchivo;
        private List<string> listaSupermercado;



        static FrmListaSuper()
        {
            const string nombreArchivo = "archivosuper.json";
            string rutaApplicationData = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            rutaArchivo = Path.Combine(rutaApplicationData, nombreArchivo);
        }


        public FrmListaSuper()
        {
            InitializeComponent();
            listaSupermercado = new List<string>();
        }

        private void FrmListaSuper_Load(object sender, EventArgs e)
        {

            CargarListaAlmacenada();
            RefrescarLista();

        }




        private void RefrescarLista()
        {
            lstObjetos.DataSource = null;
            lstObjetos.DataSource = listaSupermercado;
        }


        private void CargarListaAlmacenada()
        {
            if (File.Exists(rutaArchivo))
            {

                try
                {
                    string json = File.ReadAllText(rutaArchivo);
                    listaSupermercado = JsonConvert.DeserializeObject<List<string>>(json);
                }
                catch (Exception ex)
                {
                    MostrarMensajeDeError(ex);
                }
            }

        }


        private void btnAgregar_Click(object sender, EventArgs e)
        {
            AgregarElemento();
        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {
            EliminarElemento();
        }

        private void btnModificar_Click(object sender, EventArgs e)
        {
            ModificarElemento();
        }

        private void lstObjetos_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == '+')
            {
                AgregarElemento();
            }
            else if (e.KeyChar == '-')
            {
                EliminarElemento();
            }
            else if (e.KeyChar == 'M' || e.KeyChar == 'm')
            {
                ModificarElemento();
            }
        }

        private void AgregarElemento()
        {
            FrmAltaModificacion frmAltaModificacion = new FrmAltaModificacion("Agregar objeto", string.Empty, "Agregar");
            frmAltaModificacion.ShowDialog();

            if (frmAltaModificacion.DialogResult == DialogResult.OK)
            {
                listaSupermercado.Add(frmAltaModificacion.Objeto);
                AlmacenarCambios();
                RefrescarLista();
            }
        }


        private void ModificarElemento()
        {
            string objetoSeleccionado = lstObjetos.SelectedItem as string;

            if (objetoSeleccionado != null)
            {
                FrmAltaModificacion frmAltaModificacion = new FrmAltaModificacion("Modificar objeto", objetoSeleccionado, "Agregar");
                frmAltaModificacion.ShowDialog();

                if (frmAltaModificacion.DialogResult == DialogResult.OK)
                {
                    int indice = listaSupermercado.IndexOf(objetoSeleccionado);
                    listaSupermercado[indice] = frmAltaModificacion.Objeto;
                    AlmacenarCambios();
                    RefrescarLista();
                }
            }
            else
            {
                MessageBox.Show("Debe seleccionar un elemento de la lista.", "Información", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }


        private void EliminarElemento()
        {
            string objetoSeleccionado = lstObjetos.SelectedItem as string;

            if (objetoSeleccionado != null)
            {
                listaSupermercado.Remove(objetoSeleccionado);
                AlmacenarCambios();
                RefrescarLista();
            }
            else
            {
                MessageBox.Show("Debe seleccionar un elemento de la lista.", "Información", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void AlmacenarCambios()

        {
            try
            {
                string json = JsonConvert.SerializeObject(listaSupermercado);
                File.WriteAllText(rutaArchivo, json);
            }
            catch (Exception ex)
            {
                MostrarMensajeDeError(ex);
            }

        }

        private void MostrarMensajeDeError(Exception ex)
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.AppendLine(ex.Message);
            stringBuilder.AppendLine();
            stringBuilder.AppendLine(ex.StackTrace);

            MessageBox.Show(stringBuilder.ToString(), "ERROR", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }



}

