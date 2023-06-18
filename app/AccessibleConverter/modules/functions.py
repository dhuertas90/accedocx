from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.text import WD_LINE_SPACING



def writeParagraph(document, content, font_name = 'Arial', font_size = 12, font_bold = False, font_italic = False, font_underline = False, color = RGBColor(0, 0, 0),
              before_spacing = 0, after_spacing = 0, line_spacing = WD_LINE_SPACING.ONE_POINT_FIVE, keep_together = True, keep_with_next = False, page_break_before = False,
              widow_control = False, style = 'Normal', indentation=0):

    """
    Creacion de un Párrafo.
    Se definen los criterios aplicados al estilo.
    Se aplican los estilos al texto.
    """

    paragraph = document.add_paragraph(str(content))

    paragraph.style = style
    font = paragraph.style.font

    # CRITERIO 1: ESTILO DE FUENTE
    font.name = font_name

    # CRITERIO 2: TAMAÑO DE LETRA
    font.size = Pt(font_size)
    font.bold = font_bold
    font.italic = font_italic
    font.underline = font_underline
    font.color.rgb = color

    paragraph_format = paragraph.paragraph_format
    paragraph_format.space_before = Pt(before_spacing)
    paragraph_format.space_after = Pt(after_spacing)

    # CRITERIO 3: INTERLINEADO 
    paragraph_format.line_spacing_rule = line_spacing
    
    paragraph_format.keep_together = keep_together
    paragraph_format.keep_with_next = keep_with_next
    paragraph_format.page_break_before = page_break_before
    paragraph_format.widow_control = widow_control

    # CRITERIO 4: ALINEACION IZQUIERDA
    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

    # Listas
    if indentation!=0:
        paragraph.paragraph_format.left_indent = Pt(36)