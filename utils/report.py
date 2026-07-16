from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    products,
    confidence,
    inventory,
    quality,
    decision
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>RetailBrainAI Report</b>",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "<br/>",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Detected Products: {products}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Confidence: {confidence:.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Inventory Status: {inventory}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Detection Quality: {quality}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Final Decision: {decision}",
            styles["BodyText"]
        )
    )

    doc.build(elements)
