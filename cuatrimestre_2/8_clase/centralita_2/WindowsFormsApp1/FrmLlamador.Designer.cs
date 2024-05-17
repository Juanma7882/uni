namespace WindowsFormsApp1
{
    partial class FrmLlamador
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
            this.panel = new System.Windows.Forms.GroupBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.button15 = new System.Windows.Forms.Button();
            this.button14 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.cmbFranja = new System.Windows.Forms.ComboBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.panel.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel
            // 
            this.panel.Controls.Add(this.panel1);
            this.panel.Location = new System.Drawing.Point(82, 125);
            this.panel.Name = "panel";
            this.panel.Size = new System.Drawing.Size(413, 326);
            this.panel.TabIndex = 1;
            this.panel.TabStop = false;
            this.panel.Text = "Panel";
            this.panel.Enter += new System.EventHandler(this.groupBox1_Enter);
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.button15);
            this.panel1.Controls.Add(this.button14);
            this.panel1.Controls.Add(this.button13);
            this.panel1.Controls.Add(this.button12);
            this.panel1.Controls.Add(this.button11);
            this.panel1.Controls.Add(this.button10);
            this.panel1.Controls.Add(this.button9);
            this.panel1.Controls.Add(this.button8);
            this.panel1.Controls.Add(this.button7);
            this.panel1.Controls.Add(this.button6);
            this.panel1.Controls.Add(this.button5);
            this.panel1.Controls.Add(this.button4);
            this.panel1.Location = new System.Drawing.Point(52, 39);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(310, 263);
            this.panel1.TabIndex = 2;
            this.panel1.Paint += new System.Windows.Forms.PaintEventHandler(this.panel1_Paint);
            // 
            // button15
            // 
            this.button15.Location = new System.Drawing.Point(215, 205);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(75, 36);
            this.button15.TabIndex = 11;
            this.button15.Text = "#";
            this.button15.UseVisualStyleBackColor = true;
            this.button15.Click += new System.EventHandler(this.btn_numeral_numeral);
            // 
            // button14
            // 
            this.button14.Location = new System.Drawing.Point(121, 205);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(75, 36);
            this.button14.TabIndex = 10;
            this.button14.Text = "0";
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.btn_numeral_0);
            // 
            // button13
            // 
            this.button13.Location = new System.Drawing.Point(30, 205);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(75, 36);
            this.button13.TabIndex = 9;
            this.button13.Text = ".";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.btn_numeral_punto);
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(215, 149);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(75, 36);
            this.button12.TabIndex = 8;
            this.button12.Text = "9";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.btn_numeral_9);
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(121, 149);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(75, 36);
            this.button11.TabIndex = 8;
            this.button11.Text = "8";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.btn_numeral_8);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(30, 149);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(75, 36);
            this.button10.TabIndex = 6;
            this.button10.Text = "7";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.btn_numeral_7);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(215, 93);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(75, 33);
            this.button9.TabIndex = 5;
            this.button9.Text = "6";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.btn_numeral_6);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(121, 93);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(75, 33);
            this.button8.TabIndex = 4;
            this.button8.Text = "5";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.btn_numeral_5);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(30, 93);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(75, 33);
            this.button7.TabIndex = 3;
            this.button7.Text = "4";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.btn_numeral_4);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(215, 29);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(75, 33);
            this.button6.TabIndex = 2;
            this.button6.Text = "3";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.btn_numeral_3);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(121, 29);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(75, 33);
            this.button5.TabIndex = 1;
            this.button5.Text = "2";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.btn_numeral_2);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(30, 29);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 33);
            this.button4.TabIndex = 0;
            this.button4.Text = "1";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.btn_numeral_1);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(82, 48);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(835, 26);
            this.textBox1.TabIndex = 2;
            this.textBox1.Text = "Nro Destino";
            this.textBox1.TextChanged += new System.EventHandler(this.textBox_NroDestino);
            // 
            // cmbFranja
            // 
            this.cmbFranja.FormattingEnabled = true;
            this.cmbFranja.Location = new System.Drawing.Point(82, 470);
            this.cmbFranja.Name = "cmbFranja";
            this.cmbFranja.Size = new System.Drawing.Size(835, 28);
            this.cmbFranja.TabIndex = 3;
            this.cmbFranja.Text = "Franja";
            this.cmbFranja.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(701, 125);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(216, 62);
            this.button1.TabIndex = 4;
            this.button1.Text = "Llamar";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.llamar);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(701, 214);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(216, 62);
            this.button2.TabIndex = 5;
            this.button2.Text = "Limpiar";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.limpiar);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(701, 356);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(216, 62);
            this.button3.TabIndex = 6;
            this.button3.Text = "salir";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.salir);
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(701, 297);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(216, 26);
            this.textBox2.TabIndex = 7;
            this.textBox2.Text = "Nro Origen";
            this.textBox2.TextChanged += new System.EventHandler(this.textBox_NroOrigen);
            // 
            // FrmLlamador
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(982, 529);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.cmbFranja);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.panel);
            this.Name = "FrmLlamador";
            this.Text = "FrmLlamador";
            this.panel.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox panel;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.ComboBox cmbFranja;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Button button13;
    }
}