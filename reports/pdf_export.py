# reports/pdf_export.py

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from reports.vehicle_health_report import (
    generate_vehicle_health_report
)

from reports.trip_report import (
    generate_trip_report
)

from reports.fault_report import (
    generate_fault_report
)


def generate_pdf_report():

    pdf_file = "vehicle_report.pdf"

    document = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph(
            "SMART TELEMETRY ECU REPORT",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 12))

    # -------------------------
    # Vehicle Health Report
    # -------------------------

    health_report = generate_vehicle_health_report()

    elements.append(
        Paragraph(
            "Vehicle Health Report",
            styles["Heading2"]
        )
    )

    if isinstance(health_report, dict):

        for key, value in health_report.items():

            elements.append(
                Paragraph(
                    f"{key}: {value}",
                    styles["BodyText"]
                )
            )

    elements.append(Spacer(1, 10))

    # -------------------------
    # Trip Report
    # -------------------------

    trip_report = generate_trip_report()

    elements.append(
        Paragraph(
            "Trip Report",
            styles["Heading2"]
        )
    )

    for key, value in trip_report.items():

        elements.append(
            Paragraph(
                f"{key}: {value}",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 10))

    # -------------------------
    # Fault Report
    # -------------------------

    fault_report = generate_fault_report()

    elements.append(
        Paragraph(
            "Fault Report",
            styles["Heading2"]
        )
    )

    for fault in fault_report:

        elements.append(
            Paragraph(
                fault,
                styles["BodyText"]
            )
        )

    # Build PDF
    document.build(elements)

    print("\nPDF Report Generated Successfully!")
    print(f"File Name : {pdf_file}")