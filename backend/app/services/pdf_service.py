 
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
import io

class PDFService:
    @staticmethod
    def generate_business_plan_pdf(idea_data: dict) -> bytes:
        """
        Generate a professional PDF business plan
        """
        # Create PDF buffer
        pdf_buffer = io.BytesIO()
        
        # Create PDF document
        doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=letter,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch
        )
        
        # Container for PDF elements
        elements = []
        
        # Get styles
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1f2937'),
            spaceAfter=12,
            alignment=1  # Center alignment
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#374151'),
            spaceAfter=6,
            spaceBefore=12
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['BodyText'],
            fontSize=11,
            textColor=colors.HexColor('#4b5563'),
            spaceAfter=6,
            alignment=4  # Justify alignment
        )
        
        # Title
        title = Paragraph(f"<b>{idea_data.get('title', 'Business Plan')}</b>", title_style)
        elements.append(title)
        elements.append(Spacer(1, 0.2*inch))
        
        # Metadata
        date_generated = datetime.now().strftime("%B %d, %Y")
        metadata_text = f"Generated on: {date_generated} | Industry: {idea_data.get('industry', 'N/A')}"
        metadata = Paragraph(metadata_text, styles['Normal'])
        elements.append(metadata)
        elements.append(Spacer(1, 0.3*inch))
        
        # Business Description
        elements.append(Paragraph("<b>Business Description</b>", heading_style))
        description = Paragraph(idea_data.get('description', 'N/A'), body_style)
        elements.append(description)
        elements.append(Spacer(1, 0.2*inch))
        
        # Business Model
        elements.append(Paragraph("<b>Business Model</b>", heading_style))
        business_model = Paragraph(idea_data.get('business_model', 'N/A'), body_style)
        elements.append(business_model)
        elements.append(Spacer(1, 0.2*inch))
        
        # Target Audience
        elements.append(Paragraph("<b>Target Audience</b>", heading_style))
        target_audience = Paragraph(idea_data.get('target_audience', 'N/A'), body_style)
        elements.append(target_audience)
        elements.append(Spacer(1, 0.2*inch))
        
        # SWOT Analysis
        elements.append(Paragraph("<b>SWOT Analysis</b>", heading_style))
        swot = Paragraph(idea_data.get('swot_analysis', 'N/A'), body_style)
        elements.append(swot)
        elements.append(Spacer(1, 0.2*inch))
        
        # Market Potential
        elements.append(Paragraph("<b>Market Potential</b>", heading_style))
        market = Paragraph(idea_data.get('market_potential', 'N/A'), body_style)
        elements.append(market)
        elements.append(Spacer(1, 0.3*inch))
        
        # Keywords
        elements.append(Paragraph("<b>Keywords</b>", heading_style))
        keywords = Paragraph(idea_data.get('keywords', 'N/A'), body_style)
        elements.append(keywords)
        
        # Build PDF
        doc.build(elements)
        
        # Get PDF bytes
        pdf_buffer.seek(0)
        return pdf_buffer.getvalue()