import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# Import section builders
from build_sqms_referenced_docx import build_attendx_sqms_referenced_docx
from sections_front_matter import add_front_matter
from sections_ch1_ch2 import add_chapter1_and_chapter2
from sections_ch3_ch4 import add_chapter3_and_chapter4
from sections_ch5_ch7 import add_chapters_5_6_7_and_refs

def generate_full_docx():
    print("=" * 80)
    print("STARTING FULL ATTENDX DOCUMENTATION GENERATION (SQMS.PDF REFERENCED FORMAT)")
    print("=" * 80)

    doc, helpers = build_attendx_sqms_referenced_docx()

    # Configure Header & Footer
    section = doc.sections[0]
    
    # Header
    header = section.header
    p_hdr = header.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_hdr = p_hdr.add_run("AttendX: Smart Attendance Monitoring & Parent Notification System")
    r_hdr.font.name = 'Times New Roman'
    r_hdr.font.size = Pt(8.5)
    r_hdr.font.italic = True
    r_hdr.font.color.rgb = RGBColor(0x71, 0x80, 0x96)

    # Footer
    footer = section.footer
    p_ftr = footer.paragraphs[0]
    p_ftr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    
    # Left part in footer
    r_ftr_dept = p_ftr.add_run("Dept. of Computer Science & Engineering | Academic Project Report              Page ")
    r_ftr_dept.font.name = 'Times New Roman'
    r_ftr_dept.font.size = Pt(8.5)
    r_ftr_dept.font.color.rgb = RGBColor(0x71, 0x80, 0x96)

    # XML Page Number Field
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    
    r_page = p_ftr.add_run()
    r_page._r.append(fldChar1)
    r_page._r.append(instrText)
    r_page._r.append(fldChar2)
    r_page._r.append(fldChar3)
    r_page.font.name = 'Times New Roman'
    r_page.font.size = Pt(8.5)
    r_page.font.bold = True
    r_page.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    # 1. Add Front Matter (Cover, Certificate, Declaration, Acknowledgements, Abstract, TOC, List of Figures, List of Tables)
    print("\n[Step 1/4] Adding Front Matter...")
    add_front_matter(doc, helpers)

    # 2. Add Chapters 1 and 2 (Introduction & Survey of Technologies)
    print("[Step 2/4] Adding Chapter 1 (Introduction) & Chapter 2 (Survey of Technologies)...")
    add_chapter1_and_chapter2(doc, helpers)

    # 3. Add Chapters 3 and 4 (Requirements and Analysis & System Design with 10 UML Models)
    print("[Step 3/4] Adding Chapter 3 (Requirements & Analysis) & Chapter 4 (System Design)...")
    add_chapter3_and_chapter4(doc, helpers)

    # 4. Add Chapters 5, 6, 7 and References (Implementation, Testing, Results 9 Screens, Conclusion, References)
    print("[Step 4/4] Adding Chapter 5 (Implementation & Testing), Chapter 6 (Results & Discussion), Chapter 7 (Conclusion), and References...")
    add_chapters_5_6_7_and_refs(doc, helpers)

    output_filename = "AttendX_Project_Documentation.docx"
    doc.save(output_filename)
    
    file_size = os.path.getsize(output_filename)
    print("\n" + "=" * 80)
    print(f"SUCCESS: Document successfully created at: {output_filename}")
    print(f"File size: {file_size:,} bytes (~ {round(file_size / (1024*1024), 2)} MB)")
    print("=" * 80)

if __name__ == "__main__":
    generate_full_docx()

