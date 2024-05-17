namespace proyecto
{
    partial class Login
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.iniciar = new System.Windows.Forms.Button();
            this.title = new System.Windows.Forms.Label();
            this.usuario = new System.Windows.Forms.Label();
            this.contrasena = new System.Windows.Forms.Label();
            this.cerrarPrograma = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(175, 139);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(397, 26);
            this.textBox1.TabIndex = 0;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(175, 233);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(397, 26);
            this.textBox2.TabIndex = 1;
            // 
            // iniciar
            // 
            this.iniciar.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.iniciar.Location = new System.Drawing.Point(291, 290);
            this.iniciar.Name = "iniciar";
            this.iniciar.Size = new System.Drawing.Size(125, 51);
            this.iniciar.TabIndex = 2;
            this.iniciar.Text = "INICIAR";
            this.iniciar.UseVisualStyleBackColor = true;
            this.iniciar.Click += new System.EventHandler(this.iniciar_Click);
            // 
            // title
            // 
            this.title.AutoSize = true;
            this.title.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.title.Location = new System.Drawing.Point(265, 35);
            this.title.Name = "title";
            this.title.Size = new System.Drawing.Size(226, 40);
            this.title.TabIndex = 3;
            this.title.Text = "Iniciar sesion";
            this.title.Click += new System.EventHandler(this.label1_Click);
            // 
            // usuario
            // 
            this.usuario.AutoSize = true;
            this.usuario.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.usuario.Location = new System.Drawing.Point(170, 94);
            this.usuario.Name = "usuario";
            this.usuario.Size = new System.Drawing.Size(220, 29);
            this.usuario.TabIndex = 4;
            this.usuario.Text = "Nombre de usuario";
            this.usuario.Click += new System.EventHandler(this.label1_Click_1);
            // 
            // contrasena
            // 
            this.contrasena.AutoSize = true;
            this.contrasena.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.contrasena.Location = new System.Drawing.Point(170, 191);
            this.contrasena.Name = "contrasena";
            this.contrasena.Size = new System.Drawing.Size(136, 29);
            this.contrasena.TabIndex = 5;
            this.contrasena.Text = "Contraseña";
            // 
            // cerrarPrograma
            // 
            this.cerrarPrograma.BackColor = System.Drawing.Color.Brown;
            this.cerrarPrograma.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.cerrarPrograma.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.cerrarPrograma.Location = new System.Drawing.Point(2, -2);
            this.cerrarPrograma.Name = "cerrarPrograma";
            this.cerrarPrograma.Size = new System.Drawing.Size(172, 45);
            this.cerrarPrograma.TabIndex = 6;
            this.cerrarPrograma.Text = "Cerrar Programa";
            this.cerrarPrograma.UseVisualStyleBackColor = false;
            this.cerrarPrograma.Click += new System.EventHandler(this.cerrarPrograma_Click);
            // 
            // Login
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.cerrarPrograma);
            this.Controls.Add(this.contrasena);
            this.Controls.Add(this.usuario);
            this.Controls.Add(this.title);
            this.Controls.Add(this.iniciar);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Name = "Login";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button iniciar;
        private System.Windows.Forms.Label title;
        private System.Windows.Forms.Label usuario;
        private System.Windows.Forms.Label contrasena;
        private System.Windows.Forms.Button cerrarPrograma;
    }
}

