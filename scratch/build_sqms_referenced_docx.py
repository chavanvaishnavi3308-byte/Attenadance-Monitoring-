import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def build_attendx_sqms_referenced_docx():
    print("="*70)
    print("BUILDING ATTENDX DOCUMENTATION (SQMS REFERENCED FORMAT) IN DOCX")
    print("="*70)

    doc = docx.Document()

    # Page setup: Standard Letter (8.5 x 11.0 in) matching SQMS.pdf
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11.0)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

    # Styles setup
    style_normal = doc.styles['Normal']
    font_normal = style_normal.font
    font_normal.name = 'Times New Roman'
    font_normal.size = Pt(11)
    font_normal.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    # XML Helper functions
    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        for child in list(tcPr):
            if child.tag.endswith('shd'):
                tcPr.remove(child)
        tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

    def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table):
        tblPr = table._tbl.tblPr
        for child in list(tblPr):
            if child.tag.endswith('tblBorders'):
                tblPr.remove(child)
        borders_xml = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:left w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
            f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>'
            f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders_xml)

    def add_chapter_header(chap_num, chap_title):
        p1 = doc.add_paragraph()
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_before = Pt(24)
        p1.paragraph_format.space_after = Pt(4)
        p1.paragraph_format.keep_with_next = True
        r1 = p1.add_run(f"CHAPTER  {chap_num}")
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(16)
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D) # Academic Deep Navy

        p2 = doc.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(20)
        p2.paragraph_format.keep_with_next = True
        r2 = p2.add_run(chap_title.upper())
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(14)
        r2.font.bold = True
        r2.font.color.rgb = RGBColor(0x24, 0x3F, 0x60)
        return p2

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x24, 0x3F, 0x60)
        return p

    def add_h4(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(7)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.italic = True
        run.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
        return p

    def add_p(text, bold_prefix=None, space_after=6):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.name = 'Times New Roman'
            r_bold.font.size = Pt(11)
            r_bold.font.bold = True
            r_bold.font.color.rgb = RGBColor(0x1A, 0x20, 0x2C)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
        return p

    def add_bullet(text, bold_prefix=None, level=0):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.left_indent = Inches(0.25 * (level + 1))
        
        # Bullet symbol matching SQMS format
        r_bullet = p.add_run("\u2022  ")
        r_bullet.font.name = 'Arial'
        r_bullet.font.size = Pt(10)
        r_bullet.font.bold = True
        r_bullet.font.color.rgb = RGBColor(0x24, 0x3F, 0x60)

        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.name = 'Times New Roman'
            r_bold.font.size = Pt(11)
            r_bold.font.bold = True
            r_bold.font.color.rgb = RGBColor(0x1A, 0x20, 0x2C)
            
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
        return p

    def add_numbered_item(num_str, bold_title, text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.left_indent = Inches(0.25)

        r_num = p.add_run(f"{num_str}.  ")
        r_num.font.name = 'Times New Roman'
        r_num.font.size = Pt(11)
        r_num.font.bold = True
        r_num.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

        if bold_title:
            r_title = p.add_run(bold_title + "  ")
            r_title.font.name = 'Times New Roman'
            r_title.font.size = Pt(11)
            r_title.font.bold = True
            r_title.font.color.rgb = RGBColor(0x1A, 0x20, 0x2C)

        r_txt = p.add_run(text)
        r_txt.font.name = 'Times New Roman'
        r_txt.font.size = Pt(11)
        r_txt.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
        return p

    def add_fig(img_name, caption_text, width=6.0):
        candidate_paths = [
            os.path.join('diagrams', img_name),
            os.path.join('screenshots', img_name),
            os.path.join(os.path.dirname(__file__), '..', 'diagrams', img_name),
            os.path.join(os.path.dirname(__file__), '..', 'screenshots', img_name),
            img_name
        ]
        img_path = None
        for cp in candidate_paths:
            if os.path.exists(cp):
                img_path = cp
                break

        if img_path:
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(10)
            p_img.paragraph_format.space_after = Pt(3)
            p_img.paragraph_format.keep_with_next = True
            p_img.add_run().add_picture(img_path, width=Inches(width))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(3)
            p_cap.paragraph_format.space_after = Pt(12)
            r = p_cap.add_run(caption_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.italic = True
            r.font.color.rgb = RGBColor(0x4A, 0x55, 0x68)
        else:
            print(f"WARNING: Image not found: {img_name}")

    def create_table(headers, data, col_widths=None):
        table = doc.add_table(rows=len(data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(table)

        # Header Row
        hdr_row = table.rows[0]
        hdr_trPr = hdr_row._tr.get_or_add_trPr()
        hdr_trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

        for i, h in enumerate(headers):
            cell = hdr_row.cells[i]
            set_cell_background(cell, "243F60") # Academic Navy
            set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(h)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        # Data Rows
        for r_idx, row_data in enumerate(data):
            row = table.rows[r_idx + 1]
            bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, val in enumerate(row_data):
                cell = row.cells[c_idx]
                if bg_color != "FFFFFF":
                    set_cell_background(cell, bg_color)
                set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.15
                r = p.add_run(str(val))
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9.5)
                r.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

        # Column widths
        if col_widths and len(col_widths) == len(headers):
            for row in table.rows:
                for i, w in enumerate(col_widths):
                    if isinstance(w, docx.shared.Length):
                        row.cells[i].width = w
                    else:
                        row.cells[i].width = Inches(float(w))

        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(0)
        p_after.paragraph_format.space_after = Pt(6)
        return table

    def add_code_block(code_str, language="JavaScript"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.rows[0].cells[0]
        cell.width = Inches(6.5)
        set_cell_background(cell, "F1F5F9")
        set_cell_margins(cell, top=120, bottom=120, left=160, right=160)
        
        # Border
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="6" w:space="0" w:color="CBD5E0"/>'
            f'<w:left w:val="single" w:sz="18" w:space="0" w:color="2B6CB0"/>'
            f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="CBD5E0"/>'
            f'<w:right w:val="single" w:sz="6" w:space="0" w:color="CBD5E0"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        
        lines = code_str.strip().split('\n')
        for i, l in enumerate(lines):
            r = p.add_run(l + ('\n' if i < len(lines)-1 else ''))
            r.font.name = 'Consolas'
            r.font.size = Pt(9.0)
            r.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(0)
        p_after.paragraph_format.space_after = Pt(6)

    return doc, {
        'add_chapter_header': add_chapter_header,
        'add_h2': add_h2,
        'add_h3': add_h3,
        'add_h4': add_h4,
        'add_p': add_p,
        'add_bullet': add_bullet,
        'add_numbered_item': add_numbered_item,
        'add_fig': add_fig,
        'create_table': create_table,
        'add_code_block': add_code_block
    }

if __name__ == "__main__":
    doc, helpers = build_attendx_sqms_referenced_docx()
    print("Helper environment ready.")
