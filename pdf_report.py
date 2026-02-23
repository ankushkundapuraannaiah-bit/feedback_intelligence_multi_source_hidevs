from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt


def generate_chart(df, path="trend.png"):
    plt.figure()
    plt.plot(df["date"], df["confidence"])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path


def generate_pdf(summary_text, trend_df, filename="weekly_report.pdf"):

    chart_path = generate_chart(trend_df)

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("Weekly Feedback Report", styles["Title"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(summary_text, styles["BodyText"]))
    elements.append(Spacer(1, 12))

    elements.append(Image(chart_path, width=400, height=200))

    doc.build(elements)