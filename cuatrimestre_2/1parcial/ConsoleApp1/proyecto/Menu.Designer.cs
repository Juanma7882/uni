namespace proyecto
{
    partial class Menu
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.BtnAdmEmpleados = new System.Windows.Forms.Button();
            this.BtnAdmVehiculos = new System.Windows.Forms.Button();
            this.perfil = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.BackColor = System.Drawing.Color.Brown;
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.button1.Location = new System.Drawing.Point(0, 1);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(172, 45);
            this.button1.TabIndex = 3;
            this.button1.Text = "Cerrar sesion";
            this.button1.UseVisualStyleBackColor = false;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // BtnAdmEmpleados
            // 
            this.BtnAdmEmpleados.Image = global::proyecto.Properties.Resources.icons8_grupo_de_usuario_60;
            this.BtnAdmEmpleados.Location = new System.Drawing.Point(539, 136);
            this.BtnAdmEmpleados.Name = "BtnAdmEmpleados";
            this.BtnAdmEmpleados.Size = new System.Drawing.Size(183, 143);
            this.BtnAdmEmpleados.TabIndex = 2;
            this.BtnAdmEmpleados.Text = "Administrar empleados";
            this.BtnAdmEmpleados.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.BtnAdmEmpleados.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.BtnAdmEmpleados.UseVisualStyleBackColor = true;
            this.BtnAdmEmpleados.Click += new System.EventHandler(this.button3_Click);
            // 
            // BtnAdmVehiculos
            // 
            this.BtnAdmVehiculos.Image = global::proyecto.Properties.Resources.icons8_auto_50;
            this.BtnAdmVehiculos.Location = new System.Drawing.Point(303, 136);
            this.BtnAdmVehiculos.Name = "BtnAdmVehiculos";
            this.BtnAdmVehiculos.Size = new System.Drawing.Size(185, 143);
            this.BtnAdmVehiculos.TabIndex = 1;
            this.BtnAdmVehiculos.Text = "Administrar vehiculos";
            this.BtnAdmVehiculos.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.BtnAdmVehiculos.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.BtnAdmVehiculos.UseVisualStyleBackColor = true;
            this.BtnAdmVehiculos.Click += new System.EventHandler(this.button2_Click);
            // 
            // perfil
            // 
            this.perfil.Image = global::proyecto.Properties.Resources.icons8_usuario_60;
            this.perfil.Location = new System.Drawing.Point(70, 136);
            this.perfil.Name = "perfil";
            this.perfil.Size = new System.Drawing.Size(185, 143);
            this.perfil.TabIndex = 0;
            this.perfil.Text = "Perfil";
            this.perfil.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.perfil.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.perfil.UseVisualStyleBackColor = true;
            this.perfil.Click += new System.EventHandler(this.perfil_Click);
            // 
            // Menu
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.BtnAdmEmpleados);
            this.Controls.Add(this.BtnAdmVehiculos);
            this.Controls.Add(this.perfil);
            this.Name = "Menu";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Menu";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button perfil;
        private System.Windows.Forms.Button BtnAdmVehiculos;
        private System.Windows.Forms.Button BtnAdmEmpleados;
        private System.Windows.Forms.Button button1;
    }
}