from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def welcome(request):
    return render(request,'welcome.html')

def home(request):
    billing_solutions=[
                "Experienced billing experts providing high-quality services and the latest industry insights",
                "Customized solutions designed to meet the specific needs of each practice for maximum efficiency",
                "Leveraging advanced billing technology to simplify workflows and improve precision",
                "Proactively handling claims and follow-ups to guarantee prompt reimbursements",
                "Transparent communication with consistent updates and comprehensive reporting",
              ]
    return render(request, "home.html",{'data':billing_solutions})

def aboutus(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def rcm(request):
    features = [
        {"title": "Patient Registration & Insurance Verification", "desc": "We verify patient insurance details upfront, reducing claim denials and ensuring a seamless billing process."},
        {"title": "Medical Coding & Charge Entry", "desc": "Our certified coders accurately translate medical services into standardized codes, preventing costly errors."},
        {"title": "Claims Submission & Tracking", "desc": "We submit claims promptly and monitor their progress, addressing any issues that may cause delays in payments."},
        {"title": "Denial Management & Appeals", "desc": "If a claim is denied, our team immediately investigates and resubmits it, ensuring you receive the revenue you deserve."},
        {"title": "Payment Posting & Reconciliation", "desc": "We track payments, post them accurately, and reconcile accounts to maintain financial transparency."},
        {"title": "Patient Billing & Support", "desc": "We handle patient statements and inquiries, making it easy for patients to understand their bills and complete payments."},
    ]
    return render(request, 'rcm.html', {'features': features})

def credentialing(request):
    features = [
        { "title": "Faster Reimbursements", "desc": "Ensures your providers receive payments without unnecessary delays." },
        { "title": "Regulatory Compliance", "desc": "Stay aligned with insurance and government healthcare policies." },
        { "title": "Enhanced Credibility", "desc": "Being credentialed with top insurance companies enhances patient trust." },
        { "title": "Less Administrative Work", "desc": "We handle paperwork, follow-ups, and verifications for you." }
    ]
    return render(request, 'credentialing.html', {'features': features})

def medical_coding(request):
    features = [
        {
            "title": "Maximized Reimbursements",
            "desc": "Avoid underbilling or overbilling by using precise codes"
        },
        {
            "title": "Compliance Assurance",
            "desc": "Stay compliant with HIPAA, CMS, and insurance guidelines"
        },
        {
            "title": "Reduced Claim Denials",
            "desc": "Proper coding reduces errors that lead to claim rejections"
        },
        {
            "title": "Efficient Billing Process",
            "desc":"Speeds up the claims process and improves cash flow"
        },
        {
            "title": "Specialty-Specific Expertise",
            "desc":"We handle coding for various specialties like cardiology, orthopedics, and more"
        },
    ];
    return render(request, 'medicalcoding.html', {'features': features})

def billing(request):
    features = [
        {
            "title": "Timely Claim Submission",
            "desc":" We handle all claim submissions with precision to avoid delays"
        },
        {
            "title": "Denial Management ",
            "desc":"Our team reviews and corrects denied claims to ensure reimbursement"
                },
        {
            "title": "Insurance Follow-Ups",
            "desc":"We proactively communicate with insurers to track and resolve pending payments"
        },
        {
            "title": "Patient Billing Assistance",
            "desc":" Clear, transparent billing helps minimize confusion and payment delays"
        },
        {
            "title": "Maximized Reimbursements",
            "desc":" We ensure you receive the full amount owed for services provided"
        }
    ]
    return render(request, 'billing.html', {'features': features})

def compliance_report(request):
    features = [
        {
        "title": "HIPAA Compliance",
        "desc": "We adhere to strict HIPAA guidelines to protect patient data"
    },
    {
        "title": "Compliance Audits",
        "desc": "Periodic audits of your billing and coding practices to ensure compliance with current industry regulations"
    },
    {
        "title": "Custom Reporting",
        "desc": "Generate tailored financial reports to track the health of your practice’s revenue cycle and identify areas for improvement."
    }
    ]
    return render(request, 'compliancereport.html', {'features': features})

def dental(request):
    features = [
        {
            "title": "Insurance Claims Management",
            "desc": "We handle all aspects of dental insurance billing, including claim submissions, follow-ups, and appeals, ensuring you get maximum reimbursements"
        },
        {
            "title": "Insurance Verification & Pre-Authorization",
            "desc": "We verify patient eligibility, benefits, and pre-authorizations in advance, reducing claim denials and improving cash flow"
        },
        {
            "title": "Secure Billing",
            "desc": "We ensure all billing processes follow strict HIPAA regulations, keeping your patients' data safe and confidential"
        },
        {
            "title": "Customized Solutions",
            "desc": "Customized Solutions for Dental Practices including Preventive & Restorative Dentistry,Orthodontics & Periodontics,Endodontics & Prosthodontics"
        },
        {
            "title": "Dedicated Support & Reporting",
            "desc": "Get access to real-time financial reports, claim status updates, and expert guidance to optimize your revenue cycle"
        }
    ]
    return render(request, 'dental.html', {'features': features})

from django.shortcuts import render

def contact_view(request):
    errors = {}
    form_data = {}
    contactDetails = [
        {
            "icon": "assets/pin.png",
            "title": "Address",
            "content": "5729 savoy dr Houston tx 77036",
            "ref": "https://www.google.com/maps/search/?api=1&query=5729+Savoy+Dr,+Houston,+TX+77036"
        },
        {
            "icon": "assets/email.png",
            "title": "Email Us",
            "content": "skzmedicalbilling@gmail.com",
            "ref": "mailto:skzmedicalbilling@gmail.com"
        },
        {
            "icon": "assets/telephone.png",
            "title": "Call Now",
            "content": "(469) 733-6551",
            "ref": "tel:+14697336551"
        },
    ]
    if request.method == "POST":
        form_data = {
            "first_name": request.POST.get("first_name", "").strip(),
            "last_name": request.POST.get("last_name", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "phone": request.POST.get("phone", "").strip(),
            "service": request.POST.get("service", "").strip(),
            "message": request.POST.get("message", "").strip(),
        }

        # ✅ First Name Validation
        if not form_data["first_name"]:
            errors["first_name"] = "First name is required."
        elif len(form_data["first_name"]) < 2:
            errors["first_name"] = "First name must be at least 2 characters."

        # ✅ Last Name Validation
        if not form_data["last_name"]:
            errors["last_name"] = "Last name is required."

        # ✅ Email Validation
        if not form_data["email"]:
            errors["email"] = "Email is required."
        elif "@" not in form_data["email"]:
            errors["email"] = "Enter a valid email address."

        # ✅ Phone Number Validation
        if not form_data["phone"]:
            errors["phone"] = "Phone number is required."
        elif not form_data["phone"].isdigit():
            errors["phone"] = "Phone number must contain only digits."

        # ✅ Service Selection Validation
        if not form_data["service"]:
            errors["service"] = "Please select a service."

        if not errors:
            # ✅ Form is valid, process the data (e.g., save to DB)
            return render(request, "contact_success.html", {"form_data": form_data})
        

    return render(request, "contact.html", {'data': contactDetails,"errors": errors, "form_data": form_data})



def appointment_request(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName', '').strip()
        last_name = request.POST.get('lastName', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        # Email content
        subject = f"New Contact Form Submission - {first_name} {last_name}"
        
        # HTML Email Body (Corrected)
        body = f"""
        <div style="font-family: Arial, sans-serif; border: 1px solid #ddd; padding: 20px; border-radius: 8px; background-color: #f9f9f9;">
            <h2 style="color: #0097B2;">📧 New Appointment Request</h2>
            <p><strong>Name:</strong> {first_name} {last_name}</p>
            <p><strong>Email:</strong> <a href="mailto:{email}" style="color: #0097B2;">{email}</a></p>
            <p><strong>Phone:</strong> {phone}</p>
            <p><strong>Service Requested:</strong> {service}</p>
            <p><strong>Message:</strong></p>
            <blockquote style="background: #f1f1f1; padding: 10px; border-left: 5px solid #0097B2;">
                {message}
            </blockquote>
            <br/>
            <p style="color: #888;">Please reach out to the client at your earliest convenience to confirm the appointment.</p>
            <p><strong>Best Regards,</strong></p>
            <p><strong>SKZ Medical Billing Team</strong></p>
        </div>
        """

        # Send Email
        send_mail(
            subject,
            "",  # Plain text body (optional)
            email,  # Sender Email
            ['designerhub455@gmail.com'],  # Receiver Email (Admin email)
            fail_silently=False,
            html_message=body  # ✅ Send HTML email
        )
        
        return render(request, 'contact.html', {'success': "Your request has been submitted successfully!"})


    return render(request, 'contact.html')

def privacy_policy(request):
    return render(request,'privacy-policy.html')