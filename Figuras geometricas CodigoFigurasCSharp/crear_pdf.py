from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        # Nombre y fecha en el encabezado
        self.set_font("Arial", size=10)
        self.cell(0, 10, "Nombre: Jonathan Félix", ln=1)
        self.cell(0, 10, "Fecha: " + datetime.today().strftime('%d/%m/%Y'), ln=1)
        self.cell(0, 10, "Página: " + str(self.page_no()), ln=1)
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, title, ln=1)
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Courier", '', 10)
        self.multi_cell(0, 5, body)
        self.ln()

# Código C# con comentarios
codigo = '''
// Clase para representar un Círculo
public class Circulo
{
    private double radio;

    // Constructor que recibe el radio
    public Circulo(double radio)
    {
        this.radio = radio;
    }

    // CalcularArea es una función que devuelve un valor double, se utiliza para calcular el área de un círculo
    public double CalcularArea()
    {
        return Math.PI * radio * radio;
    }

    // CalcularPerimetro devuelve el perímetro (circunferencia) del círculo
    public double CalcularPerimetro()
    {
        return 2 * Math.PI * radio;
    }
}

// Clase para representar un Rectángulo
public class Rectangulo
{
    private double largo;
    private double ancho;

    // Constructor que recibe el largo y el ancho
    public Rectangulo(double largo, double ancho)
    {
        this.largo = largo;
        this.ancho = ancho;
    }

    // CalcularArea calcula el área multiplicando largo por ancho
    public double CalcularArea()
    {
        return largo * ancho;
    }

    // CalcularPerimetro devuelve la suma de todos los lados
    public double CalcularPerimetro()
    {
        return 2 * (largo + ancho);
    }
}
'''

# Crear el PDF
pdf = PDF()
pdf.add_page()
pdf.chapter_title("Código en C# - Clases para Figuras Geométricas")
pdf.chapter_body(codigo)
pdf.output("codigo_figuras.pdf")
